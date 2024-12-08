debug = False

from utils import dprint, warn, char_grid_from_lines
from collections import defaultdict
from pprint import pprint
import copy



N = 1
E = 2
S = 4
W = 8

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def turn_right(dir):
    return dir + 1 if dir < 3 else 0

def forward(pos, dir):
    return (pos[0] + dirs[dir][0], pos[1] + dirs[dir][1])






def solution(sections):

    # dprint(f'{file=}')

    result1 = result2 = 0

    grid = char_grid_from_lines(sections[0])
    print(grid)

    pos = None

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '^':
                pos = (r, c)
                grid[r][c] = N
            elif grid[r][c] == '.':
                grid[r][c] = 0


    # visited = [{pos[1]}, set(), set(), set()]
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    dir = 0

    result1 = 1

    steps = 0

    next_pos = (pos[0] + dirs[dir][0], pos[1] + dirs[dir][1])
    while (0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0])):
        # print(f"{pos=}")
        steps += 1
        if steps % 100 == 0:
            print(f"{steps=}")

        if grid[next_pos[0]][next_pos[1]] == '#':
            dir = dir + 1 if dir < 3 else 0

        else:
            if grid[next_pos[0]][next_pos[1]] & dir == 0:
                if check_right(grid, pos, dir + 1 if dir < 3 else 0, dirs):
                    result2 += 1
                    print(f"o at {pos=}")
                    return (result1, result2)
            # print()

            pos = next_pos

            c = grid[pos[0]][pos[1]]

            if not c:
                result1 += 1

#             if (c == (dir + 1 if dir < 3 else 0)):
#                 result2 += 1
#                 # print(f"o at {pos=}")

        grid[pos[0]][pos[1]] |= 2**dir
        next_pos = (pos[0] + dirs[dir][0], pos[1] + dirs[dir][1])


        # for row in grid:
            # print("".join(str(c) for c in row))

        # input(":")


    # submitted P1: 4662 (Answer is too low)
    # submitted P2: 338 (Answer is too low)

    return (result1, result2)

def check_right(grid, pos, dir, dirs):
    visited = {}
    visited[pos] = 2**dir

    check = 0
    while True:
        check += 1
        # print(f"{check=}")
        next_pos = (pos[0] + dirs[dir][0], pos[1] + dirs[dir][1])
        if next_pos in visited and (visited[next_pos] | dir):
            return True

        if not (0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0])):
            return False
        c = grid[next_pos[0]][next_pos[1]]
        print(next_pos, end="")
        if c == '#':
            # print("")
            dir = dir + 1 if dir < 3 else 0
            continue

        amp = c & dir
        if c & (2**dir):
            # print("")
            # print(f"{c=},{dir=}")
            return True

        pos = next_pos
        if pos in visited:
            visited[pos] |= 2**dir
        else:
            visited[pos] = 2**dir
