def peak(nums):
    n = len(nums)
    if nums[0] > nums[1]:
        return nums[0]
    if nums[n - 1] > nums[n - 2]:
        return nums[n - 1]
    
    l, r = 1, n - 2
    while l <= r:
        mid = (l + r)//2
        if nums[mid - 1] < nums[mid] > nums[mid + 1]:
            return nums[mid]
        elif nums[mid] < nums[mid + 1]:
            l = mid + 1
        else:
            r = mid - 1
    
    return -1

# nums = [2,3,4,6,3,2,1,5,8,10,1,4,2]
# nums = [8,2]
nums = [2, 8]
print(peak(nums))