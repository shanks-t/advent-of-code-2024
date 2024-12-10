from utils import time_it, read_input, input_path
import numpy as np


@time_it
def main(data: str) -> str:
    array = np.fromstring(data, dtype=int, sep="\n")
    array = np.reshape(array, (len(array), -1))
    print(array)
    return "fin"


if __name__ == "__main__":
    print(main(read_input(input_path(__file__).replace(".txt", "_practice.txt"))))
    # print(main(read_input(input_path(__file__))))
