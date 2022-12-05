#!/usr/bin/env python3

def solution(data_source): 

    result1 = result2 = 0
    
    total = 0
    with open(data_source, 'r', encoding='UTF-8') as file:
        while (line := file.readline().rstrip()):
            a, b = line.split()
            a = ord(a) - ord('A')
            b = ord(b) - ord('X')

            # Part1
            score1 = b + 1
            if a == b:
                score1 += 3
            if (a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 0):
                score1 += 6
            result1 += score1

            # Part2
            if b == 0:
                b = a - 1
                if b == -1:
                    b = 2
            elif b == 1:
                b = a
            elif b == 2:
                b = a + 1
                if b == 3:
                    b = 0
            score2 = b + 1
            if a == b:
                score2 += 3
            if (a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 0):
                score2 += 6
            result2 += score2



    return(result1, result2)
