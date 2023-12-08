debug = False

from utils import dprint, warn
from collections import defaultdict
from pprint import pprint
import copy


def solution(sections):

    # dprint(f'{file=}')

    result1 = result2 = 0

    lines = sections[0]

    letters = 'AKQJT98765432'

    hands = []
    for line in lines:
        s, bid = line.split()
        hand = []
        for c in s:
            hand.append(letters.index(c))
        bid = int(bid)

        hands.append((hand, bid))


    rankings = []

    for i in range(len(hands)):
        hand, bid = hands[i]

        type_ = 0

        cards = defaultdict(int)

        for c in hand:
            cards[c] = cards[c] + 1

        dprint(f'{cards=}')

        counts = list(cards.values())
        counts.sort()
        dprint(f'{counts}')

        if counts[-1] == 5:
            typ = 1  # Five of a kind
        elif counts[-1] == 4:
            typ = 2  # Four of a kind
        elif counts[-1] == 3:
            if counts[-2] == 2:
                typ = 3  # Full house
            else:
                typ = 4  # Three of a kind
        elif counts[-1] == 2:
            if counts[-2] == 2:
                typ = 5  # Two pairs
            else:
                typ = 6  # One pair
        else:
            typ = 7  # High card

        rankings.append((typ, hand, bid))

    rankings.sort()
    dprint(rankings)

    for i in range(1, len(rankings)+1):
        result1 += i * rankings[0-i][-1]

#         cards = set(list(hand))
#         if len(cards) == 1:  # Five of a kind
#             type_ = 7
#         elif len(cards) == 2:  # Four of a kind, Full house
#
#         elif len(cards) == 3:  # Two Pairs, Three of a kind
#
#         elif len(cards) == 5:  # High card
#             type_ = 1


    return (result1, result2)
