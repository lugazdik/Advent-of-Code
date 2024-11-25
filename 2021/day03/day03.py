# link to source problem: https://adventofcode.com/2021/day/3

def read_file(path):
    result = []
    with open(path, 'r') as file:
        for line in file:
            result.append(line.strip())
    return result


def find_positions(input_numbers):
    item_length = len(input_numbers[0])
    result = [0] * item_length
    for item in input_numbers:
        for x in range(item_length):
            if item[x] == '1':
                result[x] += 1
            elif item[x] == '0':
                result[x] -= 1
    return result


def filter_matches(input_numbers, position, is_oxygen):
    result = find_positions(input_numbers)
    matches = []
    for item in input_numbers:
        if is_oxygen:
            if result[position] >= 0 and item[position] == '1':
                matches.append(item)
            elif result[position] < 0 and item[position] == '0':
                matches.append(item)
        else:
            if result[position] >= 0 and item[position] == '0':
                matches.append(item)
            elif result[position] < 0 and item[position] == '1':
                matches.append(item)
    return matches


def task01(input_numbers):
    result = find_positions(input_numbers)
    first_bin = ''
    second_bin = ''
    for x in range(len(result)):
        if result[x] > 0:
            first_bin += '1'
            second_bin += '0'
        else:
            first_bin += '0'
            second_bin += '1'
    return int(first_bin, 2) * int(second_bin, 2)


def task02(input_numbers):
    oxygen_numbers = input_numbers
    co2_numbers = input_numbers
    position = 0
    while len(oxygen_numbers) > 1 or len(co2_numbers) > 1:
        if len(oxygen_numbers) > 1:
            oxygen_numbers = filter_matches(oxygen_numbers, position, True)
        if len(co2_numbers) > 1:
            co2_numbers = filter_matches(co2_numbers, position, False)
        position += 1
    return int(''.join(oxygen_numbers), 2) * int(''.join(co2_numbers), 2)


prepared_file = read_file('day03.txt')
print(task01(prepared_file))
print(task02(prepared_file))

