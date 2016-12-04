def is_bipartite(g):
    colored_nodes = {}
    for n in g:
        # test if already colored or isolated
        if n in colored_nodes or len(g[n]) == 0:
            continue

        queue = [n]
        colored_nodes[n] = 1  # use 1 by default

        while queue:
            v = queue.pop()
            # opposite color
            c = 1 - colored_nodes[v]

            for w in g.neighbors(v):
                if w in colored_nodes:
                    if colored_nodes[w] == colored_nodes[v]:
                        raise Exception("not bipartite")
                else:
                    colored_nodes[w] = c
                    queue.append(w)

    isolated_nodes = [n for (n, d) in g.degree_iter() if d == 0]
    colored_nodes.update(dict.fromkeys(isolated_nodes, 0))

    X = set(n for n in colored_nodes if colored_nodes[n] == 1)
    return sorted(list(X))


def get_bipartition(g):
    """For a bipartite graph, returns a list of nodes S s.t. (S, V\S) is a bipartition.

    >>> from networkx import Graph
    >>> get_bipartition(Graph({1: [2, 3], 2: [], 3: []})) in ([1], [2, 3])
    True

    Parameters
    ----------
    g : Graph

    Returns
    -------
    partition : list
        List of all nodes on one side of the partition.
    None if the graph is not bipartite.
    """

    try:
        return is_bipartite(g)
    except:
        return None

# Create a simple line graph g: "(1)->(2)->(3)"
# (The creation parameter is a dict of {node: list_of_neighbors},
# but this is not something you will be needing in your code.)
# >>> from networkx import Graph
# >>> g = Graph({1: [2], 2: [3]})
# >>> g.number_of_nodes()
# 3

# Example. Iterate over the nodes and mark them as visited
# >>> visited = set()
# >>> for node in g.nodes_iter(): # There is also g.nodes(), which returns a list
# ...    # do some work here
# ...    visited.add(node)

# Example. Given a Node v, get all nodes s.t. there is an edge between
# v and that node
# >>> g.neighbors(1)
# [2]

# Example. Get the edges of the graph:
# >>> e.edges() # as with nodes, there is also g.edges_iter()
# [(1, 2), (2, 3)]

# For more information, consult the NetworkX documentation:
# https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html
