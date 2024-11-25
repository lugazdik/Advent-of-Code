# link to source problem: https://adventofcode.com/2021/day/6

def read_file(file):
    with open(file, 'r') as f:
        return list(map(int, f.readline().split(',')))


def task_naive_impl(file_input, days):
    joined_list = file_input
    for i in range(days):
        add_array = []
        for x in range(len(joined_list)):
            if joined_list[x] == 0:
                joined_list[x] = 6
                add_array.append(8)
            else:
                joined_list[x] -= 1
        joined_list = joined_list + add_array
    return len(joined_list)


def task_smart_impl(file_input, days):
    fishes = [file_input.count(i) for i in range(9)]
    for x in range(days):
        num = fishes.pop(0)
        fishes[6] += num
        fishes.append(num)
    return sum(fishes)


res = read_file('day06.txt')
# print(task_naive_impl(res, 80))
print(task_smart_impl(res, 256))
