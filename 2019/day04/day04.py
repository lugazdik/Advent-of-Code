def first_task(lower_bound, upper_bound):
    result = []
    for i in range(lower_bound, upper_bound):
        array = []
        for digit in str(i):
            array.append(int(digit))
        found_double = False
        valid = True
        for j in range(len(array) - 1):
            if array[j] == array[j+1]:
                found_double = True
            if array[j] > array[j+1]:
                valid = False
                break
        if valid and found_double:
            result.append(i)
    return result


def second_task(lower_bound, upper_bound):
    first_result = first_task(lower_bound, upper_bound)
    result = []
    for number in first_result:
        array = []
        for digit in str(number):
            array.append(digit)
        group_of_double = False
        i = 0
        while i < len(array) - 1:
            if array[i] == array[i+1]:
                count = 2
                i += 1
                while i + 1 <= len(array) - 1:
                    if array[i] != array[i+1]:
                        if count == 2:
                            group_of_double = True
                        break
                    else:
                        count += 1
                        i += 1
                if count == 2:
                    group_of_double = True
            if group_of_double:
                result.append(number)
                break
            else:
                i += 1
    return result


# WORKS, BUT UGLY CODE, SHOULD BE WAY SIMPLER
print(len(second_task(134564, 585159)))
