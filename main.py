"""Quiet Dread entrypoint.

Builds one short pull-request approval line and stores it in
/output/entry.txt. The line is deliberately plain on the surface:
it signs off on the change, counts how many approvals came before
it, and admits that none of them actually stuck in memory.

The file must contain exactly that line -- no trailing newline --
so the output stays a single line within the allowed length.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.txt"

# The approval is split into its three natural beats so each part
# can be read on its own: the verdict, the tally, and the aside.
VERDICT = "Looks good."
TALLY = "I have approved 400 PRs this year and remember none of them,"
ASIDE = "including, soon, this one."


def compose_line() -> str:
    """Join the named parts into the final one-line approval."""
    parts = [VERDICT, TALLY, ASIDE]
    return " ".join(part.strip() for part in parts if part.strip())


def write_entry() -> None:
    """Write the composed line to the output file, exactly as-is."""
    line = compose_line()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    target = os.path.join(OUTPUT_DIR, OUTPUT_NAME)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


if __name__ == "__main__":
    write_entry()
