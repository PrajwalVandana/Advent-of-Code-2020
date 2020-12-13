def run(operation):
    global res, op_num

    if operation[0] == 'acc':
        res += operation[1]
    elif operation[0] == 'jmp':
        op_num += operation[1] - 1
    op_num += 1


def switch(instruction):
    return 'jmp' if instruction == 'nop' else 'nop'


with open('/users/sysadmin/Documents/Prajwal/Programming/Python/Competitions/Advent of Code/input.txt') as fin:
    finished = False
    operations = []
    while not finished:
        line = fin.readline().strip()
        if not line:
            finished = True
        else:
            operations.append((line[:3], int(line[4:])))

    finished = False
    i = 0
    while i in range(len(operations)) and not finished:
        if operations[i][0] != 'acc':
            operations[i] = switch(operations[i][0]), operations[i][1]
            res = 0
            op_num = 0
            seen_op_nums = set()
            run_finished = False
            while not run_finished:
                run(operations[op_num])
                if op_num in seen_op_nums:
                    run_finished = True
                elif op_num >= len(operations):
                    run_finished = True
                    finished = True
                else:
                    seen_op_nums.add(op_num)

            operations[i] = switch(operations[i][0]), operations[i][1]
        i += 1

    print(res)
