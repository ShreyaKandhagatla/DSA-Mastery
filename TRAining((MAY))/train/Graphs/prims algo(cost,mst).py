'''
from collections import defaultdict
import heapq

def prim_with_dict(graph, start):
    visited = set()
    min_heap = [(0, start, None)]  # (weight, node, parent)
    mst = []
    parent = {}
    key = {node: float('inf') for node in graph}
    key[start] = 0

    while min_heap:
        weight, u, par = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        parent[u] = par
        if par is not None:
            mst.append((par, u, weight))
        for v, w in graph[u]:
            if v not in visited and w < key[v]:
                key[v] = w
                heapq.heappush(min_heap, (w, v, u))
    
    return mst, parent

# Sample graph as dictionary
graph = defaultdict(list)
edges = [
    ('A', 'B', 2),
    ('A', 'D', 1),
    ('B', 'D', 3),
    ('B', 'E', 10),
    ('C', 'E', 5),
    ('C', 'F', 8),
    ('D', 'E', 4),
    ('E', 'F', 6)
]

# Build the undirected graph
for u, v, w in edges:
    graph[u].append((v, w))
    graph[v].append((u, w))

mst, parent = prim_with_dict(graph, 'A')
print("Prim's MST using dictionary:")
for u, v, w in mst:
    print(f"{u} - {v}: {w}")   
'''
from collections import defaultdict
import heapq

def prim_with_dict(graph, start):
    visited = set()
    min_heap = [(0, start, None)] # (weight, current_node, parent)
    mst = []
    parent = {}
    key = {node: float('inf') for node in graph}
    key[start] = 0

    while min_heap:
        weight, u, par = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        parent[u] = par
        if par is not None:
            mst.append((par, u, weight))
        for v, w in graph[u]:
            if v not in visited and w < key[v]:
                key[v] = w
                heapq.heappush(min_heap, (w, v, u))
    
    return mst, parent

# Sample graph as dictionary
graph = defaultdict(list)
edges = [
    ('A', 'B', 2),
    ('A', 'D', 1),
    ('B', 'D', 3),
    ('B', 'E', 10),
    ('C', 'E', 5),
    ('C', 'F', 8),
    ('D', 'E', 4),
    ('E', 'F', 6)
]

# Build the undirected graph
for u, v, w in edges:
    graph[u].append((v, w))
    graph[v].append((u, w))

# Run Prim's algorithm
mst, parent = prim_with_dict(graph, 'A')

# Calculate total cost of MST
total_cost = sum(w for _, _, w in mst)
print("Cost of Prim's MST:", total_cost)


n