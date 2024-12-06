debug = False

from utils import dprint, warn, char_grid_from_lines
from collections import defaultdict
from pprint import pprint
import copy


def solution(sections):

    # dprint(f'{file=}')

    result1 = result2 = 0

    grid = char_grid_from_lines(sections[0])

    result1 = len(find_all(grid, 'XMAS'))

    result2 = len(find_xmas(grid))

    return (result1, result2)


def find_all(grid, word):

    l = len(word)
    matches = []

    firsts = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == word[0]:
                firsts.append([r, c])
    dprint(firsts)

    directions = []
    for ri in [-1, 0, 1]:
        for ci in [-1, 0, 1]:
            if ci == ri == 0:
                continue
            directions.append([ri, ci])
    dprint(directions)

    for start in firsts:
        sr, sc = start


        for d in directions:
            dr, dc = d

            er = sr + (l-1) * dr
            ec = sc + (l-1) * dc

            is_match = True

            if not (0 <= er < len(grid) and 0 <= ec < len(grid[0])):
                is_match = False
                continue

            for i in range(l):
                if grid[sr + i * dr][sc + i * dc] != word[i]:
                    is_match = False
                    break

            if is_match:
                matches.append([start, d])


    return matches


def find_xmas(grid):

    word = 'MAS'
    l = len(word)
    matches = []

    firsts = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == word[l//2]:
                firsts.append([r, c])
    dprint(firsts)

    for start in firsts:
        sr, sc = start

        if not (1 <= sr < len(grid) - 1 and 1 <= sc < len(grid[0]) - 1):
            continue

        nw = grid[sr - 1][sc - 1]
        se = grid[sr + 1][sc + 1]

        ne = grid[sr - 1][sc + 1]
        sw = grid[sr + 1][sc - 1]

        corners = set([nw, se, ne, sw])
        allowed = set([word[0], word[-1]])

        if corners == allowed and nw != se and ne != sw:
            matches.append(start)

    # matches < 2043

    return matches

