from utils import time_it, read_input, input_path
import numpy as np
from collections import deque


@time_it
def main(data: str) -> str:
    grid = preprocess_data(data)
    # print(grid)
    start_nodes = get_start_nodes(grid)
    # print(start_nodes)
    return bfs(grid, start_nodes)


def preprocess_data(data: str) -> list[list[str, str]]:
    lines = data.split("\n")
    grid = [[char for char in line] for line in lines]
    return grid


def get_valid_neighbors(curr_row, curr_col, curr_height, grid):
    valid_neighbers: list[tuple[str, str]] = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    height_positions = []
    for (x, y) in directions:
        next_row = curr_row + y
        next_col = curr_col + x
        # print(f"next cell: {next_row},{next_col}")
        if 0 <= next_row < len(grid[0]) and 0 <= next_col < len(grid[curr_row]):
            next_height = grid[next_row][next_col]
            if int(next_height) == int(curr_height) + 1:
                # print(f"next height: {
                #       next_height}\n curr height: {curr_height}")
                valid_neighbers.append((next_row, next_col))
                if int(next_height) == 9:
                    height_positions.append((next_row, next_col))
                # print(f"next cell: {(next_row, next_col)}: {next_height}")
    # if height_positions:
        # print(f"height pos: {height_positions}")
    return valid_neighbers, height_positions


def get_start_nodes(grid):
    start_nodes: list[tuple[int, int]] = []
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == "0":
                start_nodes.append((i, j))
    return start_nodes


def bfs(grid, start_nodes):
    # rows, col = len(grid), len(grid[0])
    total_score = 0
    for node in start_nodes:
        visited = set()
        node_height_positions = set()
        score = 0
        q = deque([node])
        while q:
            row, col = q.popleft()
            if (row, col) in visited:
                continue
            visited.add((row, col))
            # print(f"curr height: {grid[row][col]}")
            # print(f"node: {node}")
            valid_neighbors, height_positions = get_valid_neighbors(
                row, col, int(grid[row][col]), grid)
            node_height_positions.update(height_positions)
            q.extend(valid_neighbors)
        score += len(node_height_positions)
        total_score += score
        print(f"total_score for {node}: {score}")
        print(f"height positions for {node}: {node_height_positions}")
    return total_score


if __name__ == "__main__":
    print(main(read_input(input_path(__file__).replace(".txt", "_practice.txt"))))
    # print(main(read_input(input_path(__file__))))
