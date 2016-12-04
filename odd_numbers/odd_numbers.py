# coding: utf-8
import sys

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

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: .py <array file>")
        sys.exit(1)
    
    # Read list from given file or stdin
    with open(sys.argv[1]) as f:
        line = f.readline().split()
        number_array = [int(i) for i in line]
        
        # Find solution
        result = odd_numbers(number_array)
        
        # Output solution
        print("The count of odd numbers is %d." % result)
        