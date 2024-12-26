import pytest
from part_1 import regex_parse, multiply_and_sum_ints


def test_regex_parse():
    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    assert regex_parse(input) == [(2, 4), (5, 5), (11, 8), (8, 5)]


def test_mulitiply_and_sum_ints():
    input = [(2, 4), (5, 5), (11, 8), (8, 5)]
    assert multiply_and_sum_ints(input) == 161
