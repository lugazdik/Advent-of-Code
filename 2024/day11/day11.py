def read_input(input_path: str):
    with open(input_path, "r") as f:
        return list(map(int, f.read().strip().split()))


def brute_force(stones: list[int], iterations: int = 25) -> int:
    for _ in range(iterations):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif (num_digits := len(str(stone))) % 2 == 0:
                new_stones.append(int(str(stone)[: num_digits // 2]))
                new_stones.append(int(str(stone)[num_digits // 2 :]))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return len(stones)


print(brute_force(read_input("day11.txt")))
