from collections import defaultdict

def neighbors(point):
    x, y, z, w = point

    res = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if not (i == j == k == l == 0):
                        res.append((x+i, y+j, z+k, w+l))

    return res


with open('/users/sysadmin/Documents/Prajwal/Programming/Competitions/Advent of Code/input.txt') as fin:
    finished = False
    points = defaultdict(lambda: False)
    line_num = 0
    while not finished:
        line = fin.readline().strip()
        if not line:
            finished = True
        else:
            lst = list(line)
            for i in range(len(lst)):
                point = i, line_num, 0, 0
                points[point] = lst[i] == '#'
                # all the points that could possibly be affected in
                # the first cyle are added
                for neighbor in neighbors(point):
                    points[neighbor]

            line_num += 1

    for _ in range(6):
        cur_points = list(points.keys())
        switches = []
        for point in cur_points:
            active_neighbors = sum((points[neighbor]
                                    for neighbor in neighbors(point)))
            if points[point] and active_neighbors not in {2, 3}:
                switches.append(point)
            elif not points[point] and active_neighbors == 3:
                switches.append(point)

        for switch in switches:
            points[switch] = not points[switch]

    res = 0
    for state in points.values():
        res += state

    print(res)
