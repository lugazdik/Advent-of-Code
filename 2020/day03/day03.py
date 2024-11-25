def find_trees(file, right, down):
    with open(file, 'r') as f:
        x = y = result = current_line = 0
        for line in f:
            l = line.strip()
            if y != 0 and current_line == y:
                if l[x % len(l)] == "#":
                    result += 1
            if current_line == 0 or current_line == y:
                x += right
                y += down
            current_line += 1
        return result


def task2():
    check = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    result = 1
    for tmp in check:
        result *= find_trees('day03.txt', tmp[0], tmp[1])
    return result


print(task2())
