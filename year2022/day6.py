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

            print(result1, result2)



    return (result1, result2)

