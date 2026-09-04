import re

_PATTERN = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")


def is_valid(version: str) -> bool:
    """Check a simple semantic version without prerelease metadata."""
    return bool(_PATTERN.fullmatch(version.strip()))


def next_version(version: str, part: str = "patch") -> str:
    """Increment major, minor, or patch for a semantic version."""
    match = _PATTERN.fullmatch(version.strip())
    if not match or part not in {"major", "minor", "patch"}:
        raise ValueError("expected X.Y.Z and part major, minor, or patch")
    values = [int(value) for value in match.groups()]
    index = {"major": 0, "minor": 1, "patch": 2}[part]
    values[index] += 1
    for position in range(index + 1, 3):
        values[position] = 0
    return ".".join(map(str, values))
