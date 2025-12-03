with open("day03.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

def part1(lines):
    joltages = []
    for line in lines:
        first_digit = 0
        second_digit = 0
        for index, digit in enumerate(line):
            if int(digit) > first_digit and index < len(line) - 1:
                first_digit = int(digit)
                second_digit = 0
                continue
            if int(digit) > second_digit:
                second_digit = int(digit)
                continue
        joltages.append(str(first_digit) + str(second_digit))
    return sum([int(joltage) for joltage in joltages])

def part2(lines, joltage_length=12):
    joltages = []
    for line in lines:
        current_joltage = [0] * joltage_length
        digits = [int(digit) for digit in line]
        last_jolt_index = 0
        for jolt_index in range(joltage_length):
            rest_index = joltage_length - jolt_index
            rest_digits = digits[last_jolt_index: len(digits) - rest_index + 1]
            max_joltage = max(rest_digits)
            max_joltage_index = rest_digits.index(max_joltage)
            current_joltage[jolt_index] = max_joltage
            last_jolt_index += max_joltage_index + 1
        joltages.append(''.join([str(joltage) for joltage in current_joltage]))
    return sum([int(joltage) for joltage in joltages])

# print(part1(lines))
print(part2(lines))
            