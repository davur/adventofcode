debug = False

from utils import dprint, warn
from collections import defaultdict
from pprint import pprint
import copy


def solution(sections):

    # dprint(f'{file=}')

    result1 = result2 = 0

    lines = sections[0]
    # dprint(lines)

    game_wins = dict()
    game_copies = dict()

    for game in lines:

        game_name, game_record = game.split(': ')
        dprint(f'{game_name=}')
        _, game_number = game_name.split()
        game_number = int(game_number)
        have_string, win_string = game_record.split(' | ')

        numbers = set([int(num) for num in have_string.split()])
        winning = set([int(num) for num in win_string.split()])

        # dprint(f'{numbers=}')
        # dprint(f'{winning=}')

        found = numbers & winning

        game_wins[game_number] = len(found)
        game_copies[game_number] = 1

        if found:
            score = 2**(len(numbers & winning) - 1)
            dprint(f'{score=}')
            result1 += score

    for game_number in game_copies:
        copies = game_copies[game_number]
        wins = game_wins[game_number]
        for i in range(game_number + 1, game_number + 1 + wins):
            game_copies[i] += copies

    result2 = sum(game_copies.values())

    return (result1, result2)
