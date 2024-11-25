def task1(file):
    with open(file, 'r') as f:
        numbers = []
        for line in f:
            numbers.append(int(line))
        for number in numbers:
            looking_for = 2020 - number
            if looking_for in numbers:
                print(looking_for*number)


# task1('day01.txt')

def task2(file):
    with open(file, 'r') as f:
        numbers = []
        for line in f:
            numbers.append(int(line))
        for i in range(len(numbers)):
            num1 = numbers[i]
            for j in range(i, len(numbers)):
                num2 = numbers[j]
                if num1 + num2 < 2020:
                    for k in range(j, len(numbers)):
                        num3 = numbers[k]
                        if num1+num2+num3 == 2020:
                            print(num1*num2*num3)


# task2('day01.txt')
