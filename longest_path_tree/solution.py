# coding: utf-8
def bfs(graph, source):
    inf = float("inf")
    dist = {}

    for node in graph.nodes_iter():
        dist[node] = inf

    dist[source] = 0
    previous = {}
    Q = [source]
    while Q:
        u = Q.pop(0)
        for v in graph.neighbors(u):
            if dist[v] == inf:
                Q.append(v)
                previous[v] = u
                dist[v] = dist[u] + 1
    return sorted(dist.items(), key=lambda x: x[1])[::-1], previous


def get_longest_path(graph):
    """Return one longest path in the given graph or None, if the graph
    is cyclic.
    
    To run doctests:
        python3 -m doctest -v solution.py
    >>> from networkx import Graph
    >>> get_longest_path(Graph({1: []})) == [1]
    True
    >>> get_longest_path(Graph({1: [2]})) in ([1, 2], [2, 1])
    True
    >>> get_longest_path(Graph({1: [2], 2: [3], 3: [1]}))
    >>> get_longest_path(Graph({1: [2], 2: [3], 3: [4], 4:[]})) in ([1, 2, 3, 4], [4, 3, 2, 1])
    True
    >>> get_longest_path(Graph({3: [4], 4: [1], 1: [2, 5], 5:[6]})) in ([3, 4, 1, 5, 6], [6, 5, 1, 4, 3])
    True

    Parameters
    ----------
    graph : Graph

    Returns
    -------
    path : list or None
        List of vertices in the order they appear in the path.
        E.g. if the path is 3 -> 2 -> 1, return [3, 2, 1]. Return
        None if graph is cyclic.
    """
    if len(graph) == 0:
        return None

    if len(graph) == 1:
        return graph.nodes()

    # A connected graph with no cycles has n-1 edges.
    if graph.number_of_edges() != len(graph) - 1:
        return None

    path, previous = bfs(graph, graph.nodes()[0])
    u, dist = path[0]
    path, previous = bfs(graph, source=u)

    v, dist = path[0]
    final_path = [v]
    next_node = previous[v]
    while next_node in previous:
        final_path.append(next_node)
        next_node = previous[next_node]

    final_path.append(next_node)

    return final_path
