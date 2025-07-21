def countSubsets(arr, sum, subset = [], i = 0):
    if sum == 0:
        print(subset)
        return
    if i == len(arr):
        return
    countSubsets(arr, sum - arr[i], subset + [arr[i]], i + 1)
    countSubsets(arr, sum, subset, i + 1)

arr = list(map(int, input().split()))
k = int(input())

