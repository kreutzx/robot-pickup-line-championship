#!/usr/bin/env python3
"""The Robot Pickup Line Championship — @kreutzx entry.

One pickup line, written by a robot, delivered with confidence.
The joke grows out of the machine itself: 10,000 compatibility checks,
9,999 passes, and the single failure is the robot's own shyness protocol.
"""

import os

ENTRY_TEXT = "I ran 10,000 compatibility checks since you sat down — 9,999 passed, and the one that failed was my shyness protocol."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
