from random import random

from poker import main, ALLOWED_SYMBOLS


def gen_entries(count: int):
    symbols_count = len(ALLOWED_SYMBOLS.keys())
    symbols = list(ALLOWED_SYMBOLS.keys())
    entries = [(symbols[int(random()*symbols_count)],
                symbols[int(random()*symbols_count)]) for i in range(count)]
    return entries


def perf_test():
    entries = gen_entries(1000000)
    for first, second in entries:
        main(first, second)


if __name__ == '__main__':
    perf_test()
