from copy import deepcopy
with open("day04.txt", "r") as file:
    grid = []
    for line in file.readlines():
        grid.append(list(line.strip()))

possible_neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def check_neighbors(grid, row, col):
    count = 0
    for neighbor in possible_neighbors:
        new_row = row + neighbor[0]
        new_col = col + neighbor[1]
        if new_row >= 0 and new_row < len(grid) and new_col >= 0 and new_col < len(grid[new_row]) and grid[new_row][new_col] == "@":
            count += 1
    return count

def part1(grid, remove: bool = False):
    accessible_cells = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "@" and check_neighbors(grid, row, col) < 4:
                accessible_cells.append((row, col))
    if remove:
        for row, col in accessible_cells:
            grid[row][col] = "."
    return len(accessible_cells)

def part2(grid):
    count_accessible = 0
    while (accessible_cells := part1(grid, True)) > 0:
        count_accessible += accessible_cells
    return count_accessible

print(part1(grid))
print(part2(deepcopy(grid)))