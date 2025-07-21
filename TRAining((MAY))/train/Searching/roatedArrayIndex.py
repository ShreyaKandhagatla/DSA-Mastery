def rotatedIndex(nums):
    l, r = 0, len(nums) - 1

    while l < r:
        mid = (l + r)//2
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid
    
    return l

nums = [15,18,20,22,2,5,8,10,12,13]
print(rotatedIndex(nums))