#!/usr/bin/env python3

"""Advent of Code

Usage:
  main.py [--year=YEAR] [--day=DAY] [--debug] [<data_source>...]
  main.py [--help | --version]

Options:
  -h, --help         Show this screen.
  --version          Show version.
  --year=YEAR        Year [default: 2023].
  --day=DAY          Day [default: 1].
  --debug            Enable debug logging.
  <data_source>...   Path(s) to data source.

"""
from docopt import docopt

from utils import dprint, read_data_sources, bcolors
import utils



def main():
    arguments = docopt(str(__doc__), version="0.0.1")


    debug = arguments['--debug']
    utils.debug = bool(debug)
    if debug:
        dprint(arguments)

    year = int(arguments['--year'])
    day = int(arguments['--day'])
    data_sources = arguments['<data_source>']

    _day = __import__(f'year{year}.day{day}', globals(), locals(), ['solution'])
    solution = _day.solution

    # solution.solution('year2022/day1/sample.txt')

    if not data_sources:
        data_sources = read_data_sources(year, day)


    # if not data_sources:
    #    data_sources = [
    #             f'year{year}/day{day}.sample.in',
    #             f'year{year}/day{day}.sample-2.in',
    #             # f'year{year}/day{day}.sample-3.in',
    #             ]

    ds_i = 1
    for ds in data_sources:
        print(f"Data source #{ds_i} ({ds}): ")
        content, p1_expected, p2_expected = data_sources[ds]

        result1, result2 = solution(content)

        print("Part 1:                            %s" % result1)

        if str(result1) == p1_expected:
            print(f"{bcolors.OKGREEN}CORRECT -- Expected value          {p1_expected}{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}INCORRECT -- Expected value       {p1_expected}{bcolors.ENDC}")
        print()

        if result2 is not None:
            print("Part 2:                            %s" % result2)
            if str(result2) == p2_expected:
                print(f"{bcolors.OKGREEN}CORRECT -- Expected value          {p2_expected}{bcolors.ENDC}")
            else:
                print(f"{bcolors.FAIL}INCORRECT -- Expected value        {p2_expected}{bcolors.ENDC}")
            print()

        print()
        if ds_i < len(data_sources):
            print("Do you want to test the next data source")
            choice = input("Y/n: ")
            if choice and choice[0] in 'nN':
                break
            ds_i += 1


if __name__ == '__main__':
    main()
