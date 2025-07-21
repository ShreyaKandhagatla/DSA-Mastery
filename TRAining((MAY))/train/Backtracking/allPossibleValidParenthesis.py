def dfs(n, opened = 0, closed = 0, s = ''):
    if opened > n or closed > n or closed > opened:
        return
    if opened == closed == n:
        print(s)
    dfs(n, opened+1, closed,s+'(')
    dfs(n, opened, closed+1, s+')')

dfs(3)