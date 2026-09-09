import subprocess
import json


APPLE_SCRIPT = r'''
tell application "Safari"
    set output to ""

    repeat with w in windows
        repeat with t in tabs of w
            set tabURL to URL of t

            if tabURL contains "youtube.com/watch" then

                try
                    set resultText to do JavaScript "
                        (() => {
                            const v = document.querySelector('video');

                            if (!v) {
                                return 'NO_VIDEO';
                            }

                            const title =
                                document.querySelector('h1.ytd-watch-metadata')?.innerText ||
                                document.title ||
                                '';

                            const channel =
                                document.querySelector('#owner #channel-name a')?.innerText ||
                                document.querySelector('#owner #channel-name')?.innerText ||
                                document.querySelector('ytd-video-owner-renderer a')?.innerText ||
                                document.querySelector('.ytd-channel-name a')?.innerText ||
                                '';

                            const isLive =
                                !Number.isFinite(v.duration) ||
                                v.duration === Infinity ||
                                document.querySelector('.ytp-live') !== null;

                            let status;

                            if (isLive) {
                                status = v.paused ? 'LIVE_PAUSED' : 'LIVE_PLAYING';
                            } else if (v.ended) {
                                status = 'ENDED';
                            } else if (v.paused) {
                                status = 'PAUSED';
                            } else {
                                status = 'PLAYING';
                            }

                            return JSON.stringify({
                                title: title,
                                channel: channel,
                                status: status,
                                current_time: v.currentTime || 0,
                                duration: Number.isFinite(v.duration) ? v.duration : 0
                            });
                        })()
                    " in t

                    if resultText is not missing value then
                        set output to output & resultText & "|||" & tabURL & linefeed
                    end if

                on error errMsg
                    -- Ignore tabs that Safari cannot inspect
                end try

            end if
        end repeat
    end repeat

    return output
end tell
'''


def get_youtube_tabs():
    result = subprocess.run(
        ["osascript", "-e", APPLE_SCRIPT],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return []

    videos = []

    for line in result.stdout.strip().splitlines():
        if "|||" not in line:
            continue

        try:
            data, url = line.split("|||", 1)
            video = json.loads(data)

            video["url"] = url
            videos.append(video)

        except (json.JSONDecodeError, ValueError):
            continue

    return videos


def get_active_youtube():
    videos = get_youtube_tabs()

    if not videos:
        return None

    # Prefer currently playing videos
    for video in videos:
        if video["status"] == "PLAYING":
            return video

    # Then live streams that are playing
    for video in videos:
        if video["status"] == "LIVE_PLAYING":
            return video

    # Then finished videos
    for video in videos:
        if video["status"] == "ENDED":
            return video

    # Then normal paused videos
    for video in videos:
        if video["status"] == "PAUSED":
            return video

    # Finally paused live streams
    for video in videos:
        if video["status"] == "LIVE_PAUSED":
            return video

    return None
