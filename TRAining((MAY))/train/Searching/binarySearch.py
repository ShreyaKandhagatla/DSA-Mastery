def binarySearch(nums, k):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = l + (r - l)//2

        if nums[mid] == k:
            print(l,r)
            return f'Found at {mid}'
        if k < nums[mid]:
            r = mid - 1
        else:
            l = mid + 1
    
    return 'Not Found'

nums = [2,3,5,6,7,7,8,9,10,10,10,13,15]
k = 7
print(binarySearch(nums, k))