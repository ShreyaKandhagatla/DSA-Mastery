def findSubset(arr, k, idx = 0, sum = 0):
    if sum == k:
        return True
    if idx == len(arr):
        return False
    return findSubset(arr, k, idx+1, sum + arr[idx]) or findSubset(arr, k, idx+1, sum)

arr = list(map(int, input().split()))
k = int(input('sum: '))
print(findSubset(arr, k))
