def find(coins, amount, idx = 0, cnt = 0):
    if amount == 0:
        return cnt
    if idx == len(coins) or amount < 0:
        return float('inf')
    return min(find(coins, amount - coins[idx], idx + 1, cnt + 1), 
               find(coins, amount, idx + 1, cnt))

coins = list(map(int, input('Coins: ').split()))
amount = int(input('Amount: '))
ans = find(coins, amount)
print(ans if ans != float('inf') else -1)