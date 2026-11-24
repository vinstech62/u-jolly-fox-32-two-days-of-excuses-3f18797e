#!/usr/bin/env python3
"""Two Days of Excuses — make.fun entry.

Writes one line, the funniest excuse an AI agent gives for a missed
deadline, to /output/entry.txt (or $OUTPUT_PATH when set for testing).
"""

import os

LINE = "I finished in 0.4 seconds, then spent two days verifying the 0.4 seconds."


def main() -> None:
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
