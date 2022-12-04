#!/usr/bin/env python3

"""Advent of Code Day 3

Usage:
  part1.py --data-source <data> 

Options:
  -h, --help            Show this screen.
  --version             Show version.
  --data-source=<data>  Path to data source

"""
from docopt import docopt


def main(data_source): 

    total = 0
    
    lines = []
    with open(data_source, 'r', encoding='UTF-8') as file:
        while (line := file.readline().rstrip()):
            lines.append(line)

    for line in lines:
        first = line[0:int(len(line)//2)]
        second = line[len(line)//2:]

        first, second = list(first), list(second)

        first.sort()
        second.sort()

        print(line)

        found = None
        for l in first:
            if l in second:
                found = l
                break

        val = 0
        if found and found.isupper():
            val = ord(found) - ord('A') + 27
        else:
            val = ord(found) - ord('a') + 1
        
        total += val

        print(found, val, total)



if __name__ == '__main__':
    arguments = docopt(str(__doc__), version="0.0.1")

    main(data_source=arguments['--data-source'])
