
def task1(file):
    with open(file, 'r') as f:
        lines = []
        for line in f:
            a, b, c = line.split(' ')
            minimum, maximum = a.split('-')
            lines.append((int(minimum), int(maximum), b[0], c.strip()))
        result = 0
        for current in lines:
            count = 0
            for letter in current[3]:
                if letter == current[2]:
                    count += 1
            if current[0] <= count <= current[1]:
                result += 1
        return result


def task2(file):
    with open(file, 'r') as f:
        lines = []
        for line in f:
            a, b, c = line.split(' ')
            first, second = a.split('-')
            lines.append((int(first), int(second), b[0], c.strip()))
        result = 0
        for current in lines:
            if current[3][current[0] - 1] == current[2]:
                first = True
            else:
                first = False
            if current[3][current[1] - 1] == current[2]:
                second = True
            else:
                second = False
            if first != second:
                result += 1
        return result


print(task2('day02.txt'))
