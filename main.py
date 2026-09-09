import time
from urllib.parse import urlparse, parse_qs

from pypresence import Presence
from pypresence.types import ActivityType
from config import CLIENT_ID, POLL_INTERVAL
from safari import get_active_youtube


def connect_discord():

    print("Connecting to Discord...")

    rpc = Presence(CLIENT_ID)
    rpc.connect()

    print("Discord connected!")

    return rpc


def clean_title(title):

    if title.endswith(" - YouTube"):
        title = title[:-10]

    return title.strip()


def get_video_id(url):

    try:
        parsed = urlparse(url)

        if parsed.hostname in ("www.youtube.com", "youtube.com", "m.youtube.com"):
            return parse_qs(parsed.query).get("v", [None])[0]

        if parsed.hostname == "youtu.be":
            return parsed.path.strip("/").split("/")[0]

    except Exception:
        pass

    return None


def get_thumbnail_url(url):

    video_id = get_video_id(url)

    if not video_id:
        return None

    youtube_thumbnail = f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"

    return (
        "https://images.weserv.nl/"
        "?url=" + youtube_thumbnail.replace("://", "%3A%2F%2F").replace("/", "%2F")
        + "&trim=20"
        + "&w=512"
        + "&h=512"
        + "&fit=cover"
    )


def update_presence(rpc, video):

    title = clean_title(video["title"])
    channel = video.get("channel", "").strip()

    current_time = video["current_time"]
    duration = video["duration"]
    status = video["status"]
    video_url = video["url"]

    thumbnail_url = get_thumbnail_url(video_url)

    if channel:
        activity_name = f"YouTube 🍓 · {channel}"
    else:
        activity_name = "YouTube 🍓"

    activity_name = activity_name[:128]

    if thumbnail_url:
        large_image = thumbnail_url
    else:
        large_image = "bearly-watching"

    if status == "LIVE_PLAYING":

        rpc.update(
            activity_type=ActivityType.WATCHING,
            name=activity_name,
            details=title[:128],
            state="🔴 watching live ♡",
            large_image=large_image,
            large_text="Watch this video on YouTube",
            large_url=video_url,
            small_image="watching",
            small_text="Watching Live Stream 🔴",
            buttons=[
                {
                    "label": "Watch Video",
                    "url": video_url
                }
            ]
        )

    elif status == "LIVE_PAUSED":

        rpc.update(
            activity_type=ActivityType.WATCHING,
            name=activity_name,
            details=title[:128],
            state="▶️ live stream paused ♡",
            large_image=large_image,
            large_text="Watch this video on YouTube",
            large_url=video_url,
            small_image="watching",
            small_text="Live Stream Paused ▶️",
            buttons=[
                {
                    "label": "Watch Video",
                    "url": video_url
                }
            ]
        )

    elif status == "PLAYING":

        start_time = time.time() - current_time
        end_time = start_time + duration

        rpc.update(
            activity_type=ActivityType.WATCHING,
            name=activity_name,
            details=title[:128],
            state="🧸 little youtube break ♡",
            start=int(start_time),
            end=int(end_time),
            large_image=large_image,
            large_text="Watch this video on YouTube",
            large_url=video_url,
            small_image="watching",
            small_text="Watching YouTube 🍓",
            buttons=[
                {
                    "label": "Watch Video",
                    "url": video_url
                }
            ]
        )

    elif status == "PAUSED":

        rpc.update(
            activity_type=ActivityType.WATCHING,
            name=activity_name,
            details=title[:128],
            state="🛌 little bear is resting ♡",
            large_image=large_image,
            large_text="Watch this video on YouTube",
            large_url=video_url,
            small_image="watching",
            small_text="YouTube Paused 💤",
            buttons=[
                {
                    "label": "Watch Video",
                    "url": video_url
                }
            ]
        )

    elif status == "ENDED":

        rpc.update(
            activity_type=ActivityType.WATCHING,
            name=activity_name,
            details=title[:128],
            state="🍓 finished watching ♡",
            large_image=large_image,
            large_text="Watch this video on YouTube",
            large_url=video_url,
            small_image="watching",
            small_text="Finished Watching 🍓",
            buttons=[
                {
                    "label": "Watch Video",
                    "url": video_url
                }
            ]
        )


def clear_presence(rpc):

    try:
        rpc.clear()
    except Exception:
        pass


def main():

    print()
    print("╭──────────────────────────────────╮")
    print("│      Bearly Watching          │")
    print("│      Safari → Discord         │")
    print("╰──────────────────────────────────╯")
    print()

    rpc = None

    last_url = None
    last_status = None
    last_channel = None

    try:

        while True:

            # --------------------------------
            # Discord connection
            # --------------------------------

            if rpc is None:

                try:

                    rpc = connect_discord()

                except Exception:

                    rpc = None

                    time.sleep(5)

                    continue

            # --------------------------------
            # Safari detection
            # --------------------------------

            try:

                video = get_active_youtube()

            except Exception:

                video = None

            # --------------------------------
            # Active YouTube
            # --------------------------------

            if video:

                title = clean_title(video["title"])
                channel = video.get("channel", "").strip()
                status = video["status"]
                url = video["url"]

                if (
                    url != last_url
                    or status != last_status
                    or channel != last_channel
                ):

                    print()
                    print("Now watching:")
                    print(f"   {title}")

                    if channel:
                        print(f"Channel:")
                        print(f"   {channel}")

                    print(f"Status: {status}")
                    print(f"{url}")

                    last_url = url
                    last_status = status
                    last_channel = channel

                # --------------------------------
                # Update Discord
                # --------------------------------

                try:

                    update_presence(rpc, video)

                except Exception:

                    # Discord connection was lost.
                    try:
                        rpc.close()
                    except Exception:
                        pass

                    rpc = None

                    time.sleep(2)

            # --------------------------------
            # No active YouTube
            # --------------------------------

            else:

                if last_url is not None:

                    print()
                    print("No active YouTube video.")
                    print("Clearing Discord presence...")

                clear_presence(rpc)

                last_url = None
                last_status = None
                last_channel = None

            time.sleep(POLL_INTERVAL)

    except KeyboardInterrupt:

        print()
        print("Bearly Watching is going to sleep...")

        if rpc:

            try:
                rpc.clear()
                rpc.close()

            except Exception:
                pass

        print("Bye bye!")

    except Exception as e:

        print()
        print(f"Error: {e}")

        if rpc:

            try:
                rpc.clear()
                rpc.close()

            except Exception:
                pass


if __name__ == "__main__":
    main()
