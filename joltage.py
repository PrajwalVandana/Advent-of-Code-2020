memo = {}

# way 1: recursive function w/ memoization
def ways(main_lst, idx):
    global memo

    lst = main_lst[idx:]
    if len(lst) == 1:
        return 1
    elif idx in memo:
        return memo[idx]
    else:
        next_indexes = []
        i = 1
        while i in range(len(lst)) and lst[i]-lst[0] <= 3:
            next_indexes.append(i)
            i += 1

        res = 0
        for i in next_indexes:
            res += ways(main_lst, i+idx)

        memo[idx] = res
        return res


with open('/users/sysadmin/Documents/Prajwal/Programming/Competitions/Advent of Code/input.txt') as fin:
    finished = False
    joltages = [0]
    mx_jolts = 0
    while not finished:
        line = fin.readline().strip()
        if not line:
            finished = True
        else:
            num = int(line)
            joltages.append(num)
            mx_jolts = max(mx_jolts, num)

    joltages.append(mx_jolts+3)
    joltages.sort()

    # way 2: fill up a list with number of ways for each i,
    #        using a recursive rule
    #        (credit to some dude on r/adventofcode)
    ways_list = [1]+[0]*joltages[-1]
    for i in joltages[1:]:
        ways_list[i] = ways_list[i-1] + ways_list[i-2] + ways_list[i-3]

    print(ways_list[-1])

    print(ways(joltages, 0))
