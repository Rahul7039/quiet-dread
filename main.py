"""Quiet Dread: write the chosen one-line code review comment to /output/entry.txt.

The entry is a single line (99 characters) that approves a pull request while
carrying quiet existential dread. It is written exactly, with no trailing
newline, so the file holds one line of 1-140 characters.
"""

import os

ENTRY = "Looks good. I have approved 400 PRs this year and remember none of them, including, soon, this one."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
