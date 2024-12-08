from utils import dprint, warn
from collections import defaultdict
from pprint import pprint
import copy


def solution(sections):

    result1 = result2 = 0

    lines = sections[0]

    left = []
    right = []

    for line in lines:
        leftval, rightval = line.split()
        left.append(int(leftval))
        right.append(int(rightval))

    left.sort()
    right.sort()

    for i in range(len(left)):
        l = left[i]
        r = right[i]
        distance = l - r if l > r else r - l
        result1 += distance

    counts = {}

    for r in right:
        if r in counts:
            counts[r] += 1
        else:
            counts[r] = 1

    for i in range(len(left)):
        l = left[i]
        if l in counts:
            count = counts[l] * l
            result2 += count

    return (result1, result2)

