
def task1(file):
    with open(file, 'r') as f:
        groups = f.read().split('\n\n')
        res = 0
        for group in groups:
            split_group = group.split('\n')
            values = set()
            for g in split_group:
                for letter in g:
                    values.add(letter)
            res += len(values)
        return res


def task2(file):
    with open(file, 'r') as f:
        groups = f.read().split('\n\n')
        res = 0
        for group in groups:
            split_group = group.split('\n')
            group_values = set()
            first = True
            for g in split_group:
                values = set()
                for letter in g:
                    values.add(letter)
                if len(group_values) == 0 and first:
                    group_values = group_values.union(values)
                    first = False
                else:
                    group_values = group_values.intersection(values)
            res += len(group_values)
        return res


# print(task1('day06.txt'))
# print(task2('day06.txt'))
