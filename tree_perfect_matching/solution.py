def tree_perfect_matching(tree):
    """For a tree, return a list of edges that constitutes a perfect matching: a set of edges having no endpoints in common that covers all vertices.
    
    To run doctests:
        python -m doctest -v solution.py
    >>> from networkx import Graph
    >>> tree_perfect_matching(Graph({1: [2, 3], 2: [], 3: []}))
    >>> tree_perfect_matching(Graph({1: [3], 2: [4], 3: [2]})) in ([(1, 3), (2, 4)], [(2, 4), (3, 1)], [(1, 3), (4, 2)], [(3, 1), (4, 2)])
    True
    
    Parameters
    ----------
    tree : Graph

    Returns
    -------
    matching : list
        list of edges (as (int, int) tuples) that constitutes a perfect matching, or None.
    """

    if len(tree) % 2 == 1:
        return None

    edges = set()
    parents = set(tree.nodes())

    while len(tree) > 0:
        curr_nodes = [n for n in parents if tree.degree(n) == 1]
        parents = set()
        to_remove = []

        for node in curr_nodes:
            try:
                neighbor = tree.neighbors(node)[0]
            except:
                continue

            to_remove.extend([neighbor, node])

            edges.add(tuple(sorted((node, neighbor))))

            parents |= set(tree.neighbors(neighbor))
            parents.remove(node)

            tree.remove_nodes_from([node, neighbor])

        if not to_remove:
            return None

        parents -= set(to_remove)

    return list(edges)
