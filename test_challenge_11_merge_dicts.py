import pytest

from Merge_Two_Dictionaries import merge_dicts


def test_merge_dicts_merges_non_overlapping_keys():
    a = {"a": 1}
    b = {"b": 2}
    assert merge_dicts(a, b) == {"a": 1, "b": 2}


def test_merge_dicts_b_overrides_a_on_conflict():
    a = {"a": 1, "x": 100}
    b = {"x": 200, "b": 2}
    assert merge_dicts(a, b) == {"a": 1, "x": 200, "b": 2}


def test_merge_dicts_handles_empty_dicts():
    assert merge_dicts({}, {}) == {}
    assert merge_dicts({"a": 1}, {}) == {"a": 1}
    assert merge_dicts({}, {"b": 2}) == {"b": 2}


def test_merge_dicts_returns_new_dict_and_does_not_mutate_inputs():
    a = {"a": 1, "x": 100}
    b = {"x": 200, "b": 2}

    a_copy = a.copy()
    b_copy = b.copy()

    result = merge_dicts(a, b)

    assert result == {"a": 1, "x": 200, "b": 2}
    assert result is not a
    assert result is not b
    assert a == a_copy
    assert b == b_copy


@pytest.mark.parametrize(
    "a, b",
    [
        ("not a dict", {"b": 2}),
        ({"a": 1}, "not a dict"),
        (None, {"b": 2}),
        ({"a": 1}, None),
        ([], {"b": 2}),
        ({"a": 1}, []),
        (123, {"b": 2}),
        ({"a": 1}, 456),
        (True, {"b": 2}),
        ({"a": 1}, False),
    ],
)
def test_merge_dicts_rejects_non_dict_inputs(a, b):
    with pytest.raises(TypeError):
        merge_dicts(a, b)
