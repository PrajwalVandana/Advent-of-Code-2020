memo = {}


def matching(word, rule):
    global memo

    if (word, rule) not in memo:
        word_len = len(word)

        if rule == frozenset({(42,), (42, 8)}):
            if word_len % 8:
                res = False
            else:
                res = True
                for i in range(0, word_len, 8):
                    if not matching(word[i:i+8], rules[42]):
                        res = False
                        break
        elif rule == frozenset({(42, 31), (42, 11, 31)}):
            if word_len % 8:
                res = False
            else:
                res = True
                for i in range(0, word_len//2, 8):
                    if not matching(word[i:i+8], rules[42]):
                        res = False
                        break
                if res:
                    for i in range(word_len//2, word_len, 8):
                        if not matching(word[i:i+8], rules[31]):
                            res = False
                            break
        else:
            if type(rule) == str:
                res = word == rule
            elif type(rule) == tuple:
                if len(rule) == 1:
                    res = matching(word, rules[rule[0]])
                else:
                    r1, r2 = rules[rule[0]], rules[rule[1]]
                    res = False
                    for i in range(1, len(word)):
                        if matching(word[:i], r1) and matching(word[i:], r2):
                            res = True
                            break
            else:
                res = False
                for r in rule:
                    if matching(word, r):
                        res = True
                        break

        memo[word, rule] = res

    return memo[word, rule]


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
            if num == 8:
                rule = '42 | 42 8'
            elif num == 11:
                rule = '42 31 | 42 11 31'

            if '|' in rule:
                rule = rule.split(' | ')
                rule = frozenset(
                    map(lambda x: tuple(map(int, x.split())), rule))
            elif '"' in rule:
                rule = rule[1]
            else:
                rule = tuple(map(int, rule.split()))

            rules[num] = rule

    main_rule = rules[0]
    res = 0
    finished = False
    while not finished:
        word = fin.readline().strip()
        if not word:
            finished = True
        else:
            res += matching(word, main_rule)

    print(res)
