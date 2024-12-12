from collections import deque


def read_input(input_path: str):
    with open(input_path, "r") as f:
        return [list(row.strip()) for row in f.readlines()]


def part1(grid: list[list[str]]):
    garden_plots = []
    for row_index in range(len(grid)):
        for col_index in range(len(grid[0])):
            if grid[row_index][col_index] is not None:
                garden_plots.append(bfs(grid, (row_index, col_index)))
    return sum([area * perimeter for area, perimeter in garden_plots])


def bfs(grid: list[list[str]], start_position: tuple[int, int]):
    queue = deque([start_position])
    plot_symbol = grid[start_position[0]][start_position[1]]
    seen = set()
    area = 0
    perimeter = 0
    while queue:
        row, col = queue.popleft()
        if (row, col) in seen:
            continue
        seen.add((row, col))
        area += 1
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row = row + direction[0]
            new_col = col + direction[1]
            if (
                0 <= new_row < len(grid)
                and 0 <= new_col < len(grid[0])
                and grid[new_row][new_col] == plot_symbol
            ):
                queue.append((new_row, new_col))
            else:
                perimeter += 1
    for row, col in seen:
        grid[row][col] = None
    return area, perimeter


print(part1(read_input("day12.txt")))
