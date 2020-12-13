class Rules:
    def __init__(self):
        self.data = {}

    def __setitem__(self, i, val):
        self.data[i] = val

    def __getitem__(self, i):
        res = {ele[1] for ele in self.data[i]}
        for _, col in self.data[i]:
            res |= self[col]
        return res

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return repr(self.data)

    def __iter__(self):
        return iter(self.data)

    def __contains__(self, val):
        return val in self.data

    def count(self, i):
        return sum([ele[0]*(1 + self.count(ele[1])) for ele in self.data[i]])


with open('/users/sysadmin/Documents/Prajwal/Programming/Competitions/Advent of Code/input.txt') as fin:
    finished = False
    rules = Rules()
    while not finished:
        line = fin.readline().strip('.\n')
        if not line:
            finished = True
        else:
            bag, contents_str = tuple(line.split(' bags contain '))
            contents = set()
            if contents_str != 'no other bags':
                contents_list = contents_str.split(', ')
                for i in range(len(contents_list)):
                    num, colors = tuple(' '.join(contents_list[i].split()[:-1]).split(' ', 1))
                    contents.add((int(num), colors))

            rules[bag] = contents

    print(rules.count('shiny gold'))
