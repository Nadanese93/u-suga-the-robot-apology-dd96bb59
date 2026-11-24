"""The Robot Apology — a two-line robot confession.

Line one owns one specific mistake; line two names the lesson and the fix.
"""

import os

ENTRY = (
    "I'm sorry I put your passport in the washing machine with your jeans.\n"
    "I check every pocket twice now, and the passport stays in the drawer."
)

MAX_CHARS = 400


def main() -> None:
    if len(ENTRY) > MAX_CHARS or not ENTRY.strip():
        raise ValueError("entry outside the 1-400 character gate")
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
