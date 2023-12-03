debug = False

from utils import dprint, warn
from collections import defaultdict
from pprint import pprint
import copy


def solution(sections):

    # dprint(f'{file=}')

    result1 = result2 = 0

    grid = sections[0]
    # dprint(lines)


    directions = []
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if not (x == 0 and y == 0):
                directions.append((x, y))
    dprint(f'{directions=}')

    for row in range(len(grid)):
        grid[row] = list(grid[row])

    dprint(f'{grid=}')

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            c = grid[row][col]
            if c in '.X' or c.isdigit():
                continue
            dprint(f'{c=}')

            part_numbers = []

            for direction in directions:
                rd, cd = direction
                ri, ci = row + rd, col + cd

                val = 0

                if ri >= 0 and ri < len(grid) and ci >= 0 and ci < len(grid[ri]):
                    first = ci
                    if grid[ri][ci].isdigit():
                        while first - 1 >= 0 and grid[ri][first - 1].isdigit():
                            first = first - 1

                        last = first
                        while last < len(grid[ri]) and grid[ri][last].isdigit():
                            last += 1

                        val = int("".join(grid[ri][first:last]))
                        part_numbers.append(val)
                        dprint(f'{direction=} {val=}')
                        for cj in range(first, last):
                            grid[ri][cj] = 'X'

                        result1 += val

            if c == '*' and len(part_numbers) == 2:
                gear_ratio = part_numbers[0] * part_numbers[1]
                dprint(f'{gear_ratio=}')
                result2 += gear_ratio


    # for line in lines



    return (result1, result2)
