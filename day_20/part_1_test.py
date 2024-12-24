import pytest
from part_1 import Grid


def test_grid_init():
    test_input_str = "###\n#S#\n#.#\n#E#"
    grid = Grid(test_input_str)
    assert grid.start == (1, 1)
    assert grid.height == 4
    assert grid.width == 3
    assert grid.end == (3, 1)


def test_grid_ops():
    test_input_str = "###\n#S#\n#.#\n#E#"
    grid = Grid(test_input_str)
    assert grid.is_wall((0, 0))
    assert not grid.is_wall((1, 1))

    assert grid.is_valid_position((0, 0))
    assert not grid.is_valid_position((0, 6))

    neighbors = list(grid.get_neighbors((1, 1)))
    expected_neighbors = [(0, 1), (1, 0), (1, 2), (2, 1)]
    assert sorted(neighbors) == sorted(expected_neighbors)
