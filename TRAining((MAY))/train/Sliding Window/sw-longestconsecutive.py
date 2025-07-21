def longestConsecutiveSubarray(nums):
    ans = 1
    count = 1
    for i in range(len(nums) - 1):
        if nums[i] + 1 == nums[i + 1]:
            count += 1
        else:
            count = 1
        ans = max(ans, count)
    return ans

nums = list(map(int, input().split()))
print(longestConsecutiveSubarray(nums))