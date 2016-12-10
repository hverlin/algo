# coding: utf-8


def get_coins(target_value, denominations):
    """Makes change for the given target value using the fewest coins possible.

    To run doctests:
        python3 -m doctest -v solution.py
    >>> get_coins(62, [7, 25, 41])
    [3, 0, 1]
    >>> get_coins(21894, [1506, 1708, 2001, 2009, 2066, 2999, 3003])
    >>> get_coins(60, [1, 2, 5, 10, 20, 50, 100, 200])
    [0, 0, 0, 1, 0, 1, 0, 0]
    >>> get_coins(1, [1, 2, 5])
    [1, 0, 0]

    Parameters
    ----------
    target_value : int
        The amount we need to make change for.
    denominations : list of int, sorted from smallest to largest
        The values of different coins, e.g. [1, 2, 5, 10, 20, 50, 100,
        200] for the euro.

    Returns
    -------
    coins_used : list of int, or None
        A list the same length as denominations, specifying how many of
        each coin were used to get to target_value. Empty or None if we
        cannot form change for target_value using the given
        denominations.
    """

    mat = [[0 for i in range(len(denominations))] for i in range(0, target_value + 1)]

    skip_index = set()
    for i, v in enumerate(denominations):
        if v <= target_value:
            mat[v][i] = 1
            skip_index.add(v)

    for target in range(target_value + 1):
        if target not in skip_index:
            temp = float("inf")

            for idx, v in enumerate(denominations):
                if target - v >= 0:
                    s = sum(mat[target - v])
                    if s > 0 and s + 1 < temp:
                        temp = s + 1
                        mat[target] = list(mat[target - v])
                        mat[target][idx] += 1

    return mat[target_value] if sum(mat[target_value]) > 0 else None
