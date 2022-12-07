debug = False

from .utils import *
from collections import defaultdict
from pprint import pprint


def ints(nums):
    return [int(num) for num in nums]






def directory_stack_to_path(cur):
    #cur = ['a', 'e', 'd']
    #path = '/a/e/d/'

    if len(cur) == 0:
        return "/"
    else:
        return "/%s/" % ("/".join(cur))


def solution(file):

    result1 = 0
    result2 = 0

    sections = read(file)
    rows = sections[0]
    
    cur = []
    cur_path = None
    dirsizes = defaultdict(int)
    # = {
    #   '/': 23352670, 
    #   '/a/': 94269, 
    #   '/a/e/': 584, 
    #   '/d/': 24933642,
    # }

    for line in rows:
        if line[0] == '$':
            commands = line.split()
            # $ cd /
            # $ cd blarg
            # $ ls

            if commands[1] == 'cd':
                if commands[2] == '..':
                    cur.pop()
                elif commands[2] == '/':
                    cur = []
                else: # $ cd tmp
                    cur.append(commands[2])
                cur_path = directory_stack_to_path(cur)

            elif commands[1] == 'ls':
                path = directory_stack_to_path(cur)
                dirsizes[path] = 0
                
        else:
            first, second = line.split()
            if first == 'dir':
                continue
            else:
                dirsizes[cur_path] += int(first)

    dirsizes_list = [(path, dirsizes[path]) for path in dirsizes]
    dirsizes_list.sort()

    total_dirsizes = []
    
    for i in range(len(dirsizes_list)):
        path, dirsize = dirsizes_list[i]
        total_dirsize = dirsize
        j = i + 1
        while j < len(dirsizes_list) and dirsizes_list[j][0].startswith(path):
            total_dirsize += dirsizes_list[j][1]
            j += 1

        total_dirsizes.append((total_dirsize, path))


    total_dirsizes.sort()

    # Part 1:
    result1 = 0
    for i in range(len(total_dirsizes)):
        dirsize = total_dirsizes[i][0]
        if dirsize < 100000:
            result1 += dirsize

    total_size = total_dirsizes[-1][0]
    disk_size = 70000000
    size_required = 30000000
    to_delete = size_required - (disk_size - total_size)

    for i in range(len(total_dirsizes)):
        dirsize = total_dirsizes[i][0]
        if dirsize > to_delete:
            result2 = dirsize
            break

    return (result1, result2)


