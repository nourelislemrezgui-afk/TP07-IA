class Graph:
    def __init__(self):
        self.adj = {}

    def add_node(self, node):
        self.adj[node] = []

    def add_edge(self, src, dst, cost):
        self.adj[src].append((dst, cost))

    def get_neighbors(self, node):
        return self.adj.get(node, [])