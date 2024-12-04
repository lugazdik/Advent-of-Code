GRID = []


def read_input(input_path: str):
    with open(input_path, "r") as f:
        for line in f.readlines():
            GRID.append(list(line.strip()))


def check_position(
    row: int, col: int, search_word: list[str], search_char_index: int, direction: str
):
    if row < 0 or col < 0 or row >= len(GRID) or col >= len(GRID[0]):
        return 0
    if GRID[row][col] != search_word[search_char_index]:
        return 0
    else:
        if search_char_index == len(search_word) - 1:
            return 1
        else:
            if direction == "down":
                return check_position(
                    row, col + 1, search_word, search_char_index + 1, direction
                )
            elif direction == "right":
                return check_position(
                    row + 1, col, search_word, search_char_index + 1, direction
                )
            elif direction == "down_left":
                return check_position(
                    row - 1, col + 1, search_word, search_char_index + 1, direction
                )
            elif direction == "down_right":
                return check_position(
                    row + 1, col + 1, search_word, search_char_index + 1, direction
                )


def part1(search_word: list[str]):
    result = 0
    for row in range(len(GRID)):
        for col in range(len(GRID[0])):
            # it is enough to check these directions since we look for reverse word as well
            for direction in ["down", "right", "down_left", "down_right"]:
                result += check_position(
                    row, col, search_word, 0, direction
                ) or check_position(row, col, search_word[::-1], 0, direction)
    return result


def part2(search_word: list[str]):
    result = 0
    for row in range(len(GRID)):
        for col in range(len(GRID[0])):
            if check_position(row, col, search_word, 0, "down_right") or check_position(
                row, col, search_word[::-1], 0, "down_right"
            ):
                result += check_position(
                    row + 2, col, search_word, 0, "down_left"
                ) or check_position(row + 2, col, search_word[::-1], 0, "down_left")
    return result


read_input("day04.txt")
print(part1(["X", "M", "A", "S"]))
print(part2(["M", "A", "S"]))
