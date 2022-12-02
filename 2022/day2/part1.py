#!/usr/bin/env python3

"""Advent of Code Day 1

Usage:
  part1.py --data-source <data> 

Options:
  -h, --help            Show this screen.
  --version             Show version.
  --data-source=<data>  Path to data source

"""
from docopt import docopt

def main(data_source): 

    
    numbers = []
    total = 0
    with open(data_source, 'r', encoding='UTF-8') as file:
        while (line := file.readline().rstrip()):
            they, you = line.split()

            score = 0
            print(they, you)

            they = ord(they[0]) - ord('A')
            you = ord(you[0]) - ord('X')
            print(they, you)

            score += you + 1
            if they == you:
                score += 3
            
            if (they == 0 and you == 1) or (they == 1 and you == 2) or (they == 2 and you == 0):
                score += 6

            total += score
            print(score, total)
            print("")

    print(total)


if __name__ == '__main__':
    arguments = docopt(str(__doc__), version="0.0.1")

    main(data_source=arguments['--data-source'])
