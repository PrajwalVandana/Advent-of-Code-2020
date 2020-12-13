def valid(passport):
    if 1920 <= int(passport['byr']) <= 2002:
        if 2010 <= int(passport['iyr']) <= 2020:
            if 2020 <= int(passport['eyr']) <= 2030:
                height = passport['hgt']
                if height[-2:] == 'cm':
                    lo = 150
                    hi = 193
                else:
                    lo = 59
                    hi = 76
                if len(height)> 3 and lo <= int(height[:-2]) <= hi:
                    hair_color = passport['hcl']
                    if hair_color[0] == '#' and len(hair_color) == 7:
                        if set(hair_color[1:]) <= {hex(num)[2:] for num in range(16)}:
                            eye_color = passport['ecl']
                            if eye_color in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
                                id_num = passport['pid']
                                if len(id_num) == 9 and set(id_num) <= {str(num) for num in range(10)}:
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


with open('/users/sysadmin/Documents/Prajwal/Programming/Python/Competitions/Advent of Code/input.txt') as fin:
    res = 0
    finished = False
    while not finished:
        blank_line_found = False
        passport = {}
        line_num = 0
        while not blank_line_found:
            line = fin.readline().split()
            if not line:
                finished = not line_num
                blank_line_found = True
            else:
                for pair_str in line:
                    pair = pair_str.split(':')
                    passport[pair[0]] = pair[1]
            line_num += 1

        if {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} <= set(passport):
            res += valid(passport)

    print(res)
