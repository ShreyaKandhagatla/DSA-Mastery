#job scheduling cost
from bisect import bisect_right

def job_scheduling(start, end, cost):
    n = len(start)
    dp = [0] * n
    dp[0] = cost[0]

    for i in range(1, n):
        for j in range(i):
            if end[j] <= start[i]:
                dp[i] = max(dp[i], dp[j] + cost[i])
                print(i, dp[i])
        if dp[i] == 0:
            dp[i] = cost[i]
    # print(dp)
    return max(dp)
start = [1, 2, 4, 6, 5, 7]
end   = [3, 5, 6, 7, 8, 9]
cost  = [5, 6, 5, 4, 11, 2]

print("Maximum Cost:", job_scheduling(start, end, cost))
