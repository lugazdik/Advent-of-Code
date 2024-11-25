def first_task(file, first, second):
    with open(file, 'r') as f:
        ops = [int(s) for s in f.read().split(',')]
        ops[1] = first
        ops[2] = second
        pos = 0
        while pos < len(ops) and ops[pos] != 99:
            first_index = ops[pos + 1]
            second_index = ops[pos + 2]
            res_index = ops[pos + 3]
            if ops[pos] == 1:
                ops[res_index] = ops[first_index] + ops[second_index]
            elif ops[pos] == 2:
                ops[res_index] = ops[first_index] * ops[second_index]
            pos += 4
        return ops[0]

        
def second_task(file):
    for i in range(0, 100):
        for j in range(0, 100):
            if first_task(file, i, j) == 19690720:
                return 100 * i + j


# print(first_task('day02.txt', 12, 2))
print(second_task('day02.txt'))
