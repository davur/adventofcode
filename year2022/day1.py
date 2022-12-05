#!/usr/bin/env python3

def solution(data_source): 

    with open(data_source, 'r', encoding='UTF-8') as file:
        numbers = file.readlines()

    totals = []
    total = 0
    for i in numbers:
        i = i.strip()
        if i:
            total += int(i)
        else:
            totals.append(total)
            total = 0

    totals.sort()

    result1 = totals[-1]
    result2 = sum(totals[-3:])

    return (result1, result2)
