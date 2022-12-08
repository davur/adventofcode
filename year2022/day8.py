debug = False

from .utils import *
from collections import defaultdict
from pprint import pprint
import copy



def solution(file):

    result1 = 0
    result2 = 0

    sections = read(file)

    grid = sections[0]

    visibility = []

    for r in range(len(grid)):
        visibility.append([])
        for c in range(0, len(grid[r])):
            visibility[r].append(0)

    
    # for each row
    for r in range(len(grid)):
        visibility[r][0] = 1
        visibility[r][-1] = 1

        left = grid[r][0]
        for c in range(1, len(grid[r])-1):
            height = grid[r][c]
            if height > left:
                visibility[r][c] = 1
                left = height

        right = grid[r][-1]
        for c in range(len(grid[r])-1,0,-1):
            height = grid[r][c]
            if height > right:
                visibility[r][c] = 1
                right = height
        
    for c in range(len(grid[0])):
        visibility[0][c] = 1
        visibility[-1][c] = 1

        top = grid[0][c]
        for r in range(1, len(grid)-1):
            height = grid[r][c]
            if height > top:
                visibility[r][c] = 1
                top = height

        bottom = grid[-1][c]
        for r in range(len(grid)-1,0,-1):
            height = grid[r][c]
            if height > bottom:
                visibility[r][c] = 1
                bottom = height

    result1 = 0
    for r in range(len(grid)):
        result1 += sum([visibility[r][c] for c in range(len(grid[r]))])


    # Part 2
    cardinals = [(-1,0), (1,0), (0,-1), (0,1)]
    max_score = -1

    for r in range(len(grid)):  # [3]: #
        for c in range(len(grid[r])): # [2]: #
            score = 1
            for rd, cd in cardinals:
                ri, ci = r + rd, c + cd
                
                cardinal_score = 0
                while 0 <= ri < len(grid) and 0 <= ci < len(grid[ri]):
                    cardinal_score += 1
                    if grid[ri][ci] >= grid[r][c]:
                        break
                    ri, ci = ri + rd, ci + cd

                # print(rd, cd, cardinal_score)

                score *= cardinal_score

            if score > max_score:
                max_score = score

    result2 = max_score


    return (result1, result2)
