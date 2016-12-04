# coding: utf-8
import sys


# coding: utf-8
def hello_world(n):
    """Prints 'Hello World!' n times to stdout.

    To run doctests:
        python3 -m doctest -v solution.py
    >>> hello_world(3)
    Hello World!
    Hello World!
    Hello World!
    
    Parameters
    ----------

    n : integer
        number of times to repeat 'Hello World!' to stdout

    Returns
    -------
    N/A (no return value)
    """
    
    for i in range(n):
        print("Hello World!")
    


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: .py <int>")
        sys.exit(1)
    
    n = int(sys.argv[1])
    
    # Call the function
    hello_world(n)
