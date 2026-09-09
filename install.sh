#!/bin/bash

set -e

APP_NAME="Bearly Watching"
PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_DIR="$PROJECT_DIR/.venv"
PYTHON="$VENV_DIR/bin/python"

LABEL="com.bearly-watching"
LAUNCH_AGENTS_DIR="$HOME/Library/LaunchAgents"
PLIST_PATH="$LAUNCH_AGENTS_DIR/$LABEL.plist"

echo ""
echo "╭──────────────────────────────────╮"
echo "│         Bearly Watching          │"
echo "│         Safari → Discord         │"
echo "╰──────────────────────────────────╯"
echo ""

# Check macOS
if [[ "$(uname)" != "Darwin" ]]; then
    echo "This application requires macOS."
    exit 1
fi

# Check Python
echo "Checking Python..."

if ! command -v python3 >/dev/null 2>&1; then
    echo "Python 3 is not installed."
    echo "Please install Python 3 and try again."
    exit 1
fi

PYTHON3="$(command -v python3)"

echo "Python found: $PYTHON3"
echo ""

# Create virtual environment
if [[ ! -d "$VENV_DIR" ]]; then
    echo "Creating virtual environment..."
    "$PYTHON3" -m venv "$VENV_DIR"
else
    echo "Virtual environment already exists."
fi

echo ""

# Install dependencies
echo "Installing dependencies..."
"$PYTHON" -m pip install --upgrade pip
"$PYTHON" -m pip install -r "$PROJECT_DIR/requirements.txt"

echo ""

# Create logs directory
mkdir -p "$PROJECT_DIR/logs"

echo "Setting up LaunchAgent..."

mkdir -p "$LAUNCH_AGENTS_DIR"

# Stop existing LaunchAgent if running
launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true

# Create LaunchAgent
cat > "$PLIST_PATH" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
    "http://www.apple.com/DTDs/PropertyList-1.0.dtd">

<plist version="1.0">
<dict>

    <key>Label</key>
    <string>$LABEL</string>

    <key>ProgramArguments</key>
    <array>
        <string>$PYTHON</string>
        <string>$PROJECT_DIR/main.py</string>
    </array>

    <key>WorkingDirectory</key>
    <string>$PROJECT_DIR</string>

    <key>RunAtLoad</key>
    <true/>

    <key>KeepAlive</key>
    <true/>

    <key>StandardOutPath</key>
    <string>$PROJECT_DIR/logs/bearly-watching.log</string>

    <key>StandardErrorPath</key>
    <string>$PROJECT_DIR/logs/bearly-watching-error.log</string>

</dict>
</plist>
EOF

# Validate plist
plutil -lint "$PLIST_PATH" >/dev/null

# Load LaunchAgent
launchctl bootstrap "gui/$(id -u)" "$PLIST_PATH"

echo ""
echo "✨ Installation complete!"
echo ""
echo "Bearly Watching is now running in the background."
echo ""
echo "🍓 Enjoy Bearly Watching!"
echo ""
