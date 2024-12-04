DIAGONALS = ["up_left", "up_right", "down_left", "down_right"]
DIRECTIONS = ["up", "down", "left", "right"] + DIAGONALS


def read_input(input_path: str):
    grid = []
    with open(input_path, "r") as f:
        for line in f.readlines():
            grid.append(list(line.strip()))
    return grid


def check_position(
    col: int, row: int, search_char_index: int, direction: str, search_word: tuple[str]
):
    if col < 0 or row < 0 or col >= len(GRID[0]) or row >= len(GRID):
        return 0
    if GRID[row][col] != search_word[search_char_index]:
        return 0
    else:
        if search_char_index == len(search_word) - 1:
            return 1
        else:
            if direction == "up":
                return check_position(
                    col - 1, row, search_char_index + 1, direction, search_word
                )
            elif direction == "down":
                return check_position(
                    col + 1, row, search_char_index + 1, direction, search_word
                )
            elif direction == "left":
                return check_position(
                    col, row - 1, search_char_index + 1, direction, search_word
                )
            elif direction == "right":
                return check_position(
                    col, row + 1, search_char_index + 1, direction, search_word
                )
            elif direction == "up_left":
                return check_position(
                    col - 1, row - 1, search_char_index + 1, direction, search_word
                )
            elif direction == "up_right":
                return check_position(
                    col - 1, row + 1, search_char_index + 1, direction, search_word
                )
            elif direction == "down_left":
                return check_position(
                    col + 1, row - 1, search_char_index + 1, direction, search_word
                )
            elif direction == "down_right":
                return check_position(
                    col + 1, row + 1, search_char_index + 1, direction, search_word
                )


def part1():
    search_word = ["X", "M", "A", "S"]
    result = 0
    for row in range(len(GRID)):
        for col in range(len(GRID[0])):
            for direction in DIRECTIONS:
                result += check_position(col, row, 0, direction, tuple(search_word))
    return result


def part2():
    search_word = ["M", "A", "S"]
    result = 0
    for row in range(len(GRID)):
        for col in range(len(GRID[0])):
            if check_position(
                col, row, 0, "down_right", tuple(search_word)
            ) or check_position(col, row, 0, "down_right", tuple(search_word[::-1])):
                if check_position(
                    col, row + 2, 0, "down_left", tuple(search_word)
                ) or check_position(
                    col, row + 2, 0, "down_left", tuple(search_word[::-1])
                ):
                    result += 1
    return result


GRID = read_input("day04.txt")
print(part1())
print(part2())
