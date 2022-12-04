#!/usr/bin/env python3

"""Advent of Code Day 3

Usage:
  part2.py --data-source <data> 

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

    index = 0
    while index < len(lines):
        line = lines[index]

        found = None
        for c in line:
            if c in lines[index+1] and c in lines[index+2]:
                found = c
                index += 3
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
