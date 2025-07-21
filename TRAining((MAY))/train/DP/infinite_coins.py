#coin change infinite coins
coin = [2, 3, 4, 5]
amt = 12

r, c = len(coin), amt + 1
dp = [[0] * c for i in range(r)]

for i in range(r):
    dp[i][0] = 1

for i in range(r):
    for j in range(c):
        if j < coin[i]:
            dp[i][j] = dp[i-1][j]
        elif dp[i][j - coin[i]]:
            dp[i][j] = dp[i][j - coin[i]]
        # elif dp[i - 1][j]:
        #     dp[i][j] = dp[i - 1][j]
        # elif dp[i - 1][j % coin[i]]:
        #     dp[i][j] = dp[i - 1][j % coin[i]]

for row in dp:
    print(row)

print(dp[-1][-1])