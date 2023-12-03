#!/usr/bin/env python3

"""Advent of Code

Usage:
    setup.py [--year=YEAR] [--day=DAY] [--debug]
  setup.py [--help | --version]

Options:
    -h, --help         Show this screen.
  --version          Show version.
  --year=YEAR        Year [default: 2023].
  --day=DAY          Day [default: 1].
  --part=PART        Part [default: ALL].
  --debug            Enable debug logging.

"""
from docopt import docopt

import os.path


def setup():
    arguments = docopt(str(__doc__), version="0.0.1")

    debug = arguments['--debug']
    if debug:
        print(arguments)

    year = int(arguments['--year'])
    day = int(arguments['--day'])

    more_samples = True
    sample_number = 1
    while more_samples:
        if sample_number == 1:
            sample_suffix = ''
        else:
            sample_suffix = f'-{sample_number}'

        sample_file = f'year{year}/day{day}.sample{sample_suffix}.in'
        sample_exists = os.path.isfile(sample_file)
        prompt_for_input = False
        if sample_exists:
            print(f"Sample file {sample_file} already exists")
            choice = input("Do you want to overwrite it? y/N: ")
            prompt_for_input = (choice[0] in 'yY')
        else:
            print(f"Sample file {sample_file} does not exists")
            choice = input("Do you want to create it? y/N: ")
            prompt_for_input = (choice[0] in 'yY')

        if prompt_for_input:
            print("Enter/Paste sample content. Ctrl-D to save it.")
            contents = []
            while True:
                try:
                    line = input()
                except EOFError:
                    break
                contents.append(line)

            with open(sample_file, 'w', encoding='UTF-8') as file:
                file.write('\n'.join(contents))


        sample_output = f'year{year}/day{day}.sample{sample_suffix}.p1.out'
        sample_exists = os.path.isfile(sample_output)
        prompt_for_input = False
        if sample_exists:
            print(f"P1 output file {sample_output} already exists")
            choice = input("Do you want to overwrite it? y/N: ")
            prompt_for_input = (choice[0] in 'yY')
        else:
            print(f"P1 output file {sample_output} does not exists")
            choice = input("Do you want to create it? y/N: ")
            prompt_for_input = (choice[0] in 'yY')

        if prompt_for_input:
            expected_output = input("Enter/Paste expected output: ")

            with open(sample_output, 'w', encoding='UTF-8') as file:
                file.write(expected_output)

        sample_output = f'year{year}/day{day}.sample{sample_suffix}.p2.out'
        sample_exists = os.path.isfile(sample_output)
        prompt_for_input = False
        if sample_exists:
            print(f"P2 output file {sample_output} already exists")
            choice = input("Do you want to overwrite it? y/N: ")
            prompt_for_input = (choice[0] in 'yY')
        else:
            print(f"P2 output file {sample_output} does not exists")
            choice = input("Do you want to create it? y/N: ")
            prompt_for_input = (choice[0] in 'yY')

        if prompt_for_input:
            expected_output = input("Enter/Paste expected output: ")

            with open(sample_output, 'w', encoding='UTF-8') as file:
                file.write(expected_output)


        choice = input("Do have more samples? y/N: ")
        more_samples = (choice[0] in 'yY')
        sample_number += 1




    # solution.solution('year2022/day1/sample.txt')
    # f'year{year}/day{day}.sample.in',
    # f'year{year}/day{day}.in',

if __name__ == '__main__':
    setup()
