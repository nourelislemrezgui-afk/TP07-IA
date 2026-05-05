from node import Node
from graph import Graph

def load_graph(cities_file, distances_file):

    graph = Graph()
    nodes = {}

    # ---- load cities ----
    with open(cities_file, "r") as f:
        for line in f:
            name = line.strip()
            node = Node(name)
            nodes[name] = node
            graph.add_node(node)

    # ---- load edges ----
    with open(distances_file, "r") as f:
        for line in f:
            src, dst, cost = line.strip().split(",")

            graph.add_edge(
                nodes[src],
                nodes[dst],
                
                float(cost)
            )

    return graph, nodes
    