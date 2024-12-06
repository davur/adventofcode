debug = False

from utils import dprint, warn
from collections import defaultdict
from pprint import pprint
import copy


def solution(sections):

    # dprint(f'{file=}')

    result1 = result2 = 0

    rules = sections[0]

    page_lists = sections[1]

    # 47|53
    print(rules)
    print(page_lists)

    after = {}
    before = {}

    for rule in rules:
        a, b = [int(i) for i in rule.split('|')]

        if a not in after:
            after[a] = set()
        after[a] |= {b}

        if b not in before:
            before[b] = set()
        before[b] |= {a}


    invalid = []

    # P1
    for page_list in page_lists:
        page_list = [int(i) for i in page_list.split(',')]

        print(f"{page_list=}")
        valid = is_valid(page_list, before, after)

        if valid:
            mid = page_list[len(page_list)//2]
            result1 += mid
        else:
            invalid.append(page_list)

    # P2

    for k in after:
        after_k = after[k]

        for v in after_k:
            if v not in before:
                before[v] = {k}
            else:
                before[v] |= {k}


    for page_list in invalid:
        page_list = fix(page_list, before)
        mid = page_list[len(page_list)//2]
        result2 += mid


    return (result1, result2)


def is_valid(page_list, before, after):
    for i in range(1, len(page_list)):
        cur = page_list[i]
        pre = page_list[:i]
        post = page_list[i:]

        for p in pre:
            if p in before and cur in before[p]:
                return False

        for p in post:
            if p in after and cur in after[p]:
                return False

    return True


def fix(page_list, before):
    new_page_list = []

    while len(page_list):
        i = 0
        while i < len(page_list):
            p1 = page_list[i]

            is_lowest = True
            for j in range(len(page_list)):
                if i == j:
                    continue
                p2 = page_list[j]

                if p1 in before and p2 in before[p1]:
                    is_lowest = False

            if is_lowest:
                page_list.pop(i)
                new_page_list.append(p1)
                break

            i += 1

    return new_page_list

