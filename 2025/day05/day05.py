with open('day05.txt', 'r') as file:
    ranges, items = file.read().split('\n\n')
    fresh_items = []
    i = 0
    for r in ranges.split('\n'):
        start, end = map(int, r.split('-'))
        fresh_items.append((start, end))
    items = list(map(int, items.split('\n')))

def is_fresh(item, fresh_items):
    for start, end in fresh_items:
        if item >= start and item <= end:
            return True
    return False

def part1(fresh_items, items):
    count_fresh = 0
    for item in items:
        if is_fresh(item, fresh_items):
            count_fresh += 1
    return count_fresh
        

def part2(fresh_items):
    sorted_ranges = sorted(fresh_items)
    merged = [sorted_ranges[0]]
    for current_start, current_end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]
        if current_start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            merged.append((current_start, current_end))

    return sum(end - start + 1 for start, end in merged)

print(part1(fresh_items, items))
print(part2(fresh_items))