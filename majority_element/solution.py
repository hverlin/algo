# coding: utf-8

def find_majority_element(data, tiebreaker=None):
    """Return the majority element of the list, if any, or None.
    
    To run doctests:
        python3 -m doctest -v solution.py
    >>> from element import to_element_list
    >>> from majority_element import read_data_from_file
    >>> find_majority_element(to_element_list([1, 2]))
    >>> find_majority_element(read_data_from_file("examples/03.3.instance"))
    3

    Parameters
    ----------
    elements : list of Element objects

    Returns
    -------
    element : Element or None
        One of the majority elements in the lists (if exists), otherwise None
        E.g. if no majority element, return None.
    """
    
    return find_maj(data)

def find_maj(A):
    if len(A) == 1: return A[0]

    elif len(A) == 2:
        return A[0] if A[0] == A[1] else None
    
    else:
        m = len(A)//2
        majA = find_maj(A[:m])
        majB = find_maj(A[m:])

        if majA == majB: return majA
        
        elif majA == None and majB != None:
            return majB if len([x for x in A if x == majB]) > len(A)//2 else None

        elif majA != None and majB == None:
            return majA if len([x for x in A if x == majA]) > len(A)//2 else None

        elif majA != None and majB != None:
            if len([x for x in A if x == majA]) > len(A)//2: return majA
            elif len([x for x in A if x == majB]) > len(A)//2: return majB
            else: return None
        else: return None

