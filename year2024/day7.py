debug = False

from utils import dprint, warn, char_grid_from_lines, number_to_base
from collections import defaultdict
from pprint import pprint
import copy


def solution(sections):

    result1 = result2 = 0

    lines = sections[0]

    MUL = '*'
    ADD = '+'

    operators = [MUL, ADD]

    for l, line in enumerate(lines):
        result, equation = line.split(':')
        result = int(result)
        numbers = [int(i) for i in equation.strip().split(' ')]

        print(f"{l}: {line}")
        # print(f'{result=}')
        # print(f'{numbers=}')
        # do the thing

        # numbers=[9, 7, 18, 13]
        # result=292
        if check_solution_p1(result, numbers):
            result1 += result

        if check_solution_p2(result, numbers):
            result2 += result

    return (result1, result2)



def check_solution_p1(result, numbers):

    for i in range(1<<(len(numbers)-1)):

        res = numbers[0]

        for j in range(1, len(numbers)):

            if (1<<(j-1)) & i:
                res *= numbers[j]
            else:
                res += numbers[j]

        if res == result:
            return True

    return False

def check_solution_p2(result, numbers):

    ADD = 0
    MUL = 1
    CAT = 2

    for i in range(3**(len(numbers)-1)):
        base3 = number_to_base(i, 3)

        padding = [0] * (len(numbers) - 1 - len(base3))

        base3 = padding + base3

        res = numbers[0]

        for j in range(1, len(numbers)):

            operator = base3[j - 1]

            if operator == ADD:
                res += numbers[j]
            elif operator == MUL:
                res *= numbers[j]
            else:
                res = int(str(res) + str(numbers[j]))

            if res > result:
                break

        if res == result:
            return True

    return False
