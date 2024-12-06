def read_input(input_path: str) -> list[list[str]]:
    with open(input_path, "r") as f:
        return [[*(line.strip())] for line in f.readlines()]


def find_start() -> tuple[int, int]:
    for row in range(len(GRID)):
        for col in range(len(GRID[row])):
            if GRID[row][col] == "^":
                return row, col


def new_direction(cur_direction: str) -> str:
    if cur_direction == "up":
        return "right"
    if cur_direction == "right":
        return "down"
    if cur_direction == "down":
        return "left"
    if cur_direction == "left":
        return "up"


def move_position(postion: tuple[int, int], direction) -> tuple[int, int]:
    if direction == "up":
        return postion[0] - 1, postion[1]
    if direction == "down":
        return postion[0] + 1, postion[1]
    if direction == "left":
        return postion[0], postion[1] - 1
    if direction == "right":
        return postion[0], postion[1] + 1


def is_in_bounds(pos: tuple[int, int]) -> bool:
    return 0 <= pos[0] < len(GRID) and 0 <= pos[1] < len(GRID[0])


def check_path(grid: list[list[str]]) -> tuple[set[tuple[int, int]], bool]:
    # returns visited positions and if the path loops
    visited = set()
    cur_pos = START
    cur_dir = "up"
    states = {cur_pos + tuple([cur_dir])}
    while is_in_bounds(cur_pos):
        visited.add(cur_pos)
        next_pos = move_position(cur_pos, cur_dir)
        if is_in_bounds(next_pos) and grid[next_pos[0]][next_pos[1]] == "#":
            cur_dir = new_direction(cur_dir)
        else:
            cur_pos = next_pos
        cur_state = cur_pos + tuple([cur_dir])
        if cur_state in states:
            return visited, True
        states.add(cur_state)
    return visited, False


GRID = read_input("day06.txt")
START = find_start()


def find_solutions() -> tuple[int, int]:
    original_path = check_path(GRID)[0]
    count_loops = 0
    for pos in original_path - {START}:
        new_grid = [row[:] for row in GRID]
        new_grid[pos[0]][pos[1]] = "#"
        if check_path(new_grid)[1]:
            count_loops += 1
    return len(original_path), count_loops


# for part 1 call check_path(GRID)[0]
print(find_solutions())
