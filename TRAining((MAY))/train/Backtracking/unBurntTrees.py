from collections import deque

def findUnburntTrees(matrix, x, y):
    r = c = len(matrix)
    x = x - 1
    y = y - 1
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def dfs(i, j):
        if i < 0 or j < 0 or i == r or j == c or matrix[i][j] == 0:
            return
        
        matrix[i][j] = 0
        for dr, dc in directions:
            dfs(i+dr, j+dc)
    
    dfs(x,y)
    unburnt = 0
    for i in range(r):
        for j in range(c):
            if matrix[i][j]:
                unburnt += 1
    
    return unburnt


matrix = [[1,0,0,1,1,1], [1,1,1,0,0,0], [0,0,1,1,1,1], [1,1,1,0,0,0], [0,0,0,0,0,1], [1,0,0,1,0,0]]
x = 3
y = 6
print(findUnburntTrees(matrix, x, y))