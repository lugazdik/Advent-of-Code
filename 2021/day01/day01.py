# link to source problem: https://adventofcode.com/2021/day/1


def read_file(path):
    with open(path, 'r') as file:
        return list(map(int, file.readlines()))


def task01(parsed_input):
    count = 0
    for i in range(1, len(parsed_input)):
        if parsed_input[i] > parsed_input[i - 1]:
            count += 1
    return count


def task02(parsed_input, window_size):
    count = 0
    for i in range(0, len(parsed_input) - window_size):
        if sum(parsed_input[i:i + window_size]) < sum(parsed_input[i + 1:i + 1 + window_size]):
            count += 1
    return count


prepared_file = read_file('day01.txt')
print(task01(prepared_file))
print(task02(prepared_file, 3))
