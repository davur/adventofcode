debug = False

from utils import dprint, warn
from collections import defaultdict
from pprint import pprint
import copy


def solution(sections):

    # dprint(f'{file=}')

    result1 = result2 = 1

    # Part 1
    lines = sections[0]

    times = [int(s) for s in lines[0].split(':')[1].split() if s.isdigit()]
    dists = [int(s) for s in lines[1].split(':')[1].split() if s.isdigit()]

    dprint(f'{times=}')
    dprint(f'{dists=}')

    for i in range(len(times)):
        time = times[i]
        dist = dists[i]

        count = 0

        for press in range(1, time):
            my_dist = press * (time - press)
            if my_dist > dist:
                count += 1

        result1 *= count

    times = [int("".join([str(t) for t in times]))]
    dists = [int("".join([str(d) for d in dists]))]
    dprint(f'{times=}')
    dprint(f'{dists=}')


    for i in range(len(times)):
        time = times[i]
        dist = dists[i]

        count = 0

        for press in range(1, time):
            my_dist = press * (time - press)
            if my_dist > dist:
                count += 1

        result2 *= count


    return (result1, result2)
