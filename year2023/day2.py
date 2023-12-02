debug = False

from .utils import *
from collections import defaultdict
from pprint import pprint
import copy


def solution(file):

    # print(f'{file=}')

    result1 = result2 = 0

    sections = read(file)
    lines = sections[0]
    # print(lines)

    result1 = 0  # sum of ids of "possible" games

    # games = dict()

    max_counts = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }

    for line in lines:
        game_name, game_record = line.split(': ')
        _, game_number = game_name.split(' ')
        sets = game_record.split('; ')
        print(f'{sets}')
        for s in sets:
            color_counts = s.split(', ')
            possible = True
            for cc in color_counts:
                count_string, color = cc.split(' ')
                if int(count_string) > max_counts[color]:
                    possible = False
                    break
            if not possible:
                break

        if possible:
            result1 += int(game_number)
        print(f'{possible=}')



    for line in lines:
        result2 += 1

    return (result1, result2)
