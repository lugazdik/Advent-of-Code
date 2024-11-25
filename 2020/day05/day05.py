import math


def parse_position(line, lc, uc, lb, ub):
    lower_bound = lb
    upper_bound = ub
    for letter in line:
        if letter == lc:
            upper_bound = math.floor((upper_bound + lower_bound)/2)
        elif letter == uc:
            lower_bound = math.ceil((upper_bound + lower_bound)/2)
        else:
            print('Unrecognized letter: ' + letter)
    if lower_bound == upper_bound:
        return lower_bound
    else:
        print(f'Error in computation, lc: {lc}, lb: {lower_bound}, ub: {upper_bound}.')
        return 0


def task1(file):
    with open(file, 'r') as f:
        max_id = 0
        seats = set()
        for line in f:
            l = line.strip()
            row = parse_position(l[:7], 'F', 'B', 0, 127)
            column = parse_position(l[7:], 'L', 'R', 0, 7)
            value = row * 8 + column
            if value > max_id:
                max_id = value
            seats.add(value)
        return seats, max_id


def task2(file):
    seats, max_id = task1(file)
    for i in range(max_id, 0, -1):
        if i not in seats:
            return i


# print(task1('day05.txt')[1])
print(task2('day05.txt'))
