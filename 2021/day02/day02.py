# link to source problem: https://adventofcode.com/2021/day/2

def read_file(path):
    result = []
    with open(path, 'r') as file:
        for line in file.readlines():
            split_line = line.split(' ')
            result.append([split_line[0], int(split_line[1])])
    return result


def task01(parsed_input):
    horizontal_pos = 0
    depth = 0
    for instruction in parsed_input:
        if instruction[0] == 'forward':
            horizontal_pos += instruction[1]
        elif instruction[0] == 'down':
            depth += instruction[1]
        elif instruction[0] == 'up':
            depth -= instruction[1]
    return horizontal_pos, depth, horizontal_pos * depth


def task02(parsed_input):
    horizontal_pos = 0
    depth = 0
    aim = 0
    for instruction in parsed_input:
        if instruction[0] == 'forward':
            horizontal_pos += instruction[1]
            depth += aim * instruction[1]
        elif instruction[0] == 'down':
            aim += instruction[1]
        elif instruction[0] == 'up':
            aim -= instruction[1]
    return horizontal_pos, depth, aim, horizontal_pos * depth


prepared_file = read_file('day02.txt')
print(task01(prepared_file))
print(task02(prepared_file))
