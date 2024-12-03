import re


def read_input(input_path: str):
    with open(input_path, "r") as f:
        return f.read().strip()


def part1(input_string: str):
    matches = re.findall(r"mul(\(\d+,\d+\))", input_string)
    result = 0
    for match in matches:
        numbers = list(map(int, str(match).strip("()").split(",")))
        result += numbers[0] * numbers[1]
    return result


def part2(input_string: str):
    matches = re.findall(r"(do\(\))|(don't\(\))|(mul\(\d+,\d+\))", input_string)
    result = 0
    do = True
    for match in matches:
        if match[0]:
            do = True
        elif match[1]:
            do = False
        elif match[2]:
            if do:
                numbers = list(
                    map(int, str(match[2]).strip("mul").strip("()").split(","))
                )
                result += numbers[0] * numbers[1]
    return result


input_line = read_input("day03.txt")
print(part1(input_line))
print(part2(input_line))
