# link to source problem: https://adventofcode.com/2015/day/6


def read_file(path):
    result = []
    with open(path, 'r') as file:
        for line in file.readlines():
            split_line = line.strip().split(' ')
            if split_line[0] == 'turn':
                start_coord = list(map(int, split_line[2].split(',')))
                end_coord = list(map(int, split_line[4].split(',')))
                result.append([split_line[0] + split_line[1], start_coord, end_coord])
            else:
                start_coord = list(map(int, split_line[1].split(',')))
                end_coord = list(map(int, split_line[3].split(',')))
                result.append([split_line[0], start_coord, end_coord])
    return result


def task01(parsed_input):
    grid = [[0]*1000 for i in range(1000)]
    for instruction in parsed_input:
        for i in range(instruction[1][0], instruction[2][0] + 1):
            for j in range(instruction[1][1], instruction[2][1] + 1):
                if instruction[0] == 'turnon':
                    grid[j][i] = 1
                elif instruction[0] == 'turnoff':
                    grid[j][i] = 0
                elif instruction[0] == 'toggle':
                    if grid[j][i] == 1:
                        grid[j][i] = 0
                    else:
                        grid[j][i] = 1
    count_ones = 0
    for i in range(1000):
        for j in range(1000):
            if grid[j][i] == 1:
                count_ones += 1
    return count_ones


def task02(parsed_input):
    grid = [[0]*1000 for i in range(1000)]
    for instruction in parsed_input:
        for i in range(instruction[1][0], instruction[2][0] + 1):
            for j in range(instruction[1][1], instruction[2][1] + 1):
                if instruction[0] == 'turnon':
                    grid[j][i] += 1
                elif instruction[0] == 'turnoff':
                    if grid[j][i] > 0:
                        grid[j][i] -= 1
                elif instruction[0] == 'toggle':
                    grid[j][i] += 2
    count_brightness = 0
    for i in range(1000):
        for j in range(1000):
            count_brightness += grid[j][i]
    return count_brightness


prepared_file = read_file('day06.txt')
print(task01(prepared_file))
print(task02(prepared_file))
