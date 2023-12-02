
from utils import dprint, warn
from collections import defaultdict
from pprint import pprint
import copy



def solution(sections):

    # dprint(f'{file=}')

    result1 = result2 = 0

    lines = sections[0]
    # dprint(lines)

    # Part 1
    result1 = 0
    for line in lines:
        # dprint(f'{line=}')
        l = None
        r = None
        for i in range(len(line)):
            c = line[i]
            # dprint(f'{c=}')
            if c in '0123456789':
                l = c
                break

        for i in range(len(line)-1, -1, -1):
            c = line[i]
            if c in '0123456789':
                r = c
                break

        if l is None or r is None:
            warn(f"No numbers found in Line '{line}'")
        else:
            val = int(f'{l}{r}')
            result1 += val

    # Part 2
    result2 = 0
    numbers = {
            'o': {'one': '1'},
            't': {'two': '2', 'three': '3'},
            'f': {'four': '4', 'five': '5'},
            's': {'six': '6', 'seven': '7'},
            'e': {'eight': '8'},
            'n': {'nine': '9'},
            'z': {'zero': '0'},
            }

    for line in lines:
        dprint(f'{line=}')
        l = None
        r = None
        for i in range(len(line)):
            c = line[i]
            # dprint(f'{c=}')
            if c in '0123456789':
                l = c
                break
                # dprint(f'int {l=}')
            if c in numbers:
                for word, value in numbers[c].items():
                    if line[i:i+len(word)] == word:
                        l = value
                        # dprint(f'{l=}')
                if l is not None:
                    break


        for i in range(len(line)-1, -1, -1):
            c = line[i]
            # dprint(f"{c=}")
            if c in '0123456789':
                r = c
                # dprint(f'int {r=}')
                break
            if c in numbers:
                for word, value in numbers[c].items():
                    if line[i:i+len(word)] == word:
                        r = value
                        # dprint(f'{r=}')
                        break
                if r is not None:
                    break

        val = int(f'{l}{r}')
        dprint(f'{val=}')

        result2 += val

    return (result1, result2)
