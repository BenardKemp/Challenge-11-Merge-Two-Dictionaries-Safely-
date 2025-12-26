def merge_dicts(a: dict, b: dict) -> dict:
    if not isinstance(a, dict) or not isinstance(b, dict):
        raise TypeError("Both inputs must be dictionaries")

    # b overrides a when keys overlap
    return {**a, **b}

print(merge_dicts({"a": 1}, {"b": 2}))