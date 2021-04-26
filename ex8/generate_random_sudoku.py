import numpy as np
from random import sample

def generate_sudoku():
    base = 3
    side = base * base

    # pattern for a baseline valid solution
    pattern = lambda r, c: (base * (r % base) + r // base + c) % side

    # randomize rows, columns and numbers (of valid base pattern)
    shuffle = lambda s: sample(s, len(s))

    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))

    # produce board using randomized baseline pattern
    board = [[nums[pattern(r, c)] for c in cols] for r in rows]
    squares = side * side
    empties = squares * 3 // 4
    for p in sample(range(squares), empties):
        board[p // side][p % side] = 0

    numSize = len(str(side))
    return board
