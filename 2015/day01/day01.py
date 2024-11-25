# link to source problem: https://adventofcode.com/2015/day/1


def read_file(path):
    with open(path, 'r') as file:
        return file.read()


def task01(parsed_input):
    return parsed_input.count('(') - parsed_input.count(')')


def task02(parsed_input):
    value = 0
    position = 0
    while value != -1:
        if parsed_input[position] == '(':
            value += 1
        else:
            value -= 1
        position += 1
    return position


prepared_file = read_file('day01.txt')
print(task01(prepared_file))
print(task02(prepared_file))
