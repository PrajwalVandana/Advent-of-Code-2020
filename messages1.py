memo = {}
def matching(rule_num):
    global memo

    if rule_num not in memo:
        rule = rules[rule_num]

        if type(rule) == str:
            res = {rule}
        elif type(rule) == tuple:
            if len(rule) == 1:
                res = matching(rule[0])
            else:
                res = set()
                r1, r2 = rule
                for start in matching(r1):
                    for end in matching(r2):
                        res.add(start+end)
        else:
            r1, r2 = tuple(rule)
            if len(r1) == 1:
                res = matching(r1[0]) | matching(r2[0])
            else:
                res = set()
                for start in matching(r1[0]):
                    for end in matching(r1[1]):
                        res.add(start+end)

                temp = set()
                for start in matching(r2[0]):
                    for end in matching(r2[1]):
                        temp.add(start+end)

                res |= temp

        memo[rule_num] = res

    return memo[rule_num]


with open('/users/sysadmin/Documents/Prajwal/Programming/Competitions/Advent of Code/input.txt') as fin:
    finished = False
    rules = {}
    while not finished:
        line = fin.readline().strip()
        if not line:
            finished = True
        else:
            num, rule = line.split(': ')
            num = int(num)
            if '|' in rule:
                rule = rule.split(' | ')
                rule = set(map(lambda x: tuple(map(int, x.split())), rule))
            elif '"' in rule:
                rule = rule[1]
            else:
                rule = tuple(map(int, rule.split()))

            rules[num] = rule


    poss = matching(0)
    res = 0
    finished = False
    while not finished:
        word = fin.readline().strip()
        if not word:
            finished = True
        else:
            res += word in poss

    print(res)
