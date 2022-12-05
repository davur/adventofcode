#!/usr/bin/env python3

def solution(data_source): 

    result1 = result2 = 0

    total = 0
    
    lines = []
    with open(data_source, 'r', encoding='UTF-8') as file:
        while (line := file.readline().rstrip()):
            lines.append(line)

    i = 0
    for i in range(len(lines)):
        line = lines[i]

        # Part1
        first = set(line[0:int(len(line)//2)])
        second = set(line[len(line)//2:])

        overlap = first & second
        
        found = overlap.pop()
        val = 0
        if found and found.isupper():
            val = ord(found) - ord('A') + 27
        else:
            val = ord(found) - ord('a') + 1
        
        result1 += val

        # Part2
        if i % 3 == 0:
            overlap = set(line) & set(lines[i+1]) & set(lines[i+2])

            found = overlap.pop()
            val = 0
            if found and found.isupper():
                val = ord(found) - ord('A') + 27
            else:
                val = ord(found) - ord('a') + 1
            
            result2 += val


    return (result1, result2)
