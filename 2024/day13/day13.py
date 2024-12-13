import re


def read_input(input_path: str):
    with open(input_path, "r") as f:
        claw_machines = []
        for claw_machine in f.read().split("\n\n"):
            item = []
            for line in claw_machine.split("\n"):
                item.append(tuple(map(int, re.findall(r"\d+", line))))
            claw_machines.append(item)
        return claw_machines


def brute_force(x1, y1, x2, y2, solution_x, solution_y):
    solutions = []
    for a in range(101):
        for b in range(101):
            if x1 * a + x2 * b == solution_x and y1 * a + y2 * b == solution_y:
                solutions.append((a, b))
    return solutions


def part1(claw_machines: list[list[tuple[int, int]]]):
    result = 0
    for claw_machine in claw_machines:
        find_solutions = brute_force(
            claw_machine[0][0],
            claw_machine[0][1],
            claw_machine[1][0],
            claw_machine[1][1],
            claw_machine[2][0],
            claw_machine[2][1],
        )
        if find_solutions:
            result += min(a * 3 + b for a, b in find_solutions)
    return result


machines = read_input("day13.txt")
print(part1(machines))
