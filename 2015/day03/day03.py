# link to source problem: https://adventofcode.com/2015/day/3

def read_file(path):
    with open(path, 'r') as file:
        return file.read()


def task01(parsed_input):
    x_pos = 0
    y_pos = 0
    visited = set()
    visited.add((0, 0))
    for item in parsed_input:
        if item == '^':
            y_pos += 1
        elif item == 'v':
            y_pos -= 1
        elif item == '<':
            x_pos -= 1
        elif item == '>':
            x_pos += 1
        visited.add((x_pos, y_pos))
    return len(visited)


def move_coordinates(prev_coords, symbol):
    if symbol == '^':
        return prev_coords[0], prev_coords[1] + 1
    elif symbol == 'v':
        return prev_coords[0], prev_coords[1] - 1
    elif symbol == '<':
        return prev_coords[0] - 1, prev_coords[1]
    elif symbol == '>':
        return prev_coords[0] + 1, prev_coords[1]


def task02(parsed_input):
    last_santa = (0, 0)
    last_robot = (0, 0)
    step = 0
    visited = set()
    visited.add((0, 0))
    for item in parsed_input:
        step += 1
        if step % 2 == 0:
            last_robot = move_coordinates(last_robot, item)
            visited.add(last_robot)
        else:
            last_santa = move_coordinates(last_santa, item)
            visited.add(last_santa)
    return len(visited)


prepared_file = read_file('day03.txt')
print(task01(prepared_file))
print(task02(prepared_file))
