def find(nums, k):
    maximum = max(nums)
    numbers = [0] * (maximum + 1)
    for num in nums:
        numbers[num] = 1
    
    print(nums)
    i = maximum
    while k > 0 and i >= 0:
        if numbers[i] == 1:
            k -= 1
        if k == 0:
            return i
        i -= 1
    
    return 'Does Not Exist'

nums = [2,13,4,2,9,9,5,8,7,13,3]
k = 3
print(find(nums, k))
