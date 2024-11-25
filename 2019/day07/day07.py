import IntcodeComputer as intcode
import itertools


def first_task(file):    
    permutations = list(itertools.permutations([0, 1, 2, 3, 4]))
    results = []
    for perm in permutations:
        input_code = [0]
        for digit in perm:
            input_code = intcode.calculate('day7.txt', [digit, input_code[0]])
        results.append(input_code[0])
    return max(results)


# first part done, second no idea
print(first_task('day7.txt'))
