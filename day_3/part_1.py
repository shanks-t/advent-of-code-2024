from utils import time_it, read_input, input_path
import re


@time_it
def main(data: str) -> str:
    regex_parse(data)
    return "fin"


def regex_parse(data: str) -> list[tuple[int, int]]:
    regex = r'mul\((\d{1,3}),(\d{1,3})\)'

    return [(int(x), int(y)) for x, y in re.findall(regex, data)]


if __name__ == "__main__":
    print(main(read_input(input_path(__file__).replace(".txt", "_practice.txt"))))
    # print(main(read_input(input_path(__file__))))
