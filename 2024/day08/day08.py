from collections import defaultdict

ANTENAS = defaultdict(list)


def read_input(input_path: str) -> list[list[str]]:
    with open(input_path, "r") as f:
        read_lines = f.readlines()
        row_len = len(read_lines)
        col_len = len(read_lines[0].strip())
        for row, line in enumerate(read_lines):
            for col, char in enumerate(line.strip()):
                if char != ".":
                    ANTENAS[char].append((row, col))
    return row_len, col_len


def find_antinodes(pos1, pos2, part2=False):
    antinodes = set() if not part2 else {pos1, pos2}
    row_diff = pos2[0] - pos1[0]
    col_diff = pos2[1] - pos1[1]
    first_antinode = (pos1[0] - row_diff, pos1[1] - col_diff)
    while 0 <= first_antinode[0] < ROW_LEN and 0 <= first_antinode[1] < COL_LEN:
        antinodes.add(first_antinode)
        if not part2:
            break
        first_antinode = (first_antinode[0] - row_diff, first_antinode[1] - col_diff)
    second_antinode = (pos2[0] + row_diff, pos2[1] + col_diff)
    while 0 <= second_antinode[0] < ROW_LEN and 0 <= second_antinode[1] < COL_LEN:
        antinodes.add(second_antinode)
        if not part2:
            break
        second_antinode = (second_antinode[0] + row_diff, second_antinode[1] + col_diff)
    return antinodes


def solve(part2=False):
    unique_antinodes = set()
    for positions in ANTENAS.values():
        for pos1 in positions:
            for pos2 in positions:
                if pos1 == pos2:
                    continue
                unique_antinodes = unique_antinodes.union(
                    find_antinodes(pos1, pos2, part2)
                )
    return len(unique_antinodes)


ROW_LEN, COL_LEN = read_input("day08.txt")
print(solve())
print(solve(part2=True))
