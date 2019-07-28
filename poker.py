import click
import sys

from enum import IntEnum
from itertools import groupby


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


def get_hand(cards):
    return sorted([(len(list(i[1])), i[0]) for i in groupby(
                sorted(cards), lambda x: x)], reverse=True)


def get_cards(card_string):
    return sorted([ALLOWED_SYMBOLS.get(i) for i in card_string])


def compare(lhand, rhand):
    lcomposition = [i[0] for i in lhand]
    rcomposition = [i[0] for i in rhand]
    if lcomposition > rcomposition:
        return 1
    if lcomposition < rcomposition:
        return -1
    if lhand > rhand:
        return 1
    if lhand < rhand:
        return -1
    return 0


def validate_input(input_string: str):
    return len(input_string) == HAND_SIZE \
        and all(i in ALLOWED_SYMBOLS for i in input_string)


@click.command()
@click.argument('lhand')
@click.argument('rhand')
def main(lhand, rhand):
    if not (validate_input(lhand) and validate_input(rhand)):
        print(f'Invalid hand symbol, should be only one of {ALLOWED_SYMBOLS}',
              file=sys.stderr)
        return 1
    lhand = get_cards(lhand)
    rhand = get_cards(rhand)
    return_string = {
        1: 'First hand wins!',
        0: 'It\'s a tie!',
        -1: 'Second hand wins!'
    }
    print(return_string[compare(get_hand(lhand), get_hand(rhand))])


if __name__ == '__main__':
    main()
