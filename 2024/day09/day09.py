def read_input(input_path: str):
    with open(input_path, "r") as f:
        grid = []
        memory_block_num = 0
        for index, item in enumerate(list(map(int, f.read().strip()))):
            if index % 2 == 0:
                for _ in range(item):
                    grid.append(memory_block_num)
                memory_block_num += 1
            else:
                for _ in range(item):
                    grid.append(".")
        return grid


def re_arrange_memory(parsed_input: list[str | int]) -> list[str | int]:
    while True:
        first_empty_index = parsed_input.index(".")
        last_memory_block_index = 0
        for index in range(len(parsed_input) - 1, 0, -1):
            if parsed_input[index] != ".":
                last_memory_block_index = index
                break
        if first_empty_index > last_memory_block_index:
            break
        else:
            parsed_input[first_empty_index] = parsed_input[last_memory_block_index]
            parsed_input[last_memory_block_index] = "."
    return parsed_input


def part1(parsed_input: list[str]) -> int:
    re_arranged_memory = re_arrange_memory(parsed_input)
    index = 0
    result = 0
    while re_arranged_memory[index] != ".":
        result += index * int(re_arranged_memory[index])
        index += 1
    return result


parsed_input = read_input("day09.txt")
print(part1(parsed_input))
