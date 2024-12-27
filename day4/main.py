DIRS = [(1,0), (0,1), (-1, 0), (0, -1), (1, 1), (1,-1), (-1, 1), (-1, -1)]
XMAS = 'XMAS'


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    times = 0
    for i, line in enumerate(lines):
        for j, char in enumerate(line): 
            if char != 'X': 
                continue
            for d in DIRS:
                print("checking dir", d)
                found = check_xmas(i, j, 1, lines, d) 
                if found:
                    times += 1
    print(times)


def check_xmas(i, j, next_index, lines, direction):
    next_i, next_j = i + direction[0], j + direction[1]
    if next_index == len(XMAS):
        return False
    if next_i < 0 or next_i == len(lines):
        return False
    if next_j < 0 or next_j == len(lines[0]):
        return False

    print(f"char={lines[next_i][next_j]}, next_i={next_i}, next_j={next_j}, next_index={next_index}, XMAS_C={XMAS[next_index]}")
    if lines[next_i][next_j] != XMAS[next_index]:
        return False

    # end of XMAS
    if next_index == 3:
        print(f"found XMAS at {i}, {j}")
        return True

    return check_xmas(next_i, next_j, next_index+1, lines, direction)


main()
