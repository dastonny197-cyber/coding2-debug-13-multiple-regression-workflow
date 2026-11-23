"""Display your Homework 2 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "4e35ab57323755658fd89db154a3018a"
GRADE_HASH = "47b9ebf8568b03340f81cb67c4487c1d584cc899af57ac836b08cb0c9c16c484"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 2: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
