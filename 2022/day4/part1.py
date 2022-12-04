#!/usr/bin/env python3

"""Advent of Code Day 4

Usage:
  part1.py --data-source <data> 

Options:
  -h, --help            Show this screen.
  --version             Show version.
  --data-source=<data>  Path to data source

"""
from docopt import docopt


def main(data_source): 

    result1 = 0
    result2 = 0
    
    lines = []
    with open(data_source, 'r', encoding='UTF-8') as file:
        while (line := file.readline().rstrip()):
            lines.append(line)

    for line in lines:
        first, second = line.split(',')
        first1, first2 = first.split('-')
        first1, first2 = int(first1), int(first2)
        second1, second2 = second.split('-')
        second1, second2 = int(second1), int(second2)

        first_set = set(range(first1, first2+1))
        second_set = set(range(second1, second2+1))

        overlap = first_set & second_set

        # part 1 if first contains second, or second contains first
        if overlap == first_set or overlap == second_set:
            result1 += 1

        # part 2 if there is any overlap
        if overlap: 
            result2 += 1


    print("Result 1:")
    print(result1)
    print()
    print("Result 2:")
    print(result2)


if __name__ == '__main__':
    arguments = docopt(str(__doc__), version="0.0.1")

    main(data_source=arguments['--data-source'])
