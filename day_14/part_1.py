from utils import time_it, read_input, input_path
import numpy as np
import re

W = 101
H = 103


@time_it
def main(data: str) -> str:
    # print(f"starting positions:\n{data}")
    np_pos, np_vel = ndarray_proccess_data(data)
    new_positions = calculate_positions_at_t(np_pos, np_vel)
    final_pos = wrapp_coordinates(new_positions)
    score = score_points_in_quadrants(final_pos)
    return score


def wrapp_coordinates(new_positions) -> list[np.ndarray]:
    wrapped_coordinates: list = []
    for position in new_positions:
        x = int(position[0] % W)
        y = int(position[1] % H)
        wrapped_coordinates.append((x, y))

    # print(f"final positions at t: {wrapped_coordinates}")
    return wrapped_coordinates


def score_points_in_quadrants(final_pos: list[tuple]) -> tuple[int, int, int, int]:
    center_row, center_col = H//2, W//2
    # print(f"center: {center_row, center_col}")
    q1, q2, q3, q4 = 0, 0, 0, 0
    for (x, y) in final_pos:
        if x == center_col or y == center_row:
            continue
        if x < center_col and y < center_row:
            q1 += 1
        if x > center_col and y < center_row:
            q2 += 1
        if x > center_col and y > center_row:
            q3 += 1
        if x < center_col and y > center_row:
            q4 += 1
    # print(f"quadrant scores: {q1, q2, q3, q4} ")
    return q1*q2*q3*q4


def ndarray_proccess_data(data: str) -> tuple[np.ndarray, np.ndarray]:
    lines = data.split("\n")

    positions = [(int(line.split()[0][2:].split(',')[0]),
                 int(line.split()[0][2:].split(',')[1]))
                 for line in lines]
    velocities = [(int(line.split()[1][2:].split(',')[0]),
                  int(line.split()[1][2:].split(',')[1]))
                  for line in lines]

    np_pos = np.array(positions)
    np_vel = np.array(velocities)
    # print(f"starting positions:\n{np_pos}")
    return np_pos, np_vel


def calculate_positions_at_t(np_pos, np_vel, t=100) -> list[tuple]:
    p_new = np_pos + t*np_vel
    # print(f"p_new after vector op: {p_new}")
    return p_new


if __name__ == "__main__":
    print(main(read_input(input_path(__file__).replace(".txt", "_practice.txt"))))
    print(main(read_input(input_path(__file__))))
