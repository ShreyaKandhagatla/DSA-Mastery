def findMin(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:  # Min must be in right half
            left = mid + 1
        else:  # Min could be mid or in left half
            right = mid
    return nums[left]

nums = [4,5,6,7,0,1,2]
print(findMin(nums))


