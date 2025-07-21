'''
Minimum value WHEN INFINITE COINS ARE GIVEN
'''
#coin change, infinite coins, but minimum number of coins
coins = [2, 3, 4, 5]
amt = 12

#1d matrix, can also use 2d matrix
r, c = len(coins), amt + 1
dp = [0] * c

for i in range(r):
    for j in range(i, c):
        print(i, dp)
        if j == coins[i]:
            dp[j] = 1
        elif dp[j - coins[i]] and dp[j]:
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        elif dp[j - coins[i]]:
            dp[j] = dp[j - coins[i]] + 1
            
print(dp)
