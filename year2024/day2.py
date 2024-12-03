debug = False

from utils import dprint, warn
from collections import defaultdict
from pprint import pprint
import copy


def solution(sections):

    # dprint(f'{file=}')

    result1 = result2 = 0

    lines = sections[0]

    for report in lines:
        print(f"{report=}")

        levels = [int(l) for l in report.split()]

        if is_safe(levels):
            result1 += 1

        safe = is_safe(levels, 1)

        for i in range(0, len(levels)):
            if safe:
                break

            new_levels = levels[0:i]
            if i < len(levels):
                new_levels += levels[i+1:]

            safe = is_safe(new_levels)
            if safe:
                break


        print(f"{safe=}")
        if safe:
            result2 += 1

        # Tried: 586



    return (result1, result2)



def is_safe(levels, tolerance=0):
    if len(levels) < 2:
        print("<2")
        return True

    # If increasing
    if levels[0] < levels[1]:
        print("Increasing")
        start = 0
        end = len(levels)
        step = 1

    elif levels[0] > levels[1]:
        start = len(levels) - 1
        end = -1
        step = -1
        print("Decreasing")

    else:
        return False

    previous = levels[start]

    print([start, end, step])

    for i in range(start + step, end, step):

        current = levels[i]
        diff = current - previous

        print([current, diff])
        if diff <= 0 or diff > 3:
            if tolerance > 0:
                tolerance -= 1
                continue
            else:
                print("False")
                return False

        previous = current

    return True



