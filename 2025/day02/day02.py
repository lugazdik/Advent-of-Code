with open('day02.txt', 'r') as file:
    ranges = []
    split_ranges = file.read().split(',')
    for item in split_ranges:
        ranges.append(tuple(map(int, item.split('-'))))

def part1(ranges):
    invalid_ids = []
    for item in ranges:
        numbers_to_check = list(map(str, list(range(item[0], item[1] + 1))))
        for number in numbers_to_check:
            if number[:len(number)//2] == number[len(number)//2:]:
                invalid_ids.append(int(number))
    return sum(invalid_ids)

def part2(ranges):
    invalid_ids = []
    for item in ranges:
        numbers_to_check = list(map(str, list(range(item[0], item[1] + 1))))
        for number in numbers_to_check:
            count_unique = len(set(number))
            if count_unique > len(number)//2:
                continue
            for split_len in range(count_unique, (len(number)//2) + 1):
                if len(number) % split_len != 0:
                    continue
                split_number = [number[index:index + split_len] for index in range(0, len(number), split_len)]
                if len(split_number) > 1 and all(num == split_number[0] for num in split_number):
                    invalid_ids.append(int(number))
                    break
    return sum(invalid_ids)

print(part1(ranges))
print(part2(ranges))