debug = False

from utils import dprint, warn, char_grid_from_lines
from collections import defaultdict
from pprint import pprint
import copy


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
                grid[r][c] = 0
                break


    # visited = [{pos[1]}, set(), set(), set()]

    dir = 0
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    result1 = 1

    while (0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])):
        # print(f"{pos=}")

        next_pos = (pos[0] + dirs[dir][0], pos[1] + dirs[dir][1])
        if not (0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0])):
            # print(f"{next_pos=}")
            break

        if grid[next_pos[0]][next_pos[1]] == '#':
            dir = dir + 1 if dir < 3 else 0
        else:
            if check_right(grid, pos, dir + 1 if dir < 3 else 0, dirs):
                result2 += 1

            pos = next_pos

            c = grid[pos[0]][pos[1]]

            if c == '.':
                result1 += 1

#             if (c == (dir + 1 if dir < 3 else 0)):
#                 result2 += 1
#                 print(f"o at {pos=}")

            grid[pos[0]][pos[1]] = dir

    # submitted P1: 4662 (Answer is too low)
    # submitted P2: 338 (Answer is too low)



    return (result1, result2)

def check_right(grid, pos, dir, dirs):

    while True:
        pos = (pos[0] + dirs[dir][0], pos[1] + dirs[dir][1])
        if not (0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])):
            return False
        c = grid[pos[0]][pos[1]]
        if c == dir:
            return True
        if c == '#':
            return False
