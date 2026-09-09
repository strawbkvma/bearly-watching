# Bearly Watching 🧸🍓

> A simple macOS app that turns your Safari YouTube session into Discord Rich Presence.

**Bearly Watching** is a lightweight, local-only macOS app that detects YouTube videos playing in Safari and turns your current watch session into a cute simple Youtube Discord Rich Presence.

It works across Safari tabs — even when the YouTube tab isn't currently active.

Everything runs locally on your Mac.
No YouTube login. No external backend. No tracking.

---

## ✨ Features

* 🎬 Detect YouTube videos across Safari tabs
* 📺 Detect YouTube channel names
* ▶️ Playing detection
* 💤 Pause detection
* 🍓 Finished video detection
* 🔴 Live stream detection
* 🖼️ Dynamic YouTube thumbnails
* ⏱️ Playback progress
* 🔗 Watch Video button
* 🔌 Discord auto-reconnect
* 🛡️ Safari & Discord error handling
* 🚀 Automatic background mode with LaunchAgent
* 🔒 Local-only architecture

---

## 🛠️ Requirements

Before installing, make sure you have:

* macOS
* Safari
* Discord Desktop
* Python 3
* An active internet connection for Discord and YouTube thumbnails

You will also need to enable Safari's:

**Develop → Allow JavaScript from Apple Events**

---

## 🍓 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/strawbkvma/bearly-watching.git
cd bearly-watching
```

### 2. Run the installer

```bash
./install.sh
```

The installer automatically:

* 🐍 Creates a Python virtual environment
* 📦 Installs the required dependencies
* 📁 Creates the local `logs/` directory
* 🚀 Configures the macOS LaunchAgent
* 🧸 Starts Bearly Watching in the background

You don't need to create your own Discord Application.

Bearly Watching uses a public Discord Application ID included in the project configuration.

---

### 3. Enable Safari automation

Before Bearly Watching can detect YouTube videos, enable:

**Safari → Develop → Allow JavaScript from Apple Events**

Depending on your macOS and Safari version, you may need to enable Safari's developer features first.

macOS may also ask for permission to allow automation between applications.

> **Tip:** If macOS shows an automation permission prompt, allow it so Bearly Watching can communicate with Safari.

---

### 4. Open YouTube in Safari

Open a YouTube video in Safari and start playing it.

Bearly Watching will automatically detect the video and update your Discord Rich Presence.

You can even switch to another Safari tab while the YouTube video continues playing.

That's it. 🧸🍓

---

## 💬 Discord Rich Presence

When you're watching YouTube, Discord displays an activity similar to:

> **Watching YouTube 🍓 · Channel**

Depending on the current playback state, your activity can include:

* 🖼️ YouTube thumbnail
* 🎬 Video title
* 📺 Channel name
* ▶️ Playback state
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

Supported live states include:

* 🔴 Live and playing
* ▶️ Live stream paused

Because live streams don't have a normal fixed duration, playback progress is handled differently from regular videos.

---

## 🐻 Multi-Tab Detection

Bearly Watching doesn't require YouTube to be your active Safari tab.

For example:

```text
Safari
├── GitHub
├── Gmail
├── Figma
├── YouTube ← playing
└── Documentation
```

Even if you're working in another Safari tab, Bearly Watching can still detect the YouTube video playing in the background.

Perfect for those:

> "I'm definitely working."
> *YouTube is playing in another tab.* 🧸

---

## 🚀 Background Mode

Bearly Watching automatically configures a macOS **LaunchAgent** when you run:

```bash
./install.sh
```

The LaunchAgent:

* starts Bearly Watching automatically when you log in
* keeps the application running in the background
* allows Rich Presence updates without keeping Terminal open

The LaunchAgent is created at:

```text
~/Library/LaunchAgents/com.bearly-watching.plist
```

### Application Logs

Logs are stored locally in:

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

The application only reads the YouTube tab information required to create the Discord Rich Presence.

Your browsing stays on your Mac. 🧸🍓

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
├── discord-test.py
├── install.sh
│
├── config.py
├── requirements.txt
│
├── README.md
├── LICENSE
└── .gitignore
```

The following directories are created locally and are **not included in the repository**:

```text
.venv/
logs/
```

### Main Files

#### `main.py`

Controls the main application loop, Discord Rich Presence, state updates, reconnect logic, and error handling.

#### `safari.py`

Handles Safari automation and YouTube video detection.

#### `discord_test.py`

A utility for testing the Discord Rich Presence connection.

#### `install.sh`

Automates the installation process, including environment setup, dependency installation, logging setup, and LaunchAgent configuration.

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

This means Bearly Watching checks Safari approximately every **5 seconds**.

You can adjust the interval if needed:

```python
POLL_INTERVAL = 3
```

A lower value provides faster updates but may increase CPU usage.

---

## 🐛 Troubleshooting

### Discord doesn't show the Rich Presence

Make sure:

1. Discord Desktop is running.
2. You are logged into Discord.
3. Bearly Watching is running.
4. YouTube is open in Safari.
5. Safari automation permissions have been granted.

You can check the application logs with:

```bash
tail -f logs/bearly-watching.log
```

For errors:

```bash
tail -f logs/bearly-watching-error.log
```

---

### YouTube is not detected

Make sure:

1. The video is open in Safari.
2. The URL is a YouTube video page.
3. **Allow JavaScript from Apple Events** is enabled.
4. Safari is running.
5. The video has finished loading.
6. macOS automation permissions have been granted.

---

### Bearly Watching detects the wrong video

Bearly Watching checks multiple Safari tabs and prioritizes an actively playing YouTube video.

If multiple YouTube videos are playing simultaneously, the selected video may depend on the order in which Safari tabs are detected.

---

### LaunchAgent is not running

You can check whether the LaunchAgent is loaded with:

```bash
launchctl list | grep bearly-watching
```

If needed, check the LaunchAgent configuration:

```bash
plutil -lint ~/Library/LaunchAgents/com.bearly-watching.plist
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

### 🎬 Detection

* [x] YouTube multi-tab detection
* [x] Playing and paused states
* [x] Finished video detection
* [x] Live stream detection
* [x] Dynamic thumbnails
* [x] Playback progress

### 💬 Discord

* [x] Discord Rich Presence
* [x] Discord auto-reconnect
* [ ] Customizable Rich Presence messages
* [ ] Optional configuration UI

### 🚀 System

* [x] LaunchAgent background support
* [ ] Easier one-command installation
* [ ] Improved LaunchAgent installer

### 🧸 Future Improvements

* [ ] Better handling of multiple simultaneously playing videos
* [ ] More YouTube page compatibility

---

## 📜 License

Bearly Watching is open-source software licensed under the **MIT License**.

See [`LICENSE`](LISENCE) for details.

---

## 🧸🍓 About

Bearly Watching started as a small macOS automation project built around **Safari, YouTube, and Discord Rich Presence**.

The idea is simple:

> Make your Discord status feel a little more cute. 🧸🍓

Made with 🧸🍓 and probably too much YouTube.
