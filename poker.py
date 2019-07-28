import click
import sys

from enum import Enum, IntEnum
from itertools import groupby
from collections import namedtuple

GroupEntry = namedtuple('GroupEntry', ['count', 'symbol'])


class AllowedSymbols(IntEnum):
    Two = 0
    Three = 1
    Four = 2
    Five = 3
    Six = 4
    Seven = 5
    Eight = 6
    Nine = 7
    Ten = 8
    Jack = 9
    Queen = 10
    King = 11
    Ace = 12


ALLOWED_SYMBOLS = dict(zip('23456789TJQKA', list(AllowedSymbols)))

HAND_SIZE = 5


class CompResult(Enum):
    FirstWon = 'First hand wins!'
    SecondWon = 'Second hand wins!'
    Tie = 'It\'s a tie!'

def get_hand(cards):
    return sorted([GroupEntry(len(list(i[1])), i[0]) for i in groupby(
                sorted(cards), lambda x: x)], reverse=True)


def get_cards(card_string: str):
    return sorted([ALLOWED_SYMBOLS.get(i) for i in card_string])


def compare(lhand, rhand):
    lcomposition = [i.count for i in lhand]
    rcomposition = [i.count for i in rhand]
    # TRICKY: first check by count of cards
    if lcomposition > rcomposition:
        return CompResult.FirstWon
    if lcomposition < rcomposition:
        return CompResult.SecondWon
    # TRICKY: then check by card values itself
    if lhand > rhand:
        return CompResult.FirstWon
    if lhand < rhand:
        return CompResult.SecondWon
    return CompResult.Tie


def validate_input(input_string: str):
    return len(input_string) == HAND_SIZE \
        and all(i in ALLOWED_SYMBOLS for i in input_string)


@click.command()
@click.argument('lhand')
@click.argument('rhand')
def main(lhand: str, rhand: str):
    if not (validate_input(lhand) and validate_input(rhand)):
        print(f'Invalid hand symbol, should be only one of {ALLOWED_SYMBOLS}',
              file=sys.stderr)
        return 1
    lhand = get_cards(lhand)
    rhand = get_cards(rhand)
    print(compare(get_hand(lhand), get_hand(rhand)).value)


if __name__ == '__main__':
    main()
