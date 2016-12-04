# coding: utf-8


def topo_sort(graph):
    ancestors = set()
    visited = set()
    ordered_nodes = []

    def dfs_search(node):
        ancestors.add(node)

        for w in graph[node]:
            if w in ancestors:
                raise Exception("cyclic.")

            if w not in visited:
                dfs_search(w)

        ancestors.remove(node)
        visited.add(node)
        ordered_nodes.append(node)

    for node in graph.nodes_iter():
        if node not in visited:
            dfs_search(node)

    else:
        return ordered_nodes[::-1]


def get_topological_sorting(digraph):
    """Given a directed graph, returns a list of nodes in topological order.

    To run doctests:
        python -m doctest -v solution.py
    >>> from networkx import DiGraph
    >>> get_topological_sorting(DiGraph({1: [], 2: [1], 3: [2]}))
    [3, 2, 1]
    >>> get_topological_sorting(DiGraph({1: [3], 2: [1], 3: [2]}))

    Parameters
    ----------
    digraph : DiGraph, a graph container instance

    Returns
    -------
    sorting : list of integers corresponding to node indices in the graph
        None, if there is no topological sorting (i.e., the graph is
        cyclic.
    """
    try:
        return topo_sort(digraph)
    except:
        return None