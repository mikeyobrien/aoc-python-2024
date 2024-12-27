DIRS = [(1,0), (0,1), (-1, 0), (0, -1), (1, 1), (1,-1), (-1, 1), (-1, -1)]
DIRS_PART2 = [[(1,-1), (-1, 1)], [(-1, -1), (1, 1)]]
XMAS = 'XMAS'


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    times = 0
    part2_times = 0
    for i, line in enumerate(lines):
        for j, char in enumerate(line): 
            if char == 'A':
                found_part2 = check_xmas2(i, j, lines)
                if found_part2:
                    part2_times += 1
            if char != 'X': 
                continue
            for d in DIRS:
                found = check_xmas(i, j, 1, lines, d) 
                if found:
                    times += 1
    print(times, part2_times)


def check_xmas(i, j, next_index, lines, direction):
    next_i, next_j = i + direction[0], j + direction[1]
    if next_index == len(XMAS):
        return False
    if next_i < 0 or next_i == len(lines):
        return False
    if next_j < 0 or next_j == len(lines[0]):
        return False
    if lines[next_i][next_j] != XMAS[next_index]:
        return False
    if next_index == 3:
        return True
    return check_xmas(next_i, next_j, next_index+1, lines, direction)

def check_bounds(i, j, lines):
    if i < 0 or i == len(lines):
        return False
    if j < 0 or j == len(lines[0]):
        return False
    return True


def check_xmas2(i, j, lines):
    valid = 0
    for dirs in DIRS_PART2:
        rem = 'MS'
        for next_dir in dirs:
            next_i, next_j = i + next_dir[0], j + next_dir[1]
            if not check_bounds(next_i, next_j, lines):
                break
            rem = rem.replace(lines[next_i][next_j], '')
        if rem == '':
            valid += 1
    return valid == 2


main()
