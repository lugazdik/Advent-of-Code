from collections import defaultdict, Counter


def read_input(input_path: str):
    with open(input_path, "r") as f:
        return list(map(int, f.read().strip().split()))


def get_stones_count_in_n_iterations(stones: list[int], iterations: int = 75) -> int:
    stones_dict = Counter(stones)
    for _ in range(iterations):
        new_stones = defaultdict(int)
        for stone in stones_dict.keys():
            if stone == 0:
                new_stones[1] += stones_dict[stone]
            elif (num_digits := len(str(stone))) % 2 == 0:
                new_stones[int(str(stone)[: num_digits // 2])] += stones_dict[stone]
                new_stones[int(str(stone)[num_digits // 2 :])] += stones_dict[stone]
            else:
                new_stones[stone * 2024] = stones_dict[stone]
        stones_dict = new_stones
    return sum(stones_dict.values())


input_stones = read_input("day11.txt")
print(f"part1: {get_stones_count_in_n_iterations(input_stones, 25)}")
print(f"part2: {get_stones_count_in_n_iterations(input_stones, 75)}")
