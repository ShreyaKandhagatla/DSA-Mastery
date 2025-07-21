#if array is sorted

def singleNumber(nums):
    ans = nums[-1]
    for i in range(0, len(nums) - 1, 2):
        if nums[i] != nums[i+1]:
            ans = nums[i]
            break

    return ans

# using binary srch
# def singleNumber(nums):
#     if len(nums) == 1:
#         return nums[0]
#     if len(nums) % 2 == 0:
#         return "No answer"
    
#     l, r = 0, len(nums)-1
#     while l < r:
#         mid = (l + r) // 2
#         if mid == 0 or mid == len(nums) - 1:
#             return nums[mid]
#         if (mid - l) % 2 == 0:
#             l = mid + 1
#         elif (r - mid) % 2 == 1:
#             r = mid - 1
#         else:
#             return nums[mid]

nums = list(map(int, input().split()))
print(singleNumber(nums))
