from collections import Counter


def read_input(input_path: str):
    first_list = []
    second_list = []
    with open(input_path, "r") as f:
        for line in f.readlines():
            split_line = line.strip().split()
            first_list.append(int(split_line[0]))
            second_list.append(int(split_line[1]))
    return first_list, second_list


def part1(first_list: list[int], second_list: list[int]):
    return sum([abs(x - y) for x, y in zip(sorted(first_list), sorted(second_list))])


def part2(first_list: list[int], second_list: list[int]):
    counter = Counter(second_list)
    result = 0
    for x in first_list:
        result += counter[x] * x
    return result


first_list, second_list = read_input("day01.txt")
print(part1(first_list, second_list))
print(part2(first_list, second_list))
