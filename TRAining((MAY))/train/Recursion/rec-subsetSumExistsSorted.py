def findSubset(arr, sum, idx = 0):
    if sum == 0:
        return True
    if idx == len(arr):
        return False
    return findSubset(arr, sum - arr[idx], idx - 1) or findSubset(arr, sum, idx - 1)

arr = list(map(int, input().split()))
k = int(input('sum: '))
print(findSubset(arr, k))
