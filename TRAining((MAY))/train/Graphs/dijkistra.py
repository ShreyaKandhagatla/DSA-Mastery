import heapq

def dijkstra(graph, start):
    # Distance dictionary: stores shortest distance from start to each node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue: stores (distance, node)
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Skip if a shorter path to current_node was already found
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

print(f"Shortest paths from {start_node}:")
for node in shortest_paths:
    print(f"{node}: {shortest_paths[node]}")
