import heapq

def ucs(graph, start, goal):

    open_list = []
    closed = set()

    start.g = 0
    heapq.heappush(open_list, (start.g, start))

    while open_list:

        _, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct(current)

        closed.add(current)

        for neighbor, cost in graph.get_neighbors(current):

            if neighbor in closed:
                continue

            g_new = current.g + cost

            if g_new < neighbor.g:
                neighbor.g = g_new
                neighbor.parent = current
                heapq.heappush(open_list, (neighbor.g, neighbor))

    return None


def reconstruct(node):
    path = []
    while node:
        path.insert(0, node.name)
        node = node.parent
    return path