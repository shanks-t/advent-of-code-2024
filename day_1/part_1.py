from utils import time_it, read_input, input_path
import numpy as np


@time_it
def main(data: str) -> str:
    array = np.fromstring(data, dtype=int, sep=" ")
    array = array.reshape(-1, 2)
    array = np.sort(array, axis=0)
    element_wise_diff = abs(array[:, 0] - array[:, 1])
    res = np.sum(element_wise_diff)
    return res


if __name__ == "__main__":
    print(main(read_input(input_path(__file__).replace(".txt", "_practice.txt"))))
    print(main(read_input(input_path(__file__))))
