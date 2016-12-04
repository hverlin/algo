# coding: utf-8


def bfs(graph, source):
    inf = float("inf")
    dist = {}

    for node in graph.nodes_iter():
        dist[node] = inf

    dist[source] = 0
    Q = [source]
    while Q:
        u = Q.pop(0)
        for v in graph.neighbors(u):
            if dist[v] == inf:
                Q.append(v)
                dist[v] = dist[u] + 1
            elif dist[v] != inf and dist[v] != dist[u] - 1:
                return dist[v] + dist[u] + 1
    return None


def get_length_of_shortest_cycle(g):
    """Find the length of the shortest cycle in the graph if a cycle exists.

    To run doctests:
        python -m doctest -v solution.py
    >>> from networkx import Graph
    >>> get_length_of_shortest_cycle(Graph({1: [2, 3], 2: [], 3: []})) 
    >>> get_length_of_shortest_cycle(Graph({1: [3], 2: [1], 3: [2]}))
    3
    
    Parameters
    ----------
    g : Graph

    Returns
    -------
    length : int or None
        Length of the shortest cycle, or None if there is no cycle.
    """
    l = [x for x in [bfs(g, node) for node in g.nodes_iter()] if x is not None]
    return min(l) if len(l) > 0 else None
