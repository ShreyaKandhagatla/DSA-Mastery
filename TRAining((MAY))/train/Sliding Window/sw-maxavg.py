def findMaxAverage(nums, k):
    total = sum(nums[:k])
    max_avg = total
    for i in range(k, len(nums)):
        total += nums[i] - nums[i - k]
        max_avg = max(max_avg, total)
    return max_avg / k

k = int(input())
nums = list(map(int, input().split()))
print(findMaxAverage(nums, k))