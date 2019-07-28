import pytest

def test_get_hand():
    from poker import get_hand
    cards = 'A3AQK'
    result = get_hand(cards)
    expected = [(2, 'A'), (1, 'K'), (1, 'Q'), (1, '3')]
    assert sorted(result) == sorted(expected),\
        f'Expected: {expected}, Result: {result}'


test_data_compare_hands = [
    ([(2, 'A'), (1, '5'), (1, '3'), (1, '4')],
     [(2, 'A'), (1, '2'), (1, '3'), (1, '4')],
     1),
    ([(2, 'A'), (1, '2'), (1, '3'), (1, '4')],
     [(2, 'A'), (1, '5'), (1, '3'), (1, '4')],
     -1),
    ([(2, 'A'), (1, '2'), (1, '3'), (1, '4')],
     [(2, 'A'), (1, '2'), (1, '3'), (1, '4')],
     0),
    ([(3, '2'), (1, 'A'), (1, '3'), (1, '4')],
     [(2, 'A'), (1, '2'), (1, '3'), (1, '4')],
     1),
    ([(3, 10), (2, 13)],
     [(3, 13), (2, 10)],
     -1),
]


@pytest.mark.parametrize('lhand,rhand,expected', test_data_compare_hands)
def test_compare_hands(lhand, rhand, expected):
    from poker import compare
    assert compare(lhand, rhand) == expected
