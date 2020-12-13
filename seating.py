def num_adj(r, c):
    res = 0
    for r_diff in range(-1, 2):
        for c_diff in range(-1, 2):
            if r+r_diff in range(len(grid)) and c+c_diff in range(len(grid[0])):
                res += prev_grid[r+r_diff][c+c_diff] == '#'
    return res - (grid[r][c] == '#')


def num_visible(r, c):
    res = 0
    r_orig, c_orig = r, c

    r -= 1
    c -= 1
    finished = False
    while r in range(len(grid)) and c in range(len(grid[r])) and not finished:  # TL
        if prev_grid[r][c] != '.':
            res += prev_grid[r][c] == '#'
            finished = True
        r -= 1
        c -= 1
    r, c = r_orig, c_orig

    r -= 1
    c += 1
    finished = False
    while r in range(len(grid)) and c in range(len(grid[r])) and not finished:  # TR
        if prev_grid[r][c] != '.':
            res += prev_grid[r][c] == '#'
            finished = True
        r -= 1
        c += 1
    r, c = r_orig, c_orig

    r += 1
    c -= 1
    finished = False
    while r in range(len(grid)) and c in range(len(grid[r])) and not finished:  # BL
        if prev_grid[r][c] != '.':
            res += prev_grid[r][c] == '#'
            finished = True
        r += 1
        c -= 1
    r, c = r_orig, c_orig

    r += 1
    c += 1
    finished = False
    while r in range(len(grid)) and c in range(len(grid[r])) and not finished:  # BR
        if prev_grid[r][c] != '.':
            res += prev_grid[r][c] == '#'
            finished = True
        r += 1
        c += 1
    r, c = r_orig, c_orig

    r -= 1
    finished = False
    while r in range(len(grid)) and c in range(len(grid[r])) and not finished:  # U
        if prev_grid[r][c] != '.':
            res += prev_grid[r][c] == '#'
            finished = True
        r -= 1
    r = r_orig

    r += 1
    finished = False
    while r in range(len(grid)) and c in range(len(grid[r])) and not finished:  # D
        if prev_grid[r][c] != '.':
            res += prev_grid[r][c] == '#'
            finished = True
        r += 1
    r = r_orig

    c -= 1
    finished = False
    while r in range(len(grid)) and c in range(len(grid[r])) and not finished:  # L
        if prev_grid[r][c] != '.':
            res += prev_grid[r][c] == '#'
            finished = True
        c -= 1
    c = c_orig

    c += 1
    finished = False
    while r in range(len(grid)) and c in range(len(grid[r])) and not finished:  # R
        if prev_grid[r][c] != '.':
            res += prev_grid[r][c] == '#'
            finished = True
        c += 1
    c = c_orig

    return res


with open('/users/sysadmin/Documents/Prajwal/Programming/Competitions/Advent of Code/input.txt') as fin:
    finished = False
    grid = []
    while not finished:
        line = fin.readline().strip()
        if not line:
            finished = True
        else:
            grid.append(list(line))

    finished = False
    prev_grid = [row[:] for row in grid]
    while not finished:
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 'L' and not num_visible(r, c):
                    grid[r][c] = '#'
                elif grid[r][c] == '#' and num_visible(r, c) >= 5:
                    grid[r][c] = 'L'

        finished = grid == prev_grid
        prev_grid = [row[:] for row in grid]

    res = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            res += grid[r][c] == '#'

    print(res)
