# Bearly Watching 🧸🍓

> A tiny macOS app that turns your Safari YouTube session into Discord Rich Presence.

Bearly Watching is a lightweight, local-only macOS app that detects YouTube videos playing in Safari and displays your current watch session on Discord Rich Presence.

It can detect videos across Safari tabs — even when the YouTube tab is not currently active.

Everything runs locally on your Mac. No YouTube login, external server, or account data is required.

---

## ✨ Features

* 🎬 Detect YouTube videos across Safari tabs
* 📺 Detect YouTube channel name
* ▶️ Playing detection
* 💤 Pause detection
* 🍓 Finished video detection
* 🔴 Live stream detection
* 🖼️ Dynamic YouTube thumbnails
* ⏱️ Playback progress
* 🔗 Watch Video button
* 🔌 Discord auto-reconnect
* 🛡️ Safari and Discord error handling
* 🚀 LaunchAgent background support
* 🔒 No YouTube login or external server required

---

## 🛠️ Requirements

* macOS
* Safari
* Discord Desktop
* Python 3
* Internet connection for Discord and YouTube thumbnails
* Safari's **Allow JavaScript from Apple Events** setting enabled

---

## 🍓 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/strawbkvma/bearly-watching.git
cd bearly-watching
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Bearly Watching

```bash
python main.py
```

> Bearly Watching uses a public Discord Application ID, so you do **not** need to create your own Discord Application.

---

## 🌐 Safari Setup

Bearly Watching uses Safari's AppleScript automation and JavaScript to inspect YouTube tabs and read the HTML5 video player state.

Safari needs to allow JavaScript execution through Apple Events.

### Enable JavaScript from Apple Events

In Safari, enable:

**Develop → Allow JavaScript from Apple Events**

Depending on your macOS and Safari version, you may need to enable Safari's developer features first.

---

## 💬 Discord Rich Presence

When you are watching YouTube, Discord displays an activity similar to:

> **Watching YouTube 🍓 · Channel**

The activity can include:

* 🖼️ YouTube thumbnail
* 🎬 Video title
* 📺 Channel name
* ▶️ Current playback state
* ⏱️ Playback progress
* 🔗 Watch Video button

### Activity States

| State          | Discord Activity              |
| -------------- | ----------------------------- |
| ▶️ Playing     | `🧸 little youtube break ♡`   |
| 🛌 Paused      | `🛌 little bear is resting ♡` |
| 🍓 Finished    | `🍓 finished watching ♡`      |
| 🔴 Live        | `🔴 watching live ♡`          |
| ▶️ Live Paused | `▶️ live stream paused ♡`     |

---

## 🔴 Live Streams

Bearly Watching can distinguish between regular YouTube videos and live streams.

Live streams can be detected as:

* 🔴 Live and playing
* ▶️ Live stream paused

Because live streams do not have a normal fixed duration, playback progress is handled differently from regular videos.

---

## 🐻 Multi-Tab Detection

Bearly Watching does **not** require the YouTube tab to be your active Safari tab.

For example:

```text
Safari
├── GitHub
├── Gmail
├── Figma
├── YouTube ← playing
└── Documentation
```

Even if you are currently viewing another Safari tab, Bearly Watching can still detect the YouTube video playing in the background.

---

## 🚀 Background Mode

Bearly Watching can run automatically in the background using a macOS LaunchAgent.

The LaunchAgent allows the application to start automatically when you log into your Mac and keeps the process running.

The LaunchAgent is located at:

```text
~/Library/LaunchAgents/com.bearly-watching.plist
```

Application logs are stored locally in:

```text
logs/
├── bearly-watching.log
└── bearly-watching-error.log
```

These files are excluded from Git using `.gitignore`.

---

## 🔒 Privacy

Bearly Watching is designed to run locally on your Mac.

It does **not**:

* require a YouTube login
* access your YouTube account
* store your YouTube watch history
* use an external backend
* send your Safari history to a server
* store watch information in a database

The application only reads the YouTube tab information needed to create the Discord Rich Presence.

---

## 🏗️ Architecture

```text
┌─────────────────────┐
│       Safari        │
│                     │
│  YouTube video      │
│  playing / paused   │
└──────────┬──────────┘
           │
           │ AppleScript
           │ + JavaScript
           ▼
┌─────────────────────┐
│   Safari Detector   │
│      safari.py      │
└──────────┬──────────┘
           │
           │ Video metadata
           │ title / channel
           │ state / URL
           ▼
┌─────────────────────┐
│   Bearly Watching   │
│       main.py       │
└──────────┬──────────┘
           │
           │ Discord IPC
           ▼
┌─────────────────────┐
│       Discord       │
│   Rich Presence     │
└─────────────────────┘
```

---

## 📁 Project Structure

```text
bearly-watching/
│
├── main.py
├── safari.py
├── discord_test.py
│
├── config.py
├── config.example.py
├── requirements.txt
│
├── README.md
├── LICENSE
└── .gitignore
```

### Main Files

#### `main.py`

Controls the main application loop, Discord Rich Presence, state updates, reconnect logic, and error handling.

#### `safari.py`

Handles Safari automation and YouTube video detection.

#### `discord_test.py`

Utility for testing the Discord Rich Presence connection.

#### `config.py`

Contains the public Discord Application ID and polling interval.

#### `config.example.py`

Example configuration file for reference.

---

## ⚙️ Configuration

The default polling interval is:

```python
POLL_INTERVAL = 5
```

This means Bearly Watching checks Safari approximately every 5 seconds.

You can adjust the interval if needed:

```python
POLL_INTERVAL = 3
```

A lower value provides faster updates but may increase CPU usage.

---

## 🐛 Troubleshooting

### Discord does not show the Rich Presence

Make sure:

1. Discord Desktop is running.
2. You are logged into Discord.
3. Bearly Watching can connect to Discord.
4. YouTube is open in Safari.
5. Bearly Watching is running with:

```bash
python main.py
```

---

### YouTube is not detected

Make sure:

1. The video is open in Safari.
2. The URL is a YouTube video page.
3. **Allow JavaScript from Apple Events** is enabled.
4. Safari is running.
5. The video has finished loading.

---

### Bearly Watching detects the wrong video

Bearly Watching checks multiple Safari tabs and prioritizes an actively playing YouTube video.

If multiple YouTube videos are playing simultaneously, the selected video may depend on the order in which Safari tabs are detected.

---

### Check application logs

If Bearly Watching is running through LaunchAgent:

```bash
tail -f logs/bearly-watching.log
```

For errors:

```bash
tail -f logs/bearly-watching-error.log
```

---

## 🛡️ Security Notes

The Discord Application ID is intentionally included in the project configuration.

Discord Application IDs are public identifiers and are **not equivalent to passwords, bot tokens, or client secrets**.

Never publish:

* Discord bot tokens
* OAuth client secrets
* Personal access tokens
* Private API keys
* Authentication credentials

---

## 🗺️ Roadmap

* [x] YouTube multi-tab detection
* [x] Playing and paused states
* [x] Finished video detection
* [x] Live stream detection
* [x] Dynamic thumbnails
* [x] Playback progress
* [x] Discord auto-reconnect
* [x] LaunchAgent background support
* [ ] Easier one-command installation
* [ ] Improved LaunchAgent installer
* [ ] Better handling of multiple simultaneously playing videos
* [ ] Customizable Rich Presence messages
* [ ] Optional configuration UI
* [ ] More YouTube page compatibility

---

## 📜 License

Bearly Watching is open-source software licensed under the MIT License.

See [`LICENSE`](LICENSE) for details.

---

## 🧸🍓 About

Bearly Watching started as a small macOS automation project built around Safari, YouTube, and Discord Rich Presence.

The goal is simple:

> Make your Discord status feel a little more like you. 🧸🍓

Made with 🧸🍓 and probably too much YouTube.
