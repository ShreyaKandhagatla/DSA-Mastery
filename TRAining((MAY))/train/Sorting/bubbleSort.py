def bubbleSort(arr):
    n = len(arr)

    for j in range(n - 1):
        swap = False
        for i in range(n - 1 - j):
            if arr[i + 1] < arr[i]:
                swap = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                # print(arr)
        if not swap:
            break
    
    return arr
    

arr = list(map(int, input().split()))
print(*bubbleSort(arr))