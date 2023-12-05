debug = False

from utils import dprint, warn
from collections import defaultdict
from pprint import pprint
import copy


def solution(sections):

    # dprint(f'{file=}')

    result1 = result2 = 0

    # Part 1
    seeds = [int(s) for s in sections[0][0].split(':')[1].split() if s.isdigit()]
    seeds.sort()
    dprint(f'{seeds=}')

    # Part 2
    seeds2 = []
    seed_numbers = [int(s) for s in sections[0][0].split(':')[1].split() if s.isdigit()]
    while len(seed_numbers):
        seeds_start = seed_numbers.pop(0)
        seeds_len = seed_numbers.pop(0)

        for i in range(seeds_len):
            seeds2.append(seeds_start + i)
    dprint(f'{seeds2=}')
    print(len(seeds2))

    maps = []

    for sec in range(1, len(sections)):
        lines = sections[sec]
        print(lines[0])

        mappings = []
        for i in range(1, len(lines)):
            nums = lines[i].split()
            dst_start = int(nums[0])
            src_start = int(nums[1])
            range_len = int(nums[2])

            r = (src_start, src_start + range_len, 0 - (src_start - dst_start))
            # dprint(f'{r=}')
            mappings.append(r)

        # dprint(f'{seeds=}')
        mappings.sort()
        # dprint(f'{mappings=}')

        # Part 1
        for i in range(len(seeds)):
            seed = seeds[i]
            # dprint(f'{seed=}')

            for mapping in mappings:
                # dprint(f'{mapping=}')
                if mapping[0] <= seed < mapping[1]:
                    seed += mapping[2]
                    seeds[i] = seed
                    break

        # Part 2
        # dprint(f'{seeds2=}')
        for i in range(len(seeds2)):
            seed = seeds2[i]

            for mapping in mappings:
                if mapping[0] <= seed < mapping[1]:
                    seed += mapping[2]
                    seeds2[i] = seed
                    break

        # seeds2.sort()


        dprint(f'{mappings=}')
        dprint(f'{seeds2=}')


    result1 = min(seeds)
    result2 = min(seeds2)

    return (result1, result2)
