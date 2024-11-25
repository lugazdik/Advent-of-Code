def first_task(file):
    with open(file, 'r') as f:
        wires = []
        for line in f:
            wires.append(line.rstrip().split(','))
        wireOne = wires[0]
        wireTwo = wires[1]
        wireOnePoints = parse_instructions(wireOne)
        wireTwoPoints = parse_instructions(wireTwo)
        ints = find_intersections(wireOnePoints, wireTwoPoints)
        minSteps = ints[0][2]
        for inter in ints:
            if inter[2] < minSteps:
                minSteps = inter[2]
        return minSteps
            
               
def parse_instructions(instructions):
    result = []
    x = 0
    y = 0
    steps = 0
    for inst in instructions:
        count = int(inst[1:])
        while count > 0:
            steps += 1
            if inst[0] == 'U':
                y += 1
            elif inst[0] == 'D':
                y -= 1
            elif inst[0] == 'L':
                x -= 1
            elif inst[0] == 'R':
                x += 1
            result.append((x, y, steps))
            count -= 1
    return result


def find_intersections(first, second):
    result = []
    for i in first:
        for j in second:
            if i[0] != j[0]:
                continue
            if i[1] != j[1]:
                continue
            print(i, j, i[2]+j[2])
            result.append(i)
            break
    return result


# WORKS BUT TAKES TOO LONG!!!(SEVERAL MINUTES)
print(first_task('day03.txt'))
