hurdles = set([(2,1),(4,1),(5,2),(3,5)])
n = 5
x, y = 2, 3

def dfs(i, j):
    if i < 0 or j < 0 or i >= n or j >= n or (i+1, j+1) in hurdles:
        return 0
    if i == n-1 and j == n-1:
        return 1
    
    return dfs(i+1, j) + dfs(i, j+1)

print(dfs(x-1, y-1))
