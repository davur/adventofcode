debug = False

from utils import dprint, warn
from collections import defaultdict
from pprint import pprint
import copy


def solution(sections):

    # dprint(f'{file=}')

    result1 = result2 = 0

#     # Part 1
#     seeds = [int(s) for s in sections[0][0].split(':')[1].split() if s.isdigit()]
#     seeds.sort()
#     dprint(f'{seeds=}')

    # Part 2
    e2e_mappings = []
    seeds2 = []
    seed_numbers = [int(s) for s in sections[0][0].split(':')[1].split() if s.isdigit()]
    while len(seed_numbers):
        seeds_start = seed_numbers.pop(0)
        seeds_len = seed_numbers.pop(0)

        e2e_mappings.append((seeds_start, seeds_start + seeds_len, 0))

    e2e_mappings.sort()


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

            # 55-67
            # 79-92

        new_e2e_mappings = []

        mi = 0
        ei = 0
        mm = mappings[0]
        em = e2e_mappings[0]

        cursor = em[0]

        while cursor < e2e_mappings[-1][1]:

            for mm in mappings:
                if mm[1] <= cursor:
                    continue
                if mm[0] < cursor < mm[1]:
                    new_e2e_mappings

        while mi < len(mappings) or ei < len(e2e_mappings):
            # em      |       |
            # mm  |___|
            if mm[1] <= em[0]:
                mi += 1
                continue

            # em      |       |
            # mm  |   _____|
            if mm[0] < em[0] and mm[1] > em[0] and mm[1] < em[1]:
                new_e2e_mappings.append((em[0], mm[1], em[2] + mm[2]))
                e2e_mappings[ei][0] = mm[1]
                em = (
                mi += 1
                mm = mappings[mi]
                continue

            # em      |      |
            # mm   |            |





        for em in e2e_mappings:
            cursor = e2
            cursor = e2e_mappings[0][0]

        for m in mappings:
            if m[1] < cursor:
                continue
            if m[0] < cursor and



        new_e2e_mappings = []

        mi = 0
        ei = 0

        while mi < len(mappings) or ei < len(e2e_mappings):
            mm = mappings[mi]
            em = e2e_mappings[ei]


        cursor = e2e_mappings[0][0]


        for em in e2e_mappings:
            for m in mappings:



        if e2e_mappings[0][0] < mappings[0][0]:
            prefix = []
            for em in e2e_mappings:
                if em[1] < mappings[0][0]:
                    prefix.append((em[0], em[1], 0))
                elif em[0] < mappings[0][0]

                                    e2e_mappings[-1]

        mi = 0
        ei = 0

        while mi < len(mappings) or ei < len(e2e_mappings):
            mm = mappings[mi]
            em = e2e_mappings[ei]

            # em      |     |
            # mm |  |
            if mm[1] < em[0]:
                new_e2e_mappings.append(mm)

            # em      |     |
            # mm |    ____|
            elif mm[0] < em[0] and mm[1] >= em[0] and mm[1] < em[1]:
                new_e2e_mappings.append((mm[0], em[0], mm[2]))
                new_e2e_mappings.append((em[0], mm[1], em[2] + mm[2]))


            |     |
     |   1  2  3  4   5
            | 1   2   3
               |1 2   3
                  |

        new_e2e_mappings = []



        # dprint(f'{mappings=}')

#         # Part 1
#         for i in range(len(seeds)):
#             seed = seeds[i]
#             # dprint(f'{seed=}')
#
#             for mapping in mappings:
#                 # dprint(f'{mapping=}')
#                 if mapping[0] <= seed < mapping[1]:
#                     seed += mapping[2]
#                     seeds[i] = seed
#                     break

#         # Part 2
#         # dprint(f'{seeds2=}')
#         for i in range(len(seeds2)):
#             seed = seeds2[i]
#
#             for mapping in mappings:
#                 if mapping[0] <= seed < mapping[1]:
#                     seed += mapping[2]
#                     seeds2[i] = seed
#                     break

        # seeds2.sort()


        dprint(f'{mappings=}')
        dprint(f'{seeds2=}')


    result1 = min(seeds)
    result2 = min(seeds2)

    return (result1, result2)
