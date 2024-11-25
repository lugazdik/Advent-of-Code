# link to source problem: https://adventofcode.com/2021/day/4

def read_file(file, matrix_dim):
    with open(file, 'r') as f:
        lines = f.readlines()
        draw = lines[0].split(',')
        lines.pop(0)
        matrices = []
        matrix = []
        index = 0
        for line in lines:
            if line == '\n':
                continue
            matrix.append(list(map(list, zip(line.split(), [False] * matrix_dim))))
            index += 1
            if index == matrix_dim:
                index = 0
                matrices.append(matrix)
                matrix = []
        return draw, matrices


def find_number(matrix, number):
    for row_number in range(len(matrix)):
        for column_number in range(len(matrix)):
            if matrix[row_number][column_number][0] == number:
                matrix[row_number][column_number][1] = True
                return check_row(matrix, row_number) or check_column(matrix, column_number)
    return False


def check_row(matrix, row):
    for column in range(len(matrix)):
        if not matrix[row][column][1]:
            return False
    return True


def check_column(matrix, column):
    for row in range(len(matrix)):
        if not matrix[row][column][1]:
            return False
    return True


def calculate_result(matrix, number):
    unchecked_sum = 0
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            if not matrix[row][column][1]:
                unchecked_sum += int(matrix[row][column][0])
    return unchecked_sum * int(number)


def task1(draw, matrices):
    for number in draw:
        for matrix in matrices:
            if find_number(matrix, number):
                return calculate_result(matrix, number)


def task2(draw, matrices):
    for number in draw:
        to_remove = []
        for matrix in matrices:
            if find_number(matrix, number):
                to_remove.append(matrix)
        if len(matrices) == 1 and len(to_remove) == 1:
            return calculate_result(to_remove[0], number)
        for m in to_remove:
            matrices.remove(m)


inp, mat = read_file('day04.txt', 5)
print(task1(inp, mat))
print(task2(inp, mat))
