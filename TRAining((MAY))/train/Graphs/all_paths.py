'''All possible paths in the graph from two points,
#for printing count of all paths
length of all paths
'''
'''
from collections import defaultdict
def all_paths(u,v,path=[],c=0):
    path.append(u)
    if(u==v):
        print(path)
        
        path.pop()
        return
    for i in d[u]:
        if(i not in path):
            all_paths(i,v,path)
            
    path.pop()
    return
    
                
graphs=[(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
d=defaultdict(list)
for i,j in graphs:
    d[i].append(j)
    d[j].append(i)
print(d)
all_paths(5,3)
'''
'''
from collections import defaultdict

def all_paths(u, v, path=None):
    if path is None:
        path = []

    path.append(u)

    if u == v:
        all_paths.count += 1
        print(path[:])  # Print current valid path
    else:
        for neighbor in d[u]:
            if neighbor not in path:  # Avoid revisiting nodes
                all_paths(neighbor, v, path)

    path.pop()  # Backtrack


# Build graph as adjacency list
graphs = [(5, 2), (5, 7), (5, 8), (2, 7), (2, 8), (8, 7), (8, 3), (2, 3)]
d = defaultdict(list)
for u, v in graphs:
    d[u].append(v)
    d[v].append(u)

# Count paths from 5 to 3
all_paths.count = 0
all_paths(5, 3)
print("Total number of paths from 5 to 3:", all_paths.count)

'''
from collections import defaultdict

def all_paths(u, v, path=None):
    if path is None:
        path = []

    path.append(u)

    if u == v:
        all_paths.count += 1
        print(f"Path {all_paths.count}: {path[:]} ----> Length: {len(path) - 1}")
    else:
        for neighbor in d[u]:
            if neighbor not in path:  # Prevent revisiting nodes
                all_paths(neighbor, v, path)

    path.pop()  # Backtrack


# Graph edges (undirected)
graphs = [(5, 2), (5, 7), (5, 8), (2, 7), (2, 8), (8, 7), (8, 3), (2, 3)]

# Build adjacency list
d = defaultdict(list)
for u, v in graphs:
    d[u].append(v)
    d[v].append(u)

# Run path finder from node 5 to node 3
all_paths.count = 0
print("All possible paths from 5 to 3 with their lengths:")
all_paths(5, 3)
print("Total number of paths:", all_paths.count)
