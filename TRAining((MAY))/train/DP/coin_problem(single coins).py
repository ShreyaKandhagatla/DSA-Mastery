'''
COIN CHANGE
COIN PROBLEM USING DYNAMIC PROGRAMMING
3 conditions:
1.if its 0 then calculate difference btw that coin and then see if its one or not
2. then see the difference of that number in the previous row and then find if its one or 0 and replace it with the same 0 or 1
3.if its already one then directly copy one

'''
coin = [2, 3, 4, 5]
amt = 13

r, c = len(coin), amt + 1
dp = [[0] * c for i in range(r)]

for i in range(r):
    dp[i][0] = 1

for i in range(r):
    for j in range(c):
        if j < coin[i]:
            dp[i][j] = dp[i-1][j]
        elif dp[i - 1][j - coin[i]]:
            dp[i][j] = 1
        elif dp[i - 1][j]:
            dp[i][j] = 1

for row in dp:
    print(row)

print(dp[-1][-1])
    