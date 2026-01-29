import heapq

# Graph representation
graph_nodes = {
    'A': [('B', 6), ('F', 3)],
    'B': [('A', 6), ('C', 3), ('D', 2)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 8)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
    'F': [('A', 3), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('I', 3)],
    'H': [('F', 7), ('I', 2)],
    'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)],
    'J': []
}

# Heuristic values
heuristic_values = {
    'A': 11,
    'B': 6,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 5,
    'H': 3,
    'I': 1,
    'J': 0
}

# A* Search Algorithm
def a_star_search(start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic_values[start], 0, start, [start]))

    closed_set = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            return path, g

        if current in closed_set:
            continue

        closed_set.add(current)

        for neighbor, cost in graph_nodes[current]:
            if neighbor not in closed_set:
                new_g = g + cost
                new_f = new_g + heuristic_values[neighbor]
                heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')

# Driver code
path, cost = a_star_search('A', 'J')

print("Path found:", path)
print("Total cost:", cost)
