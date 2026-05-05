import heapq

def a_star(graph, start, goal, h):

    open_list = []
    closed = set()

    start.g = 0
    start.h = h[start.name]
    start.f = start.g + start.h

    heapq.heappush(open_list, start)

    while open_list:

        current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct(current)

        closed.add(current)

        for neighbor, cost in graph.get_neighbors(current):

            if neighbor in closed:
                continue

            g_new = current.g + cost

            if g_new < neighbor.g:
                neighbor.g = g_new
                neighbor.h = h[neighbor.name]
                neighbor.f = neighbor.g + neighbor.h
                neighbor.parent = current

                heapq.heappush(open_list, neighbor)

    return None


def reconstruct(node):
    path = []
    while node:
        path.insert(0, node.name)
        node = node.parent
    return path