def formSubset(arr, idx = 0, subset = []):
    if idx == len(arr):
        ans.append(subset)
        return
    formSubset(arr, idx+1, subset+[arr[idx]]) # pick
    formSubset(arr, idx+1, subset) # dont pick

ans = []
arr = list(map(int, input().split()))
print(formSubset(arr))
print(ans)
