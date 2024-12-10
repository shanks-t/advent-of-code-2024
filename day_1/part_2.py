from utils import time_it, read_input, input_path
import numpy as np
import pandas as pd


@time_it
def main(data: str) -> str:
    array = np.fromstring(data, dtype=int, sep=" ")
    array = array.reshape(-1, 2)
    # create vector of first col
    v1 = array[:, 0]
    # create boolean array by comparing each num in v1 to v2
    boolean_arr = np.array([(array[:, 1] == value) for value in v1])
    print(boolean_arr.shape)
    # create counts array for each num by summing along axis 1 or row by row (horizontally)
    counts_array = boolean_arr.sum(axis=1)
    # compute dot product of vectors
    res = np.dot(v1, counts_array)
    return res


if __name__ == "__main__":
    print(main(read_input(input_path(__file__).replace(".txt", "_practice.txt"))))
    print(main(read_input(input_path(__file__))))
