#!/usr/bin/env python3

"""Advent of Code

Usage:
  main.py [--year=YEAR] [--day=DAY] [--debug] [<data_source>...]
  main.py [--help | --version]

Options:
  -h, --help         Show this screen.
  --version          Show version.
  --year=YEAR        Year [default: 2022].
  --day=DAY          Day [default: 8].
  --debug            Enable debug logging.
  <data_source>...   Path(s) to data source.

"""
from docopt import docopt




def main():
    arguments = docopt(str(__doc__), version="0.0.1")

    debug = arguments['--debug']
    if debug:
        print(arguments)

    year = int(arguments['--year'])
    day = int(arguments['--day'])
    data_sources = arguments['<data_source>']

    _day = __import__(f'year{year}.day{day}', globals(), locals(), ['solution'])
    solution = _day.solution

    # solution.solution('year2022/day1/sample.txt')
    
    if not data_sources:
        data_sources = [
            f'year{year}/day{day}.sample.in',
            f'year{year}/day{day}.in',
        ]

    for ds in data_sources:
        print(ds)
        print()
        result1, result2 = solution(ds)

        print("Part 1:                            %s" % result1)

        if result2 is not None:
            print("Part 2:                            %s" % result2)
            print()

        print()

if __name__ == '__main__':
    main()
