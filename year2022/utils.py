debug = True

from pprint import pprint

def dprint(*args):
    if debug:
        pprint(*args)
    pprint(*args)

def ints(nums):
    return [int(num) for num in nums]

def rotate(grid):
    rotated = list(zip(*grid[::-1]))
    return rotated

def read(file):
    sections = []

    section = []

    lines = []
    with open(file, 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            lines.append(line.rstrip("\n"))

    for line in lines:
        if line:
            section.append(line)
        else:
            sections.append(section)
            section = []
    sections.append(section)

    return sections
    

