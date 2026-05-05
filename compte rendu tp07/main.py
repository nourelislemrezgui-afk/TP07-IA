from loader import load_graph
from astar import a_star
from ucs import ucs

# ---- load data ----
graph, nodes = load_graph("data/cities.csv", "data/distances.csv")

start = nodes["Tunis"]
goal = nodes["Tozeur"]

# heuristics (static)
h = {
    "Tunis": 400,
    "Sousse": 300,
    "Kairouan": 250,
    "Sfax": 230,
    "Gafsa": 100,
    "Tozeur": 0,
    "Gabes": 180,
    "ElKef": 320
}

print("A*:", a_star(graph, start, goal, h))

# reset nodes manually
for n in nodes.values():
    n.g = float('inf')
    n.parent = None

print("UCS:", ucs(graph, start, goal))
