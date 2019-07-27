import click
import sys

from enum import IntEnum


ALLOWED_SYMBOLS = '23456789TJQKA'


class Combinations(IntEnum):
    HighCard = 0
    Pair = 1
    TwoPairs = 2
    Triple = 3
    Full = 4
    Four = 5


def get_hand(cards):
    return Combinations.HighCard


def get_cards(card_string):
    return []


def compare(*args):
    return 1

def validate_input(input_string: str):
    return all(i in ALLOWED_SYMBOLS for i in input_string)


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
        1: 'First hand wins',
        0: 'It\'s a tie',
        -1: 'Second hand wins'
    }
    print(return_string[compare(get_hand(lhand), get_hand(rhand))])

if __name__ == '__main__':
    main()
