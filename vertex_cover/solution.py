# coding: utf-8


def get_minimal_vertex_cover(g):
    """Find a vertex cover s.t. no subset of the vertices forms a cover.

    To run doctests:
        python -m doctest -v solution.py
    >>> from networkx import Graph
    >>> get_minimal_vertex_cover(Graph({1: [2, 3], 2: [], 3: []})) in ([2, 3], [3, 2], [1])
    True
    >>> get_minimal_vertex_cover(Graph({1: [3], 2: [1], 3: [2]})) in ([1], [2], [3])
    True
    
    Parameters
    ----------
    g : Graph

    Returns
    -------
    cover : list of int corresponding to indices of the nodes in the cover
        E.g. [1, 2, 5, 11, 12]
    """

    nodes = set()
    for n in g.nodes_iter():
        nodes.add(n)

    for u in g.nodes_iter():
        should_remove = True
        for n in g.neighbors(u):
            if n not in nodes:
                should_remove = False
        if should_remove:
            nodes.remove(u)
    return list(nodes)
