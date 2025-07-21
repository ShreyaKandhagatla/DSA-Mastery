from math import log

pos = 5

def dfs(pos, binary):
    if len(binary) == pos:
        print(binary)
        return
    dfs(pos, binary + '0')
    dfs(pos, binary + '1')

dfs(pos, '')