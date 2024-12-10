from utils import time_it, read_input, input_path
import numpy as np
from itertools import combinations


@time_it
def main(data: str) -> str:
    coordinates_dict, all_possible_points = preprocess_data(data)
    solution = find_intersection_of_coordinate_plane_and_antidodes(
        coordinates_dict, all_possible_points)
    return solution


def preprocess_data(data: str) -> tuple[dict[str, list[tuple[int, int]]], list[np.ndarray]]:
    coordinates_dict = create_coordinates_dict(data)
    all_possible_points = find_all_possible_points(coordinates_dict)
    return coordinates_dict, all_possible_points


def find_intersection_of_coordinate_plane_and_antidodes(coordinates_dict: dict, all_possible_points: list) -> int:
    intersection: list[list] = []

    # conver point to tuple for comparison with set
    all_antinodes_set = create_antinodes_set(
        coordinates_dict)
    intersection = [point
                    for point in all_possible_points if tuple(point) in all_antinodes_set]

    # print(f"total intersection: {intersection}")
    return len(intersection)


def create_antinodes_set(coordinates_dict: dict) -> set:
    all_antinodes_set = set()

    for key, sattelite_points in coordinates_dict.items():
        if key not in ['.', '#']:
            # print(f"points of dict {key}: {points}")
            combos = find_all_unique_combination_of_sattelite_points(
                sattelite_points)
            # print(f'combos: {combos}')
            antinodes_list = compute_points_of_extended_vector(combos)
            # map ndarrays to hashable tuples
            all_antinodes_set.update(map(tuple, antinodes_list))
    return all_antinodes_set


def find_all_unique_combination_of_sattelite_points(satellite_points: list[tuple]) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    return list(combinations(satellite_points, 2))


def find_all_possible_points(coordinates_dict: dict) -> list[np.ndarray]:
    all_possible_points: list[np.ndarray] = []
    for _, points in coordinates_dict.items():
        # print(points)
        all_possible_points.extend(np.array(points))
    return all_possible_points


def compute_points_of_extended_vector(combos: list[tuple]) -> list[np.ndarray]:
    antinodes_list: list[np.ndarray] = []
    for combo in combos:
        point1 = np.array(combo[0])
        point2 = np.array(combo[1])
        vector = point2 - point1
        # print(f"vector: {vector}")

        # calculate antinodes by extending line
        new_point1 = point1 - vector
        new_point2 = point2 + vector

        antinodes_list.extend([new_point1, new_point2])

        # print("Original Points:")
        # print("Point 1:", point1)
        # print("Point 2:", point2)

        # print("\nExtended Points:")
        # print("New Point 1:", new_point1)
        # print("New Point 2:", new_point2, "\n\n")
    return antinodes_list

# def compute_points_of_extended_vector(combos: list[tuple]) -> list[np.ndarray]:

#     # create 3d array of shape n, 2, 2
#     points = np.array([np.array(combo) for combo in combos])
#     # print(points.shape)
#     # print(points)
#     # print(f"first pair of points in 3d array: {points[0]}\n")
#     # print(f"first point in first pair: {points[0][0]}")
#     # print(f"second point in first pair: {points[0][1]}\n")
#     # extract x, y from all n 2,2 arrays
#     point1 = points[:, 0, :]
#     # print(f"point1: {point1}")
#     point2 = points[:, 1, :]
#     vectors = point1 - point2
#     # calculate antinodes by extenind points in both dirs by line segment(vector)
#     new_point1 = point1 - vectors
#     new_point2 = point2 + vectors

#     antinodes_list = np.array([new_point1, new_point2]).transpose(1, 0, 2)
#     return antinodes_list.reshape(-1, 2)


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
