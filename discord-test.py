import time
from pypresence import Presence

from config import CLIENT_ID


def main():
    print("╭──────────────────────────────╮")
    print("│  🧸 Bearly Watching          │")
    print("╰──────────────────────────────╯")
    print()

    print("Connecting to Discord...")

    rpc = Presence(CLIENT_ID)
    rpc.connect()

    print("Connected!")
    print("Rich Presence is active!")
    print()

    rpc.update(
        details="Watching YouTube",
        state="via Safari 💻",
        large_image="youtube",
        large_text="Bearly Watching 🧸🍓",
    )

    while True:
        time.sleep(15)


if __name__ == "__main__":
    main()
