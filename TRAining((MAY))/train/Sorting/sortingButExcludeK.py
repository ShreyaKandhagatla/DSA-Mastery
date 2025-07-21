def bubbleSort(arr, k):
    n = len(arr)

    for j in range(n - 2*k -1):
        swap = False
        for i in range(k, n - k - 1 - j):
            if arr[i + 1] < arr[i]:
                swap = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        if not swap:
            break
    
    return arr
    

arr = list(map(int, input().split()))
k = int(input())
print(*bubbleSort(arr, k))