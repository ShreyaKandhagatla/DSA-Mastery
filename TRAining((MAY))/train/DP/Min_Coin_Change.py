#Min coin change
coin = [2, 3, 4, 5]
amt = 13

r, c = len(coin), amt + 1
dp = [[0] * c for i in range(r)]
dp[0][coin[0]] = 1

for i in range(1, r):
    for j in range(c):
        if j < coin[i]:
            dp[i][j] = dp[i-1][j]
        elif j == coin[i]:
            dp[i][j] = 1
        elif dp[i - 1][j] and dp[i - 1][j - coin[i]]:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - coin[i]] + 1)
        elif dp[i - 1][j - coin[i]]:
            dp[i][j] = dp[i - 1][j - coin[i]] + 1
        elif dp[i - 1][j]:
            dp[i][j] = dp[i - 1][j]
        

for row in dp:
    print(row)

print(dp[-1][-1])