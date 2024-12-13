import re
from math import lcm


def read_input(input_path: str):
    with open(input_path, "r") as f:
        claw_machines = []
        for claw_machine in f.read().split("\n\n"):
            item = []
            for line in claw_machine.split("\n"):
                item.append(tuple(map(int, re.findall(r"\d+", line))))
            claw_machines.append(item)
        return claw_machines


def solve_using_lcm(x1, y1, x2, y2, solution_x, solution_y):
    # system of linear equations, x1 * a + x2 * b = solution_x, y1 * a + y2 * b = solution_y, a, b >= 0
    lcm1 = lcm(x1, y1)
    b = ((lcm1 / x1) * solution_x - (lcm1 / y1) * solution_y) / (
        (lcm1 / x1) * x2 - (lcm1 / y1) * y2
    )
    if b.is_integer() and b >= 0:
        a = (solution_x - b * x2) / x1
        if a.is_integer() and a >= 0:
            return int(a), int(b)


def solve(claw_machines: list[list[tuple[int, int]]], part2: bool = False):
    result = 0
    for claw_machine in claw_machines:
        find_solutions = solve_using_lcm(
            claw_machine[0][0],
            claw_machine[0][1],
            claw_machine[1][0],
            claw_machine[1][1],
            claw_machine[2][0] + 10000000000000 if part2 else claw_machine[2][0],
            claw_machine[2][1] + 10000000000000 if part2 else claw_machine[2][1],
        )
        if find_solutions:
            result += find_solutions[0] * 3 + find_solutions[1]
    return result


machines = read_input("day13.txt")
print(solve(machines))
print(solve(machines, True))
