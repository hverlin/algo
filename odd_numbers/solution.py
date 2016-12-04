# coding: utf-8
def odd_numbers(array):
    """Return the number of odd numbers found in the provided
    list of integers.
    
    To run doctests:
        python3 -m doctest -v solution.py
    >>> odd_numbers([1, 3, 4])
    2
    
    >>> odd_numbers([6, 8])
    0
    
    Parameters
    ----------

    array : list of integers
    
    Returns
    -------
    val: int
        The number of odd numbers found in the given list.
    """    
    return len([x for x in array if x % 2 != 0])    