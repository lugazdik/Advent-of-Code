from collections import deque


def read_input(input_path: str):
    with open(input_path, "r") as f:
        grid = []
        starting_points = []
        for row_index, line in enumerate(f.readlines()):
            row = []
            for col_index, number in enumerate(line.strip()):
                row.append(int(number))
                if int(number) == 0:
                    starting_points.append((row_index, col_index))
            grid.append(row)
        return grid, starting_points


def solve(grid, starting_points, part2=False):
    # BFS with queue of current point and starting points coming to the current point
    queue = deque(
        (starting_point, [starting_point]) for starting_point in starting_points
    )
    ends = {}
    while queue:
        curr_pos = queue.popleft()
        if grid[curr_pos[0][0]][curr_pos[0][1]] == 9:
            ends[curr_pos[0]] = curr_pos[1]
            continue
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = (curr_pos[0][0] + direction[0], curr_pos[0][1] + direction[1])
            if (
                0 <= new_pos[0] < len(grid)
                and 0 <= new_pos[1] < len(grid[0])
                and grid[new_pos[0]][new_pos[1]]
                == grid[curr_pos[0][0]][curr_pos[0][1]] + 1
            ):
                found = False
                for item in queue:
                    if item[0] == new_pos:
                        item[1].extend(curr_pos[1])
                        found = True
                        break
                if not found:
                    queue.append((new_pos, curr_pos[1].copy()))
    if part2:
        return sum(len(ends[end]) for end in ends)
    else:
        return sum(
            1
            for starting_point in starting_points
            for end in ends
            if starting_point in ends[end]
        )


grid, starting_points = read_input("day10.txt")
print(solve(grid, starting_points))
print(solve(grid, starting_points, part2=True))
