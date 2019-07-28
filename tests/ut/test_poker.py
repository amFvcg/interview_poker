import pytest
from poker import GroupEntry as GE
from poker import CompResult

def test_get_hand():
    from poker import get_hand
    cards = 'A3AQK'
    result = get_hand(cards)
    expected = [(2, 'A'), (1, 'K'), (1, 'Q'), (1, '3')]
    assert sorted(result) == sorted(expected),\
        f'Expected: {expected}, Result: {result}'


test_data_compare_hands = [
    ([GE(2, 'A'), GE(1, '5'), GE(1, '3'), GE(1, '4')],
     [GE(2, 'A'), GE(1, '2'), GE(1, '3'), GE(1, '4')],
     CompResult.FirstWon),
    ([GE(2, 'A'), GE(1, '2'), GE(1, '3'), GE(1, '4')],
     [GE(2, 'A'), GE(1, '5'), GE(1, '3'), GE(1, '4')],
     CompResult.SecondWon),
    ([GE(2, 'A'), GE(1, '2'), GE(1, '3'), GE(1, '4')],
     [GE(2, 'A'), GE(1, '2'), GE(1, '3'), GE(1, '4')],
     CompResult.Tie),
    ([GE(3, '2'), GE(1, 'A'), GE(1, '3'), GE(1, '4')],
     [GE(2, 'A'), GE(1, '2'), GE(1, '3'), GE(1, '4')],
     CompResult.FirstWon),
    ([GE(3, 10), GE(2, 13)],
     [GE(3, 13), GE(2, 10)],
     CompResult.SecondWon),
]


@pytest.mark.parametrize('lhand,rhand,expected', test_data_compare_hands)
def test_compare_hands(lhand, rhand, expected):
    from poker import compare
    assert compare(lhand, rhand) == expected
