import pytest
from part_2 import split_on_instructions


def test_split_on_instructions():
    input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    assert split_on_instructions(
        input) == ["xmul(2,4)&mul[3,7]!^", "?mul(8,5))"]
