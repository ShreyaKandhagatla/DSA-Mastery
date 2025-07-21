from collections import defaultdict

graph = defaultdict(list)
edges = [(5,2,3), (5,7,2), (5,8,1), (2,7,2), (2,8,4), (8,7,1), (8,3,3), (2,3,2)]

for u, v, w in edges:
    graph[u].append([v, w])
    graph[v].append([u, w])

def allPaths(u, v, path, cost):
    path.append(u)
    if u == v:
        print(path, cost)
    for i, w in graph[u]:
        if i not in path:
            cost += w
            allPaths(i, v, path, cost)
            cost -= w
    
    path.pop()

allPaths(5,3,[],0)