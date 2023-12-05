debug = False

from utils import dprint, warn
from collections import defaultdict
from pprint import pprint
import copy


def solution(sections):

    # dprint(f'{file=}')

    result1 = result2 = 0

    seeds = [int(s) for s in sections[0][0].split(':')[1].split() if s.isdigit()]
    seeds.sort()
    dprint(f'{seeds}')

    lines = sections.pop(0)
    # dprint(lines)

    maps = []

    for lines in sections:
        dprint(lines[0])

        mappings = []
        for i in range(1, len(lines)):
            nums = lines[i].split()
            dst_start = int(nums[0])
            src_start = int(nums[1])
            range_len = int(nums[2])

            r = (src_start, src_start + range_len, 0 - (src_start - dst_start))
            # dprint(f'{r=}')
            mappings.append(r)

        dprint(f'{seeds=}')
        mappings.sort()
        dprint(f'{mappings=}')

        for i in range(len(seeds)):
            seed = seeds[i]
            dprint(f'{seed=}')

            for mapping in mappings:
                dprint(f'{mapping=}')
                if mapping[0] <= seed <= mapping[1]:
                    seed += mapping[2]
                    seeds[i] = seed
                    break


        dprint(f'{seeds=}')


    result1 = min(seeds)



    return (result1, result2)
