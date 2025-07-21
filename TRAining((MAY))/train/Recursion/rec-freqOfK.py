def count(nums, k, idx=0):
    if idx == len(nums):
        return 0
    return count(nums, k, idx+1) + (1 if nums[idx] == k else 0)

nums = list(map(int, input().split()))
k = int(input('K: '))
print(count(nums, k))