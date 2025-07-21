# def findNum(nums, idx, prev, k):
#     if k == 0:
#         return True
#     if idx == len(nums):
#         return False
#     if nums[idx] == prev:
#         return findNum(nums, idx+1, prev, k-1)
#     else:
#         return findNum(nums, idx+1, prev, k)

# nums = list(map(int, input().split()))
# k = int(input('K: '))
# seen = set()
# for i in range(len(nums)):
#     if nums[i] in seen:
#         continue
#     seen.add(nums[i])
#     if findNum(nums, i, nums[i], k):
#         print('ans: ',nums[i])
#         break

from collections import defaultdict

def buildHashMap(nums, idx=0, freq=None):
    if freq is None:
        freq = defaultdict(int)
    if idx == len(nums):
        return freq
    freq[nums[idx]] += 1
    return buildHashMap(nums, idx + 1, freq)

def findNum(freq_items, idx, k):
    if idx == len(freq_items):
        return None
    key, val = freq_items[idx]
    if val == k:
        return key
    return findNum(freq_items, idx + 1, k)

nums = list(map(int, input().split()))
k = int(input('K: '))
freq = buildHashMap(nums)
print(findNum(list(freq.items()), 0, k))
