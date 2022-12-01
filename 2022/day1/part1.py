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
    print(totals[-1])


if __name__ == '__main__':
    arguments = docopt(str(__doc__), version="0.0.1")

    main(data_source=arguments['--data-source'])
