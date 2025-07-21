def lastOccurrence(nums, k):
    l, r = 0, len(nums) - 1
    ans = 'Not Found'

    while l <= r:
        mid = (l + r)//2

        if nums[mid] == k:
            ans = mid
            l = mid + 1
        elif k < nums[mid]:
            r = mid - 1
        else:
            l = mid + 1
    
    return ans

nums = [2,3,5,6,7,7,8,9,10,10,10,13,15]
k = 7
print(lastOccurrence(nums, k))