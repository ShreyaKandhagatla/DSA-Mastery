def dfs(maze, i, j, visited):
    if i == len(maze) - 1 and j == len(maze[0]) - 1:
        return 1
    if i < 0 or j < 0 or i == len(maze) or j == len(maze[0]) or maze[i][j] == 0 or (i, j) in visited:
        return 0
    visited.add((i, j))
    paths = dfs(maze, i + 1, j, visited) + dfs(maze, i - 1, j, visited) + dfs(maze, i, j - 1, visited) + dfs(maze, i, j + 1, visited)
    visited.remove((i, j))
    return paths

# maze = [[1, 0, 0, 0, 0], [1, 1, 1, 0, 0], [1, 0, 1, 0, 0],[1, 0, 1, 1, 1],[1, 1, 1, 0, 1]]
# maze = [[1, 0, 0], [1, 1, 0], [1, 1, 1]]
maze = [[1,0,0,0,0],[1,0,1,1,1],[1,0,1,0,1],[1,1,1,0,1],[0,0,0,0,1]]
print(dfs(maze, 0, 0, set()))