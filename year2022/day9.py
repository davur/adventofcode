debug = False

from .utils import *
from collections import defaultdict
from pprint import pprint
import copy



def solution(file):

    result1 = 0
    result2 = 0

    sections = read(file)

    h = [0,0]
    t = [0,0]

    dirs = {
        'R': (0,1),
        'U': (-1,0),
        'L': (0,-1),
        'D': (1,0),
    }

    for lines in sections:
        ts = {}
        ts[str(t)] = 1

        # Part1
        for line in lines:
            words = line.split()
            dir_char = words[0]
            distance = int(words[1])

            d = dirs[dir_char]
            
            for i in range(distance):
                h[0] = h[0] + d[0]
                h[1] = h[1] + d[1]

                if dir_char == 'U':
                    if h[0] < t[0] - 1:
                        t[0] = h[0]+1
                        t[1] = h[1] 
                elif dir_char == 'D':
                    if h[0] > t[0] + 1:
                        t[0] = h[0]-1
                        t[1] = h[1] 
                elif dir_char == 'L':
                    if h[1] < t[1] - 1:
                        t[1] = h[1]+1
                        t[0] = h[0] 
                elif dir_char == 'R':
                    if h[1] > t[1] + 1:
                        t[1] = h[1]-1
                        t[0] = h[0] 

                ts[str(t)] = 1

        result1 = sum(ts.values())

        # Part2
        snake = []
        for i in range(9):
            snake.append([0,0])

        H = [0,0]
        ts = {}
        ts[str(H)] = 1
            
        for line in lines:
            # print(line)
            words = line.split()
            dir_char = words[0]
            distance = int(words[1])

            d = dirs[dir_char]
            
            for i in range(distance):
                H[0] = H[0] + d[0]
                H[1] = H[1] + d[1]

                h = [H[0], H[1]]
                for j in range(len(snake)):
                    t = [snake[j][0], snake[j][1]]
                    # H top-left
                    if  h[0] < t[0] - 1 and h[1] < t[1] - 1:
                        t[0] = h[0] + 1
                        t[1] = h[1] + 1
                    # H top-right
                    elif  h[0] < t[0] - 1 and t[1] + 1 < h[1]:
                        t[0] = h[0] + 1
                        t[1] = h[1] - 1
                    # H bottom-right
                    elif t[0] + 1 < h[0] and t[1] + 1 < h[1]:
                        t[0] = h[0] - 1
                        t[1] = h[1] - 1
                    # H bottom-left
                    elif  t[0] + 1 < h[0] and h[1] < t[1] - 1:
                        t[0] = h[0] - 1
                        t[1] = h[1] + 1

                    #elif dir_char == 'R':
                    elif h[1] > t[1] + 1:
                        t[1] = h[1]-1
                        t[0] = h[0] 
                    #if dir_char == 'U':
                    elif h[0] < t[0] - 1:
                        t[0] = h[0]+1
                        t[1] = h[1] 
                    #elif dir_char == 'D':
                    elif h[0] > t[0] + 1:
                        t[0] = h[0]-1
                        t[1] = h[1] 
                    #elif dir_char == 'L':
                    elif h[1] < t[1] - 1:
                        t[1] = h[1]+1
                        t[0] = h[0] 

                    snake[j] = [t[0],t[1]]
                    h = [t[0],t[1]]
                    
                ts[str(h)] = 1

#             for r in range(-20,20):
#                 for c in range(-20,20):
#                     pos = [r,c]
#                     poss = str([r,c])
#                     printed = False
#                     if pos == H:
#                         print('H', end='')
#                         continue
#                     for i in range(len(snake)):
#                         if snake[i] == pos:
#                             printed = True
#                             print(i+1, end='')
#                             break
#                     if not printed:
#                         if poss in ts and ts[poss]:
#                             print('#', end='')
#                         elif pos == [0, 0]:
#                             print('s', end='')
#                         
#                         else:
#                             print('.', end='')
#                         
#                 print()
#             print()
#             print()


        result2 = sum(ts.values())
        print(f"{result2=}")

    # Guessed 1768
    # Guessed 2454
    # Gussed 2478 (too high)
    # 2458

                



    return (result1, result2)
