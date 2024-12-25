from utils import time_it, read_input, input_path


@time_it
def main(data: str) -> str:
    list = get_list_from_input(data)
    num_safe_reports = count_safe_reports(list)
    return num_safe_reports


def get_list_from_input(data: str) -> list[list[int]]:
    return [list(map(int, line.split())) for line in data.split('\n')]


def count_safe_reports(list: list[list[int]]) -> int:
    safe_reports = 0
    for report in list:
        safe_reports += is_safe_report(report)
    return safe_reports


def is_safe_report(report: list[int]) -> bool:
    '''
   The generator expression (x < y for x, y in zip(sequence, sequence[1:])) 
   creates pairs of consecutive elements from the sequence and checks 
   if each pair is in increasing order (x < y) 
   zip() takes two or more iterables and returns iterator of  tuples
   all() returns True if all elems in iterable are true
    '''
    is_ascending = all(x < y for x, y in zip(report, report[1:]))
    is_descending = all(x > y for x, y in zip(report, report[1:]))
    is_valid_diff = all(abs(x - y) < 4 for x, y in zip(report, report[1:]))
    return (is_ascending or is_descending) and is_valid_diff


if __name__ == "__main__":
    print(main(read_input(input_path(__file__).replace(".txt", "_practice.txt"))))
    print(main(read_input(input_path(__file__))))
