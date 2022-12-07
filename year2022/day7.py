debug = False

from .utils import *
from collections import defaultdict


def ints(nums):
    return [int(num) for num in nums]



def fullpath(arr, extra = ''):
    if extra:
        newarr = arr + [extra]
    else:
        newarr = arr

    if len(newarr) == 1:
        return '/'
    else:
        return '/'.join(newarr)

def solution(file):

    result1 = 0
    result2 = 0

    sections = read(file)

    dirs = {}

    dirsizes = defaultdict(int)

    cur = []

    for section in sections:
        rows = section

        for line in rows:

            if line[0] == '$':
                command = line[2:].split()

                if command[0] == 'cd':
                    if command[1] == '/':
                        cur = ['']
                        dirsizes[fullpath(cur)] += 0
                    elif command[1] == '..':
                        cur.pop()
                    else:
                        cur.append(command[1])
                        dirsizes[fullpath(cur)] += 0
                # ignore ls
            else:
                size, path = line.split()

                if size == 'dir':
                    dirsizes[fullpath(cur, path)] += 0
                else:
                    dirsizes[fullpath(cur)] += int(size)

        dirs = dirsizes.keys()
        print(dirs)

        dir_totals = []
        for dir in dirs:
            dir_total = sum([dirsizes[p] for p in dirsizes if p[:len(dir)] == dir])
            dir_totals.append((dir_total, dir))

        # Part 1
        result1 = 0
        for s, _ in dir_totals:
            if s <= 100000:
                result1 += s

        dir_totals.sort()
        total = dir_totals[-1][0]
        to_remove = 30000000-(70000000-total)



        # Part1
        for i in range(len(dir_totals)):
            s, p = dir_totals[i]
            if s >= to_remove: 
                result2 = s
                break

# tried 42536714
# tried 23754
# tried 2940614

    return (result1, result2)


