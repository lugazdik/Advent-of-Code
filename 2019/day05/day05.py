def first_task(file, input_number):
    with open(file, 'r') as f:
        ops = [int(s) for s in f.read().split(',')]
        pos = 0
        outputs = []
        while pos < len(ops) and ops[pos] != 99:
            if ops[pos] == 3:
                ops[ops[pos+1]] = input_number
                pos += 2
            elif ops[pos] == 4:
                outputs.append(ops[ops[pos+1]])
                pos += 2
            else:
                inst_code = [0, 0, 0, 0, 0]
                i = 0
                inst_str = str(ops[pos])
                for digit in inst_str:
                    inst_code[len(inst_str)-1-i] = int(digit)
                    i += 1
                if inst_code[2] == 0:
                    first_arg = ops[ops[pos+1]]
                else:
                    first_arg = ops[pos+1]
                if inst_code[3] == 0:
                    second_arg = ops[ops[pos+2]]
                else:
                    second_arg = ops[pos+2]
                if inst_code[0] == 1:
                    # sum
                    ops[ops[pos+3]] = first_arg + second_arg
                    pos += 4
                elif inst_code[0] == 2:
                    # multiply
                    ops[ops[pos+3]] = first_arg * second_arg
                    pos += 4
                elif inst_code[0] == 5:
                    # jump if true
                    if first_arg != 0:
                        pos = second_arg
                    else:
                        pos += 3
                elif inst_code[0] == 6:
                    # jump if false
                    if first_arg == 0:
                        pos = second_arg
                    else:
                        pos += 3
                elif inst_code[0] == 7:
                    # less than
                    if first_arg < second_arg:
                        ops[ops[pos+3]] = 1
                    else:
                        ops[ops[pos+3]] = 0
                    pos += 4
                elif inst_code[0] == 8:
                    # equals
                    if first_arg == second_arg:
                        ops[ops[pos+3]] = 1
                    else:
                        ops[ops[pos+3]] = 0
                    pos += 4
        return outputs


print(first_task('day05.txt', 5))
