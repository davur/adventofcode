debug = False

from utils import dprint, warn
from collections import defaultdict
from pprint import pprint
import copy


def solution(sections):

    # dprint(f'{file=}')

    result1 = result2 = 0

    lines = sections[0]

    for line in lines:
        history = [int(n) for n in line.split()]
        dprint(f'{history}')

        prev = history
        seqs = [history]
        done = False
        while not done:
            seq = []

            done = True
            for i in range(len(prev)-1):
                v = prev[i+1] - prev[i]
                done &= (v == 0)
                seq.append(v)

            seqs.append(seq)
            prev = seq

            dprint(f'{seq}')

        dprint(f'{seqs}')

        seqs[-1].insert(0, 0)
        seqs[-1].append(0)
        v = 0
        for j in range(-2, 0-1-len(seqs), -1):
            rightv = seqs[j][-1] + seqs[j+1][-1]
            leftv = seqs[j][0] - seqs[j+1][0]

            seqs[j].append(rightv)
            seqs[j].insert(0, leftv)

        result1 += rightv
        result2 += leftv
        dprint(f'{seqs}')







    return (result1, result2)
