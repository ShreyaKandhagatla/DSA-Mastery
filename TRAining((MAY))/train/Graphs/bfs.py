from collections import deque, defaultdict

edges = [(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
graph = defaultdict(list)
for i,j in edges:
    graph[i].append(j)
    graph[j].append(i)

def bfs(n):
    queue = deque([n])
    visited = set([n])

    while queue:
        node = queue.popleft()
        print(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)

bfs(5)