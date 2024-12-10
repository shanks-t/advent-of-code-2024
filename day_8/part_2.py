from utils import time_it, read_input, input_path
import numpy as np
from itertools import combinations


@time_it
def main(data: str) -> str:
    coordinates_dict, all_possible_points, bounding_box = preprocess_data(data)
    solution = find_intersection_of_coordinate_plane_and_antidodes(
        coordinates_dict, all_possible_points, bounding_box)
    return solution


def preprocess_data(data: str) -> tuple[dict[str, list[tuple[int, int]]], list[np.ndarray], tuple[int, int, int, int]]:
    coordinates_dict = create_coordinates_dict(data)
    all_possible_points = find_all_possible_points(coordinates_dict)
    bounding_box = find_bounding_box_of_points(all_possible_points)
    # print(bounding_box)
    return coordinates_dict, all_possible_points, bounding_box


def find_bounding_box_of_points(all_possible_points: list[np.ndarray]) -> tuple[int, int, int, int]:
    x_min, y_min, x_max, y_max = 10**5, 10**5, 0, 0
    for x, y in all_possible_points:
        x_min = int(min(x_min, x))
        y_min = int(min(y_min, y))
        x_max = int(max(x_max, x))
        y_max = int(max(y_max, y))

    return (x_min, y_min, x_max, y_max)


def find_intersection_of_coordinate_plane_and_antidodes(coordinates_dict: dict, all_possible_points: list, bounding_box: tuple) -> int:
    intersection: list[list] = []

    # conver point to tuple for comparison with set
    all_antinodes_set = create_antinodes_set(
        coordinates_dict, bounding_box)
    intersection = [point
                    for point in all_possible_points if tuple(point) in all_antinodes_set]

    # print(f"total intersection: {intersection}")
    return len(intersection)


def create_antinodes_set(coordinates_dict: dict, bounding_box: tuple) -> set:
    all_antinodes_set = set()

    for key, sattelite_points in coordinates_dict.items():
        if key not in ['.', '#']:
            # print(f"points of dict {key}: {points}")
            combos = find_all_unique_combination_of_sattelite_points(
                sattelite_points)
            # print(f'combos: {combos}')
            lines_list = compute_line_from_points(combos)
            antinodes_list = find_all_antinode_points_in_bounding_box(
                lines_list, bounding_box)
            # print(antinodes_list)
            # map ndarrays to hashable tuples
            all_antinodes_set.update(map(tuple, antinodes_list))
    return all_antinodes_set


def find_all_antinode_points_in_bounding_box(lines_list: list[tuple[int, int]], b_box: tuple[int, int, int, int]) -> list[tuple[int, int]]:
    points: list[tuple[int, int]] = []
    (x1, y1, x2, y2) = b_box
    for line in lines_list:
        slope = line[0]
        intercept = line[1]
        for x in range(x1, x2 + 1):
            y = slope * x + intercept
            if y1 <= y <= y2 and y.is_integer():
                points.append((x, y))
    # print(f"all antinode points in bouding box: {points}")
    return points


def find_all_unique_combination_of_sattelite_points(satellite_points: list[tuple]) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    return list(combinations(satellite_points, 2))


def find_all_possible_points(coordinates_dict: dict) -> list[np.ndarray]:
    all_possible_points: list[np.ndarray] = []
    for _, points in coordinates_dict.items():
        # print(points)
        all_possible_points.extend(np.array(points))
    return all_possible_points


def compute_line_from_points(combos: list[tuple]) -> list[tuple[float, float]]:
    lines_list: list[tuple[float, float]] = []
    for combo in combos:
        x1, y1 = np.array(combo[0])
        x2, y2 = np.array(combo[1])
        m = (y2 - y1)/(x2-x1)
        b = y1 - m*x1
        lines_list.append((m, b))
    return lines_list


def create_coordinates_dict(data: str) -> dict[str, list[tuple[int, int]]]:
    coordinates_dict = {}
    grid = data.split("\n")
    for y, row in enumerate(reversed(grid)):
        for x, char in enumerate(row):
            coordinates_dict.setdefault(char, []).append((x, y))

    # print(coordinates_dict)
    return coordinates_dict


if __name__ == "__main__":
    print(main(read_input(input_path(__file__).replace(".txt", "_practice.txt"))))
    print(main(read_input(input_path(__file__))))
