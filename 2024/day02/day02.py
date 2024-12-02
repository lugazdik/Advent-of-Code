def read_input(input_path: str):
    with open(input_path, "r") as f:
        return [list(map(int, line.strip().split())) for line in f.readlines()]


def validate_line(line: list[int]):
    increasing = True
    decreasing = True
    for i in range(0, len(line) - 1):
        if (diff := abs(line[i] - line[i + 1])) > 3 or diff == 0 or ():
            return False
        if line[i] > line[i + 1]:
            decreasing = False
        elif line[i] < line[i + 1]:
            increasing = False
        if (not increasing) and (not decreasing):
            return False
    return True


def part1(data: list[list[int]]):
    return sum([1 if validate_line(line) else 0 for line in data])


def part2(data: list[list[int]]):
    result = 0
    for line in data:
        for i in range(0, len(line)):
            if validate_line(line[:i] + line[i + 1 :]):
                result += 1
                break
    return result


input_numbers = read_input("day02.txt")
print(part1(input_numbers))
print(part2(input_numbers))
