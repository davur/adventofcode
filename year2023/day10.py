debug = False

from utils import dprint, warn
from collections import defaultdict
from pprint import pprint
import copy


pretty = {
        'J': '┘',
        '7': '┐',
        'F': '┌',
        'L': '└',
        '|': '│',
        '-': '─',
    }


def print_grid(grid, start, positions=False):
    if not positions:
        positions = []
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            o = grid[r][c]
            if o == 'S':
                o = start
            if (r, c) in positions:
                p = pretty[o]
            else:
                p = '.'
            print(p, end='')
        print()


def move(pos, dir):
    return (pos[0] + dir[0], pos[1] + dir[1])


def get(grid, pos):
    # dprint(pos)
    r, c = pos
    v = '.'
    if 0 <= r < len(grid):
        if 0 <= c < len(grid[r]):
            v = grid[r][c]
    # dprint(v)
    return v


north = (-1, 0)
west = (0, -1)
east = (0, 1)
south = (1, 0)


# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
options = dict()
options['|'] = (north, south)
options['-'] = (east, west)
options['L'] = (north, east)
options['J'] = (north, west)
options['7'] = (south, west)
options['F'] = (south, east)


def solution(sections):
    # dprint(f'{file=}')

    grid = sections[0]

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'S':
                start = (row, col)
    # dprint(f'{start=}')

    done = False
    pos = start
    count = 0

    above = get(grid, move(pos, north))
    left = get(grid, move(pos, west))
    right = get(grid, move(pos, east))
    below = get(grid, move(pos, south))

    # dprint(f'.{above}.')
    # dprint(f'{left}S{right}')
    # dprint(f'.{below}.')

    if above in '|7F':
        if left in '-LF':
            cur = 'J'
        elif right in '-J7':
            cur = 'L'
        else:
            # down in '|LJ':
            cur = '|'
    elif right in '-J7':
        if left in '-LF':
            cur = '-'
        else:
            # down in '|LJ'
            cur = 'F'
    else:
        # down and left
        cur = '7'

    start_tile = cur
    # dprint(f'{start_tile=}')




    positions = [start]

    done = False
    prev = (-1, -1)

    while not done:
        # dprint(f'{pos=}')
        new_pos = move(pos, options[cur][0])
        if new_pos == prev:
            new_pos = move(pos, options[cur][1])
        prev = pos
        pos = new_pos
        positions.append(pos)
        count += 1
        cur = get(grid, pos)

        if pos == start:
            done = True

    result1 = count // 2

    # Part 2
    from matplotlib.path import Path
    path = Path(positions)

    result2 = 0

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if (r, c) in positions:
                continue

            contained = path.contains_point((r, c))
            if contained:
                result2 += 1
            dprint(f'({r},{c}): {contained}')


    # print_grid(grid, start_tile, positions)


    # Learning.  Matplotlib has a structure/function to check
    # if a point is contained in path

    return (result1, result2)
