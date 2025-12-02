with open('day01.txt', 'r') as file:
    instructions = [(line[0], int(line[1:])) for line in file]

def part1(instructions):
    final_position = 50
    count_zeros = 0
    for direction, number in instructions:
        if direction == 'L':
            final_position = (final_position - number) % 100
        elif direction == 'R':
            final_position = (final_position + number) % 100
        if final_position == 0:
            count_zeros += 1
    return count_zeros

def part2(instructions):
    final_position = 50
    count_zeros = 0
    for direction, number in instructions:
        if number > 100:
            count_zeros += number // 100
            number = number % 100
        if direction == 'L':
            if final_position - number <= 0 and final_position != 0:
                count_zeros += 1
            final_position = (final_position - number) % 100
        elif direction == 'R':
            if final_position + number >= 100 and final_position != 0:
                count_zeros += 1
            final_position = (final_position + number) % 100
    return count_zeros

print(part1(instructions))
print(part2(instructions))