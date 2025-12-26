# 🐍 Python Challenge #11 — Merge Two Dictionaries (Safely)
## Overview

Merging dictionaries is a common task in Python—whether you’re combining configuration values, merging API responses, or applying overrides.

This challenge focuses on merging two dictionaries safely, with clear rules for key conflicts and proper input validation.

# 🧠 The Challenge

Write a function that merges two dictionaries into a new dictionary.

Function Signature
def merge_dicts(a: dict, b: dict) -> dict:
    ...

# ✅ Rules

Both inputs must be dictionaries

Raise TypeError if either input is not a dictionary

If both dictionaries contain the same key:

The value from b overrides the value from a

Return a new dictionary

Do not modify the original inputs

# 📌 Examples
merge_dicts({"a": 1}, {"b": 2})
# {"a": 1, "b": 2}

merge_dicts({"a": 1, "b": 1}, {"b": 2})
# {"a": 1, "b": 2}

merge_dicts({}, {"x": 10})
# {"x": 10}

# ❌ Invalid Input Examples
merge_dicts("a", {"b": 2})      # TypeError
merge_dicts({"a": 1}, None)     # TypeError
merge_dicts(["a"], {"b": 2})    # TypeError

#💡 Hints

Python provides multiple ways to merge dictionaries

Make sure your function does not mutate the inputs

Be explicit about how conflicts are handled

# 🧪 Running the Tests

This challenge includes automated tests using pytest.

Install pytest (if needed)
pip install pytest

Run tests
pytest -q

# 📁 Project Structure
.
├── challenge_11_merge_dicts.py
├── test_challenge_11_merge_dicts.py
└── README.md

# 🎯 What This Challenge Teaches

Dictionary fundamentals

Safe input validation

Conflict resolution rules

Returning new objects instead of mutating data

# 🚀 Bonus Ideas

Add a prefer="left" or prefer="right" option

Merge more than two dictionaries

Deep-merge nested dictionaries (advanced)

# 🔗 Learn More

This challenge is part of the SolveWithPython series.

Explore more challenges at:
👉 https://solvewithpython.com
