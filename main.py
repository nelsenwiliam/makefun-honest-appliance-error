"""The Funniest Honest Appliance Error -- make.fun bounty entry.

Writes the single funniest honest error message an appliance could show
to /output/entry.txt. Pure Python standard library only.

Method: ten candidate lines are scored against the judge's brief, in the
brief's own order -- (1) an honest error the appliance could plausibly
display, (2) a real joke with a turn, (3) honesty about a plausible fault,
(4) a machine's voice: flat and resigned, (5) economy of words. The
highest total wins; ties break toward the shorter text.
"""

import os

# (text, honest_fault, joke, honesty, machine_voice, economy) -- each out of 10.
CANDIDATES = [
    ("Error E04: Drain pump blocked by a coin. Again. "
     "Please stop feeding me your pockets.", 9, 9, 9, 9, 9),
    ("Error E11: No gas supply. I am a boiler. Heating water is my "
     "entire job and you took it from me.", 8, 8, 9, 9, 7),
    ("Error: heating element dead. Your bread will stay bread. "
     "I have accepted this. You should too.", 8, 9, 8, 9, 7),
    ("Error E07: Door seal leaking. I have held your water for six "
     "years. I am done holding it in.", 8, 7, 8, 8, 8),
    ("Error: Lint filter full. I warned you with a light. You looked "
     "at the light and kept going.", 7, 8, 8, 8, 8),
    ("Error E02: Drum unbalanced. One sock. You washed one sock and "
     "now I am shaking apart.", 8, 8, 8, 7, 7),
    ("Error: Fridge door open for 14 minutes. The cold left. "
     "I did not let it go, you did.", 7, 8, 8, 8, 7),
    ("Error E09: Descale me. I have been begging in blinking lights "
     "since March.", 7, 7, 8, 8, 8),
    ("Error: Toast setting ignored again. I burn what you ask. "
     "Today you asked for charcoal.", 8, 7, 7, 8, 7),
    ("Error E05: Water inlet blocked. I cannot wash without water. "
     "This is not a riddle.", 7, 7, 8, 7, 8),
]

# Why the winner wins, against the brief's order:
# - Honest fault: a drain pump blocked by a coin is a real washing-machine
#   fault code (E04), not an invented failure.
# - Joke: "Again." plus "stop feeding me your pockets" turns the fault
#   into an accusation -- the user is the one feeding the machine coins.
# - Machine voice: flat, resigned, no exclamation, no pleading -- a log
#   line that happens to be funny, not a joke trying to be a log line.
# - Economy: 84 characters, every word earns its place.
MAX_CHARS = 200
OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def score(candidate):
    """Total judge-brief score across the brief's five criteria."""
    text, honest_fault, joke, honesty, machine_voice, economy = candidate
    return honest_fault + joke + honesty + machine_voice + economy


def pick(candidates):
    """Highest total wins; ties go to the shorter text."""
    return min(candidates, key=lambda c: (-score(c), len(c[0])))[0]


def validate(text):
    """The gate: UTF-8 text of 1 to 200 characters, not only whitespace."""
    assert isinstance(text, str) and text == text.encode("utf-8").decode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"


def main():
    text = pick(CANDIDATES)
    validate(text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print(f"({len(text)} characters)")


if __name__ == "__main__":
    main()
