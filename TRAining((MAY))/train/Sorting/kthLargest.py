def find_kth_largest(arr, k):
    n = len(arr)

    for j in range(n - 1):
        swap = False
        for i in range(n - 1 - j):
            if arr[i + 1] < arr[i]:
                swap = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                # print(arr)
        if j == 0 or not swap:
            break
    
    return arr[-k]

arr = [2,5,8,6,3,1,9,4,7]
print(find_kth_largest(arr, 4))