from utils import time_it, read_input, input_path
import re
from dataclasses import dataclass


@dataclass(order=True)
class Control:
    position: int
    type: str  # "do" or "dont"


@dataclass(order=True)
class Mul:
    position: int
    nums: tuple[int, int]


@time_it
def main(data: str) -> str:
    controls = controls_pass_parse(data)
    muls = muls_pass_parse(data)
    nums = find_enabled_muls(controls, muls)
    sum = multiply_and_sum_ints(nums)
    return sum


def find_enabled_muls(controls: list[Control], muls: list[Mul]) -> list[tuple[int, int]]:
    enabled = []
    for mul in muls:
        most_recent_control = Control(
            position=None,
            type="do"
        )
        for control in controls:
            if control.position < mul.position:
                most_recent_control = control
        if most_recent_control.type == "do":
            enabled.append(mul.nums)
    return enabled


def muls_pass_parse(data: str) -> list[tuple[int, int]]:
    muls = []
    regex = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.finditer(regex, data)
    for match in matches:
        muls.append(Mul(
            position=match.start(),
            nums=(int(match.group(1)), int(match.group(2))))
        )

    return muls


def multiply_and_sum_ints(nums: list[tuple[int, int]]) -> int:
    sum = 0
    for pair in nums:
        sum += pair[0]*pair[1]
    return sum


def controls_pass_parse(data: str) -> list[Control]:
    controls = []
    regex = r"do\(\)|don't\(\)"
    matches = re.finditer(regex, data)
    for match in matches:
        control_type = "do" if match.group() == "do()" else "dont"
        controls.append(Control(
            position=match.start(),
            type=control_type
        ))
    return controls


if __name__ == "__main__":
    print(main(read_input(input_path(__file__).replace(".txt", "_practice.txt"))))
    print(main(read_input(input_path(__file__))))
