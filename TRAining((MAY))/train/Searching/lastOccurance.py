def lastOccurance(nums, k):
    for i in range(len(nums)-1, -1, -1):
        if nums[i] == k:
            return i

