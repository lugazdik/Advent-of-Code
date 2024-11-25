# link to source problem: https://adventofcode.com/2015/day/5


def read_file(path):
    result = []
    with open(path, 'r') as file:
        for line in file.readlines():
            result.append(line.strip())
    return result


def count_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for item in vowels:
        count += word.count(item)
        if count > 2:
            return True
    return False


def has_double_letter(word):
    prev = ''
    for letter in word:
        if prev == letter:
            return True
        prev = letter
    return False


def task01(parsed_input):
    invalid_strings = ['ab', 'cd', 'pq', 'xy']
    count_nice = 0
    for entry in parsed_input:
        if count_vowels(entry) and has_double_letter(entry):
            nice = True
            for item in invalid_strings:
                if item in entry:
                    nice = False
                    break
            if nice:
                count_nice += 1
    return count_nice


def two_letter_copy_no_overlap(word):
    for i in range(len(word) - 2):
        if word[i:i+2] in word[i+2:]:
            return True
    return False


def repeat_after_exactly_one_letter(word):
    for i in range(len(word) - 2):
        if word[i] == word[i + 2]:
            return True
    return False


def task02(parsed_input):
    count_nice = 0
    for entry in parsed_input:
        if two_letter_copy_no_overlap(entry) and repeat_after_exactly_one_letter(entry):
            count_nice += 1
    return count_nice


prepared_file = read_file('day05.txt')
print(task01(prepared_file))
print(task02(prepared_file))
