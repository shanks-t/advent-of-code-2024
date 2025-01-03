from utils import time_it, read_input, input_path
from collections import deque
from dataclasses import dataclass
from typing import Iterator


@dataclass
class SearchState:
    position: tuple[int, int]
    steps: int
    cheat_available: bool
    cheat_steps_remaining: int
    cheat_position: tuple[int, int] | None = None


class Grid:
    def __init__(self, raw_input: str):
        self.grid = self._get_grid_from_input(raw_input)
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.start = self._find_position("S")
        self.end = self._find_position("E")

    def __str__(self) -> str:
        # Convert the grid back to a string representation
        return '\n'.join(''.join(row) for row in self.grid)

    def _get_grid_from_input(self, data: str) -> list[list[str, str]]:
        lines = data.split("\n")
        grid = [[char for char in line] for line in lines]
        return grid

    def _find_position(self, char: str) -> tuple[int, int]:
        for x in range(self.height):
            for y in range(self.width):
                if self.grid[x][y] == char:
                    return (x, y)
        raise ValueError(f"char {char} not found in grid")

    def is_wall(self, pos: tuple[int, int]) -> bool:
        x, y = pos
        return self.grid[x][y] == "#"

    def is_valid_position(self, pos: tuple[int, int]) -> bool:
        x, y = pos
        return 0 <= x < self.width and 0 <= y < self.height

    def get_neighbors(self, position: tuple[int, int]) -> Iterator[tuple[int, int]]:
        """
        yield makes this method a generator, which is memory efficient 
        for pathfinding algorithms as it only generates valid neighbors 
        when requested, rather than creating a full list at once
        """
        x, y = position
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            new_position = (x + dx, y + dy)
            if self.is_valid_position(new_position):
                yield new_position


@time_it
def main(data: str) -> str:
    grid = Grid(data)
    cheats = find_paths_with_cheats(grid)
    return cheats


def find_baseline_path(grid: Grid) -> int:
    initial_state = SearchState(
        position=grid.start,
        steps=0,
        cheat_available=True,
        cheat_steps_remaining=0
    )
    visited = set()
    q = deque([initial_state])

    while q:
        current_state = q.popleft()

        if current_state.position == grid.end:
            return current_state.steps
        if current_state.position in visited:
            continue

        visited.add(current_state.position)

        for next_pos in grid.get_neighbors(current_state.position):
            if not grid.is_wall(next_pos):
                new_state = SearchState(
                    position=next_pos,
                    steps=current_state.steps + 1,
                    cheat_available=False,
                    cheat_steps_remaining=0
                )
                q.append(new_state)

    return float('inf')


def find_paths_with_cheats(grid: Grid) -> list[tuple[int, int]]:
    base_line_steps = find_baseline_path(grid)
    cheats = []
    visited = set()
    initial_state = SearchState(
        position=grid.start,
        steps=0,
        cheat_available=True,
        cheat_steps_remaining=0
    )

    q = deque([initial_state])

    while q:
        current_state = q.popleft()
        state_tuple = (
            current_state.position,
            current_state.cheat_available,
            current_state.cheat_steps_remaining,
            current_state.cheat_position
        )
        if state_tuple in visited:
            continue

        visited.add(state_tuple)

        if current_state.position == grid.end:
            if current_state.cheat_position:
                steps_saved = base_line_steps - current_state.steps
                if steps_saved > 0:  # Only add cheats that actually save steps
                    cheats.append((current_state.cheat_position, steps_saved))
                    continue
        for next_pos in grid.get_neighbors(current_state.position):
            if grid.is_wall(next_pos):
                if current_state.cheat_available:
                    new_state = SearchState(
                        position=next_pos,
                        steps=current_state.steps + 1,
                        cheat_available=False,
                        cheat_steps_remaining=2,
                        cheat_position=current_state.position
                    )
                    q.append(new_state)
                if current_state.cheat_steps_remaining > 0:
                    new_state = SearchState(
                        position=next_pos,
                        steps=current_state.steps + 1,
                        cheat_available=False,
                        cheat_steps_remaining=current_state.cheat_steps_remaining - 1,
                        cheat_position=current_state.cheat_position
                    )
                    q.append(new_state)
            else:
                # Handle regular moves
                new_state = SearchState(
                    position=next_pos,
                    steps=current_state.steps + 1,
                    cheat_available=current_state.cheat_available,
                    cheat_steps_remaining=current_state.cheat_steps_remaining,
                    cheat_position=current_state.cheat_position
                )
                q.append(new_state)

    return cheats


if __name__ == "__main__":
    print(main(read_input(input_path(__file__).replace(".txt", "_practice.txt"))))
    print(main(read_input(input_path(__file__))))
