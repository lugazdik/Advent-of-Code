import re


def task1(file):
    with open(file, 'r') as f:
        string = f.read()
        passports = string.split('\n\n')
        fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        result = 0
        for passport in passports:
            valid = True
            split_pass = re.split(' |\n', passport)
            found = [False, False, False, False, False, False, False]
            for field in split_pass:
                split_field = field.split(':')
                if split_field[0] == fields[0]:
                    found[0] = True
                elif split_field[0] == fields[1]:
                    found[1] = True
                elif split_field[0] == fields[2]:
                    found[2] = True
                elif split_field[0] == fields[3]:
                    found[3] = True
                elif split_field[0] == fields[4]:
                    found[4] = True
                elif split_field[0] == fields[5]:
                    found[5] = True
                elif split_field[0] == fields[6]:
                    found[6] = True
            for i in found:
                if not i:
                    valid = False
            if valid:
                result += 1
        return result


def task2(file):
    with open(file, 'r') as f:
        string = f.read()
        passports = string.split('\n\n')
        fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        result = 0
        for passport in passports:
            ok = True
            split_pass = re.split(' |\n', passport)
            found = [False, False, False, False, False, False, False]
            valid = [False, False, False, False, False, False, False]
            for field in split_pass:
                split_field = field.split(':')
                if split_field[0] == fields[0]:
                    found[0] = True
                    if split_field[1].isnumeric() and 1920 <= int(split_field[1]) <= 2002:
                        valid[0] = True
                    else:
                        valid[0] = False
                        break
                elif split_field[0] == fields[1]:
                    found[1] = True
                    if split_field[1].isnumeric() and 2010 <= int(split_field[1]) <= 2020:
                        valid[1] = True
                    else:
                        valid[1] = False
                        break
                elif split_field[0] == fields[2]:
                    found[2] = True
                    if split_field[1].isnumeric() and 2020 <= int(split_field[1]) <= 2030:
                        valid[2] = True
                    else:
                        valid[2] = False
                        break
                elif split_field[0] == fields[3]:
                    found[3] = True
                    match = re.search(r'(\d+)(in|cm)', split_field[1])
                    if match:
                        if match[2] == 'in':
                            if 59 <= int(match[1]) <= 76:
                                valid[3] = True
                            else:
                                valid[3] = False
                                break
                        else:
                            if 150 <= int(match[1]) <= 193:
                                valid[3] = True
                            else:
                                valid[3] = False
                                break
                    else:
                        valid[3] = False
                        break
                elif split_field[0] == fields[4]:
                    found[4] = True
                    match = re.search(r'^#(?:[0-9a-f]{3}){1,2}$', split_field[1])
                    if match:
                        valid[4] = True
                    else:
                        valid[4] = False
                        break
                elif split_field[0] == fields[5]:
                    found[5] = True
                    if split_field[1] in eye_color:
                        valid[5] = True
                    else:
                        valid[5] = False
                        break
                elif split_field[0] == fields[6]:
                    found[6] = True
                    if not split_field[1].isnumeric() or len(split_field[1]) != 9:
                        valid[6] = False
                        break
                    else:
                        valid[6] = True
            for i in found:
                if not i:
                    ok = False
                    break
            for i in valid:
                if not i:
                    ok = False
                    break
            if ok:
                result += 1
        return result


print(task1('day04.txt'))
print(task2('day04.txt'))
