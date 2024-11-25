# link to source problem: https://adventofcode.com/2015/day/2


def read_file(path):
    result = []
    with open(path, 'r') as file:
        for line in file.readlines():
            result.append(list(map(int, line.split('x'))))
    return result


def task01(parsed_input):
    result = 0
    for entry in parsed_input:
        entry = sorted(entry)
        result += entry[0] * entry[1]
        result += ((2 * entry[0] * entry[1]) + (2 * entry[0] * entry[2]) + (2 * entry[1] * entry[2]))
    return result


def task02(parsed_input):
    result = 0
    for entry in parsed_input:
        entry = sorted(entry)
        result += 2*(entry[0] + entry[1])
        result += entry[0] * entry[1] * entry[2]
    return result


prepared_file = read_file('day02.txt')
print(task01(prepared_file))
print(task02(prepared_file))
