# coding: utf-8


class UnionFind:
    # union-find structure
    def __init__(self):
        self.weights = {}
        self.parents = {}

    def __getitem__(self, object):

        if object not in self.parents:
            self.parents[object] = object
            self.weights[object] = 1
            return object

        path = [object]
        root = self.parents[object]

        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        for ancestor in path:
            self.parents[ancestor] = root

        return root

    def __iter__(self):
        return iter(self.parents)

    def union(self, *objects):
        roots = [self[x] for x in objects]

        max_rank = max(roots, key=lambda r: self.weights[r])

        for r in roots:
            if r != max_rank:
                self.weights[max_rank] += self.weights[r]
                self.parents[r] = max_rank


def get_spanning_tree(g):
    """
    Parameters
    ----------
    g : Graph
        Weighted undirected graph, with heights representing the maximum heights allowed on the route from u to v

    Returns
    -------
    bottleneck : int The smallest height in the spanning tree
    tree_edges : list of (int, int) tuples, each tuple representing an edge in the spanning tree
    """

    subtrees = UnionFind()
    edges = sorted(g.edges(data=True), key=lambda t: t[2].get("weight", 1), reverse=True)

    tree_edges = []
    bottleneck = float("inf")

    for u, v, d in edges:
        if subtrees[u] != subtrees[v]:
            tree_edges.append((u, v))
            bottleneck = min(d["weight"], bottleneck)
            subtrees.union(u, v)

    return bottleneck, tree_edges
