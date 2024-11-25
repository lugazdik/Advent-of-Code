def first_task(file, width, height):
    with open(file, 'r') as f:
        string = f.read()
        layers = [[] for i in range(len(string) // (width * height))]
        parse_input(layers, string, width * height)
        min_layer = min(layers, key=find_layer_with_least_zeroes)
        one_digits = find_digit_count(min_layer, 1)
        two_digits = find_digit_count(min_layer, 2)
        return one_digits * two_digits


def second_task(file, width, height):
    with open(file, 'r') as f:
        string = f.read()
        layers = [[] for i in range(len(string) // (width * height))]
        parse_input(layers, string, width * height)
        result = [2 for i in range(width * height)]
        for layer in layers:
            index = 0
            for digit in layer:
                if result[index] == 2 and digit != 2:
                    result[index] = digit
                index += 1
        print_result(result, width, height)
        return result


def find_layer_with_least_zeroes(layer):
    count = 0
    for digit in layer:
        if digit == 0:
            count += 1
    return count


def find_digit_count(layer, digit):
    count = 0
    for num in layer:
        if num == digit:
            count += 1
    return count


def parse_input(layers, string, size):
    index = 0
    for digit in string:
        if len(layers[index]) == size:
            index += 1
        layers[index].append(int(digit))


def print_result(result, width, height):
    for j in range(height):
        line = ''
        for i in range(width):
            if result[j * width + i] == 0:
                line += ' '
            elif result[j * width + i] == 1:
                line += '#'
        print(line)


print(first_task('day08.txt', 25, 6))
second_task('day08.txt', 25, 6)
