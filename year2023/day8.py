debug = False

from utils import dprint, warn
from collections import defaultdict
from pprint import pprint
# from math import lcm
import copy
import math



def solution(sections):

    # dprint(f'{file=}')

    result1 = result2 = 0

    directions = sections[0][0]

    lines = sections[1]

    # AAA = (BBB, CCC)
    # paths['AAA'] = ('BBB', 'CCC')

    paths = dict()
    for line in lines:
        node, _, left, right = line.split()
        left = left.strip('(,)')
        right = right.strip('(,)')
        paths[node] = (left, right)

    # Part1
    position = 'AAA'
    di = 0
    while position != 'ZZZ':
        if directions[di] == 'L':
            position = paths[position][0]
        else:
            position = paths[position][1]
        result1 += 1
        di += 1
        if di == len(directions):
            di = 0


    # Part2
    positions = []
    for node in paths.keys():
        if node[-1] == 'A':
            positions.append(node)


    dprint(f'{len(positions)=}')

    path_lengths = dict()

    done = False

    di = 0
    while not done:
        done = True
        for pj in range(len(positions)):
            position = positions[pj]

            if directions[di] == 'L':
                position = paths[position][0]
            else:
                position = paths[position][1]

            if position[-1] == 'Z' and pj not in path_lengths:
                path_lengths[pj] = result2 + 1

            done &= bool(position[-1] == 'Z')

            positions[pj] = position
        result2 += 1
        di += 1
        if di == len(directions):
            di = 0

        if len(path_lengths) == len(positions):
            dprint(f'{path_lengths=}')
            lcm = math.lcm(*path_lengths.values())
            dprint(f'{lcm=}')
            result2 = lcm
            done = True





    return (result1, result2)
