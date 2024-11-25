# link to source problem: https://adventofcode.com/2015/day/4
import hashlib


def read_file(path):
    with open(path, 'r') as file:
        return file.read()


def task01(parsed_input):
    number = 0
    while True:
        combined_input = parsed_input + str(number)
        result = hashlib.md5(combined_input.encode())
        if str(result.hexdigest()).startswith('00000'):
            return number
        number += 1


def task02(parsed_input):
    number = 0
    while True:
        combined_input = parsed_input + str(number)
        result = hashlib.md5(combined_input.encode())
        if str(result.hexdigest()).startswith('000000'):
            return number
        number += 1


prepared_file = read_file('day04.txt')
print(task01(prepared_file))
print(task02(prepared_file))
