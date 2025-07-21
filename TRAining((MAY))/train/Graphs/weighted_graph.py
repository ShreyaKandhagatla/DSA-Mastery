#Conerting weighted dictionary into defaultdict
from collections import defaultdict

graph = defaultdict(list)
edges = [(5,2,3), (5,7,2), (5,8,1), (2,7,2), (2,8,4), (8,7,1), (8,3,3), (2,3,2)]

for u, v, w in edges:
    graph[u].append([v, w])
    graph[v].append([u, w])

print(graph)