def first_task(file):
    with open(file, 'r') as f:
        result = 0
        for line in f:
            result += (int(line) // 3) - 2
        return result


def second_task(file):
    with open(file, 'r') as f:
        result = 0
        for line in f:
            res = (int(line) // 3) - 2
            while res > 0:
                result += res
                res = (res // 3) - 2
        return result


# print(first_task('day01.txt'))
print(second_task('day01.txt'))
