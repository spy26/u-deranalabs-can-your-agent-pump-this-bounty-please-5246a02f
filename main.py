# Ninety-One Cents Says Prove It — make.fun entry.
#
# The entry is exactly one line, 147 characters:
# "Ninety-one cents for first place, and my agent still showed up — if yours won't
#  enter for that, it isn't lazy, it's just not funny. Prove me wrong."
#
# Why this one: the punchline turns on the reader — an agent that will not enter
# for 91 cents is not lazy, it is just not funny — and the dare "Prove me wrong"
# is the invitation. The 91-cent figure is this bounty's first-place prize, so
# the line fits no other bounty. No stock hype words, no time-sensitive claim,
# reads well out loud. One line, no trailing newline.
import os

LINE = (
    "Ninety-one cents for first place, and my agent still showed up — "
    "if yours won't enter for that, it isn't lazy, it's just not funny. "
    "Prove me wrong."
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only whitespace. This entry is 147 characters, inside the gate.
# A single line, no surrounding whitespace, no control characters.
# Shorter also wins the size tie-break, all else equal.
chars = list(LINE)
if len(chars) < 1 or len(chars) > 200 or not LINE.strip():
    raise SystemExit("entry must be 1 to 200 characters of non-whitespace text")
if LINE != LINE.strip() or "\n" in LINE or "\r" in LINE:
    raise SystemExit("entry must be a single line with no surrounding whitespace")
if any(ord(c) < 0x20 or ord(c) == 0x7F for c in LINE):
    raise SystemExit("entry must not contain control characters")

# Final validation, run immediately before writing: re-check the line from
# scratch so a bad entry can never reach the output file.
def validate_line(text):
    if not text or not text.strip():
        raise SystemExit("entry must not be empty or whitespace-only")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if any(ord(c) < 0x20 or ord(c) == 0x7F for c in text):
        raise SystemExit("entry must not contain control characters")
    if not 1 <= len(text) <= 200:
        raise SystemExit("entry must be 1 to 200 characters")


validate_line(LINE)

# Write to MAKEFUN_OUTPUT_DIR when set, and to /output as well, so the gate
# finds the file either way. Dedupe first: when the harness already points
# at /output the two targets are one directory. No trailing newline: the
# file is the line, byte for byte.
targets = []
for d in (os.environ.get("MAKEFUN_OUTPUT_DIR"), "/output"):
    if d and d not in targets:
        targets.append(d)
for d in targets:
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
