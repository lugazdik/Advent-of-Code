import math

def part1():
    with open('day06.txt', 'r') as file:
        lines = file.readlines()
        number_lines = []
        operator_line = []
        for line in lines:
            split_line = line.split()
            if all(item.isdigit() for item in split_line):
                number_lines.append(list(map(int, split_line)))
            else:
                operator_line = split_line
    sums = 0
    for i in range(len(number_lines[0])):
        if operator_line[i] == '+':
            sums += sum(item[i] for item in number_lines)
        elif operator_line[i] == '*':
            sums += math.prod(item[i] for item in number_lines)
    return sums

def part2():
    with open('day06.txt', 'r') as file:
        lines = file.read().splitlines()
        number_lines = []
        operator_line = []
        for i in range(len(lines)):
            if i < len(lines) - 1:
                number_lines.append(list(lines[i])[::-1])
            else:
                operator_line = lines[i].split()[::-1]
    operator_index = 0
    current_operator = operator_line[operator_index]
    sums = 0
    current_numbers = []
    for i in range(len(number_lines[0])):
        if all(item[i] == " " for item in number_lines):
            if current_operator == '+':
                sums += sum(current_numbers)
            elif current_operator == '*':
                sums += math.prod(current_numbers)
            current_numbers = []
            operator_index += 1
            current_operator = operator_line[operator_index]
        else:
            current_numbers.append(int("".join([item[i] for item in number_lines if item[i].isdigit()])))
    if current_operator:
        if current_operator == '+':
            sums += sum(current_numbers)
        elif current_operator == '*':
            sums += math.prod(current_numbers)
    return sums



print(part1())
print(part2())
    