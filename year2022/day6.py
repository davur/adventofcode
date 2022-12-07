debug = False

from .utils import *


def ints(nums):
    return [int(num) for num in nums]

def solution(file):

    result1 = 0
    result2 = 0

    sections = read(file)

    for section in sections:
        rows = section

        for row in rows:
            row = row.strip()

            tok = ''
            i = -1

            for i in range(0, len(row)-3):
                tok = row[i:i+4]
                chars = set(tok)
                if len(chars) == 4:
                    break

            result1 = i+4

            for i in range(0, len(row)-13):
                tok = row[i:i+14]
                chars = set(tok)
                if len(chars) == 14:
                    break

            result2 = i+14

            ### One-liner version for fun
            # result1 = [i for i in range(3, len(line)) if len(set(line[i-4:i]))==4][0]
            # result2 = [i for i in range(13, len(line)) if len(set(line[i-14:i]))==14][0]
            # # ^ Does the same as lines 20-40

            print(result1, result2)



    return (result1, result2)

