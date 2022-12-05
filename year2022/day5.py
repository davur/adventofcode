debug = False

from .utils import *


def ints(nums):
    return [int(num) for num in nums]

def solution(file):

    sections = read(file)

    rows = sections[0][:-1]

    stacks1 = []
    stacks2 = []
    rotated = rotate(rows)
    for col in rotated:
        if col[0] in '[] ':
            continue
        stack = [c for c in col if c.strip()]
        stacks1.append(stack)
        stack = [c for c in col if c.strip()]
        stacks2.append(stack)

    result1 = 0
    result2 = 0

    for line in sections[1]:
        _, quantity, _, fro, _, to = line.split()
        quantity, fro, to = ints([quantity, fro, to])

        # Part 1
        for j in range(quantity):
            crate = stacks1[fro-1].pop()
            stacks1[to-1].append(crate)

        # Part 2
        for j in range(quantity):
            crate = stacks2[fro-1][0 - quantity + j]
            stacks2[to-1].append(crate)
        for j in range(quantity):
            stacks2[fro-1].pop()

    tops1 = []
    for stack in stacks1:
        if stack:
            tops1.append(stack[-1])
    result1 = ''.join(tops1)

    tops2 = []
    for stack in stacks2:
        if stack:
            tops2.append(stack[-1])
    result2 = ''.join(tops2)

    return (result1, result2)

