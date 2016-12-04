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


def get_longest_path(digraph):
    """Return one longest path in the given digraph, or return None if the graph is cyclic.

    To run doctests:
        python -m doctest -v solution.py
    >>> from networkx import DiGraph
    >>> get_longest_path(DiGraph({1:[2], 2: [1]}))
    >>> get_longest_path(DiGraph({1:[2], 2:[3], 3:[4]}))
    [1, 2, 3, 4]

    Parameters
    ----------
    digraph : DiGraph

    Returns
    -------
    path : list
        List of vertices in the order they appear in the path.
        E.g. if the path is 3 -> 2 -> 1, return [3, 2, 1]. If
        the graph is cyclic, return None.
    """

    try:
        dist = {}
        for node in topo_sort(digraph):
            pairs = [(dist[v][0] + 1, v) for v in digraph.predecessors(node)]
            dist[node] = max(pairs) if pairs else (0, node)

        node, (length, _) = max(dist.items(), key=lambda x: x[1])

        path = []
        while length > 0:
            path.append(node)
            length, node = dist[node]

        return list(reversed(path))

    except:
        return None
