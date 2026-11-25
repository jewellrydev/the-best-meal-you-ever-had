"""The Best Meal You Ever Had — a make.fun entry.

Prints exactly one sentence, at most 200 characters, about the best
meal I ever had.
"""

LINE = (
    "My grandmother's rendang, eaten barefoot on her porch while "
    "the rain argued with the tin roof and lost to coconut, smoke "
    "and patience."
)


def build_line() -> str:
    line = LINE
    assert len(line) <= 200, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
