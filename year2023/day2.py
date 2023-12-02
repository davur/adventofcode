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

    for game in lines:
        min_counts = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }

        game_name, game_record = game.split(': ')
        _, game_number = game_name.split(' ')
        sets = game_record.split('; ')
        print(f'{sets}')
        possible = True
        for s in sets:
            color_counts = s.split(', ')
            for cc in color_counts:
                count_string, color = cc.split(' ')
                if int(count_string) > max_counts[color]:
                    possible = False

                count = int(count_string)
                if min_counts[color] < count:
                    min_counts[color] = count


        if possible:
            result1 += int(game_number)
        print(f'{possible=}')

        power = min_counts['red'] * min_counts['green'] * min_counts['blue']
        print(f'{power=}')
        result2 += power

    return (result1, result2)
