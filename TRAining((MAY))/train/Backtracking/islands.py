from collections import deque
def findLand(matrix):
    visited = set()
    def bfs(i, j):
        queue = deque([(i, j)])
        while queue:
            i, j = queue.popleft()
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if i+1 < r and matrix[i+1][j]:
                queue.append((i+1, j))
            if i-1 >= 0 and matrix[i-1][j]:
                queue.append((i-1, j))
            if j-1 >= 0 and matrix[i][j-1]:
                queue.append((i, j-1))
            if j+1 < c and matrix[i][j+1]:
                queue.append((i, j+1))
        
        return

    r, c = len(matrix), len(matrix[0])
    cnt = 0
    for i in range(r):
        for j in range(c):
            if (i, j) not in visited and matrix[i][j]:
                bfs(i, j)
                cnt += 1
    
    return cnt

# matrix = [[0, 1, 1, 0, 1], [1, 1, 0, 0, 1], [0, 0, 0, 1, 1], [0, 1, 0, 0, 0]]
matrix = [[1,0,0,1,1],[1,0,0,0,1],[0,0,0,1,0],[1,0,0,0,0],[1,0,0,0,1]]
print(findLand(matrix))