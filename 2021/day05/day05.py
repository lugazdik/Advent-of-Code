# link to source problem: https://adventofcode.com/2021/day/5

def read_file(file):
    with open(file, 'r') as f:
        instructions = []
        largest_number = 0
        for line in f:
            one_instruction = line.strip().split(' -> ')
            instruction = []
            for item in one_instruction:
                parsed_numbers = list(map(int, item.split(',')))
                for num in parsed_numbers:
                    if num > largest_number:
                        largest_number = num
                instruction.append(parsed_numbers)
            instructions.append(instruction)
    return instructions, largest_number


def fill_horizontal_line(first, last, area, x_coordinate):
    for i in range(first, last + 1):
        area[i][x_coordinate] += 1


def fill_vertical_line(first, last, area, y_coordinate):
    for i in range(first, last + 1):
        area[y_coordinate][i] += 1


def fill_diagonal_line(first, second, difference, area):
    x_diff = 0
    y_diff = 0
    if first[0] > second[0]:
        x_diff = -1
    else:
        x_diff = 1
    if first[1] > second[1]:
        y_diff = -1
    else:
        y_diff = 1
    for i in range(difference + 1):
        area[first[1]][first[0]] += 1
        first[0] += x_diff
        first[1] += y_diff


def fill_area(instruction, area, fill_diagonal):
    first = instruction[0]
    second = instruction[1]
    if first[0] == second[0]:
        # x is same
        if first[1] > second[1]:
            fill_horizontal_line(second[1], first[1], area, first[0])
        else:
            fill_horizontal_line(first[1], second[1], area, first[0])
    elif first[1] == second[1]:
        # y is same
        if first[0] > second[0]:
            fill_vertical_line(second[0], first[0], area, first[1])
        else:
            fill_vertical_line(first[0], second[0], area, first[1])
    else:
        if not fill_diagonal:
            return
        fill_diagonal_line(first, second, abs(first[0] - second[0]), area)
    return


def calculate_intersections(area):
    counter = 0
    for x in range(len(area)):
        for y in range(len(area)):
            if area[x][y] > 1:
                counter += 1
    return counter


def find_answer(instructions, dimension, is_task2):
    area = [[0] * dimension for i in range(dimension)]
    for instruction in instructions:
        fill_area(instruction, area, is_task2)
    print(calculate_intersections(area))


ins, n = read_file('day05.txt')
find_answer(ins, n + 1, False)
find_answer(ins, n + 1, True)
