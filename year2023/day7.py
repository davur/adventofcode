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
    letters2 = 'AKQT98765432J'

    hands = []
    hands2 = []
    for line in lines:
        s, bid = line.split()
        hand = []
        hand2 = []
        for c in s:
            hand.append(letters.index(c))
            hand2.append(letters2.index(c))
        bid = int(bid)

        hands.append((hand, bid))
        hands2.append((hand2, bid))


    rankings = []
    rankings2 = []

    for i in range(len(hands)):
        dprint(f'{i=}')
        hand2, bid = hands[i]
        hand, bid = hands2[i]

        hand_backup = [c for c in hand]

        joker = letters2.index('J')



        cards = defaultdict(int)

        for c in hand:
            cards[c] = cards[c] + 1

        dprint(f'{hand=}')
        dprint(f'{joker=}')

        highest_card = -1
        highest_count = 0
        for k, v in cards.items():
            if v > highest_count and k != joker:
                highest_card = k
                highest_count = v
        for i in range(len(hand)):
            if hand[i] == joker:
                hand[i] = highest_card

        dprint(f'{highest_card=}')
        dprint(f'{hand=}')

        cards = defaultdict(int)

        for c in hand:
            cards[c] = cards[c] + 1

        jokers = cards[joker]

        counts = list(cards.values())
        counts.sort()
        dprint(f'{counts=}')

        if counts[-1] == 5:
            typ = 1  # Five of a kind
            typ2 = typ  # Five of a kind
        elif counts[-1] == 4:
            typ = 2  # Four of a kind
            typ2 = 1 if jokers > 1 else typ
        elif counts[-1] == 3:
            if counts[-2] == 2:
                typ = 3  # Full house
                typ2 = 1 if jokers > 0 else typ
            else:
                typ = 4  # Three of a kind
                typ2 = 2 if jokers > 0 else typ
        elif counts[-1] == 2:
            if counts[-2] == 2:
                typ = 5  # Two pairs
                typ2 = typ - jokers - 1 if jokers > 0 else typ
            else:
                typ = 6  # One pair
                typ2 = 4 if jokers > 0 else typ
        else:
            typ = 7  # High card
            typ2 = 6 if jokers else typ

        # dprint(f'{typ=}')
        dprint(f'{typ2=}')

        rankings.append((typ, hand_backup, bid))
        rankings2.append((typ2, hand2, bid))

    # dprint(f'{len(rankings2)=}')

    rankings.sort()
    # dprint(f'{rankings=}')
    rankings2.sort()
    # pprint(f'{rankings2=}')

    for i in range(1, len(rankings)+1):
        result1 += i * rankings[0-i][-1]
        result2 += i * rankings2[0-i][-1]

#         cards = set(list(hand))
#         if len(cards) == 1:  # Five of a kind
#             type_ = 7
#         elif len(cards) == 2:  # Four of a kind, Full house
#
#         elif len(cards) == 3:  # Two Pairs, Three of a kind
#
#         elif len(cards) == 5:  # High card
#             type_ = 1


    # Result2 = 244286912  is not right, it is too high
    #          # 244347314
    #         # 244155614 Still too high :(((
    #         # 243371136 Still too high
    #         # 243255879
    #         #  243255879
    #         # 243014828   Not sure if high or low

    return (result1, result2)
