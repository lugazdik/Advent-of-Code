def read_input(input_path: str):
    with open(input_path, "r") as f:
        disk = []
        memory_block_id = 0
        for index, item in enumerate(list(map(int, f.read().strip()))):
            if index % 2 == 0:
                disk += [memory_block_id] * item
                memory_block_id += 1
            else:
                disk += [None] * item
        return disk


def re_arrange_memory(disk: list[int | None]) -> list[int | None]:
    first_empty_index = disk.index(None)
    last_non_empty_index = len(disk) - 1
    while last_non_empty_index > first_empty_index:
        disk[first_empty_index], disk[last_non_empty_index] = (
            disk[last_non_empty_index],
            disk[first_empty_index],
        )
        while disk[last_non_empty_index] is None:
            last_non_empty_index -= 1
        while disk[first_empty_index] is not None:
            first_empty_index += 1
    return disk


def re_arrange_memory_part2(disk: list[int | None]) -> list[int | None]:
    last_memory_id = disk[-1]
    for to_move in range(last_memory_id, -1, -1):
        first_empty_index = disk.index(None)
        to_move_index = disk.index(to_move)
        to_move_size = 0
        for idx in range(to_move_index, len(disk)):
            if disk[idx] == to_move:
                to_move_size += 1
            else:
                break
        free_size = 0
        while first_empty_index < to_move_index and free_size < to_move_size:
            first_empty_index = first_empty_index + free_size
            free_size = 0
            while disk[first_empty_index] is not None:
                first_empty_index += 1
            while (
                first_empty_index + free_size < len(disk)
                and disk[first_empty_index + free_size] is None
            ):
                free_size += 1
        if first_empty_index < to_move_index:
            # Move file by swapping block values
            for idx in range(first_empty_index, first_empty_index + to_move_size):
                disk[idx] = to_move
            for idx in range(to_move_index, to_move_index + to_move_size):
                disk[idx] = None
    return disk


def find_checksum(disk: list[int | None]) -> int:
    return sum([index * block for index, block in enumerate(disk) if block is not None])


original_disk = read_input("day09.txt")
print(find_checksum(re_arrange_memory(original_disk.copy())))
print(find_checksum(re_arrange_memory_part2(original_disk.copy())))
