def read_input(input_path: str) -> list[list[str]]:
    equations = {}
    with open(input_path, "r") as f:
        for line in f.readlines():
            split_line = line.strip().split(": ")
            equations[int(split_line[0])] = list(map(int, split_line[1].split(" ")))
    return equations


def evaluate(equation: list[int], result: int, part2: bool = False) -> bool:
    if not result.is_integer() or result < 0:
        return False
    if len(equation) == 1:
        return equation[0] == result
    if part2:
        concat_result = False
        if str(int(result)).endswith(str(equation[0])):
            concat = str(int(result))[: -len(str(equation[0]))]
            if concat != "":
                concat_result = True
        # try addition, multiplication, and concatenation
        return (
            evaluate(equation[1:], result - equation[0], part2)
            or evaluate(equation[1:], result / equation[0], part2)
            or (evaluate(equation[1:], int(concat), part2) if concat_result else False)
        )
    return evaluate(equation[1:], result - equation[0], part2) or evaluate(
        equation[1:], result / equation[0], part2
    )


def find_solution(equations: dict[int, list[int]], part2: bool = False) -> int:
    return sum(
        [
            result
            for result, operands in equations.items()
            if evaluate(operands[::-1], result, part2)
        ]
    )


parsed_input = read_input("day07.txt")
print(find_solution(parsed_input))
print(find_solution(parsed_input, part2=True))
