from collections import defaultdict
from functools import cache, cmp_to_key

ORDERING_RULES = defaultdict(set)


def read_input(input_path: str):
    ordered_lines = []
    with open(input_path, "r") as f:
        first_part, second_part = f.read().split("\n\n")
        for rule in first_part.split("\n"):
            key, value = rule.split("|")
            ORDERING_RULES[key].add(value)
        for line in second_part.split("\n"):
            ordered_lines.append(line.split(","))
    return ordered_lines


lines = read_input("day05.txt")


@cache
def check_ordering(first: str, second: str):
    if second not in ORDERING_RULES:
        return 0
    if first in ORDERING_RULES[second]:
        return 1
    return -1


def both_parts(lines: list[list[str]], fix_ordering: bool = False):
    result = 0
    for line in lines:
        copied_line = sorted(line, key=cmp_to_key(check_ordering))
        if fix_ordering:
            if copied_line != line:
                result += int(copied_line[len(line) // 2])
        else:
            if copied_line == line:
                result += int(copied_line[len(line) // 2])
    return result


print(both_parts(lines, False))
print(both_parts(lines, True))
