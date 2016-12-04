# coding: utf-8
def ceil(a):
    if int(a) == a: return int(a)
    else: return int(a) + 1

def get_nth_smallest_value(array1, array2):
    """Find nth smallest value from union of 2 * n integers in time O(log n).

    To run doctests:
        python -m doctest -v solution.py
    >>> get_nth_smallest_value([1, 2, 3], [4, 5, 6])
    3
    >>> get_nth_smallest_value([1, 2, 4, 6], [3, 5, 7, 8])
    4
    >>> get_nth_smallest_value([-84, -79, -77, -65, -54, -53, -31, -11, -10, -7, -4, 10, 24, 25, 35, 69, 90], 
    ... [-100, -93, -78, -56, -55, -45, 1, 3, 16, 27, 50, 56, 64, 65, 70, 74, 100])
    -4
    >>> get_nth_smallest_value([-498, -489, -480, -465, -442, -429, -381, -372, -350, -297, -289, 
    ... -203, -199, -170, -139, -121, -106, -95, -89, -80, 24, 26, 66, 164, 175, 180, 
    ... 198, 220, 225, 243, 269, 271, 288, 311, 328, 335, 343, 392, 425, 439, 459],
    ... [-451, -433, -336, -247, -240, -215, -194, -172, -146, -142, -79, -65, 
    ... -41, -13, -4, 44, 57, 69, 92, 145, 148, 170, 191, 194, 195, 213, 241, 255, 259, 
    ... 261, 286, 291, 362, 377, 382, 424, 432, 461, 482, 490, 491])
    69
    >>> get_nth_smallest_value([1, 2, 3, 4, 5, 6],[-9, -8, -7, 10, 11, 12])
    3

    Parameters
    ----------
    array1 : sorted list of int
    array2 : sorted list of int, same length as array1

    Returns
    -------
    val : int
        The nth smallest value in the union of the two lists, when both
        lists have length n.
    """
    return smallest(array1, 0, array2, 0, len(array1))


def smallest(A, Ai, B, Bi, n):
    if n == 2: 
        return sorted([A[Ai], A[Ai+1], B[Bi], B[Bi+1]])[1]
    
    ma = A[Ai + n//2 - 1]
    mb = B[Bi + n//2 - 1]

    if ma < mb:
        return smallest(A, Ai + n//2, B, Bi, ceil(n/2))
    else:
        return smallest(A, Ai, B, Bi + n//2, ceil(n/2))

