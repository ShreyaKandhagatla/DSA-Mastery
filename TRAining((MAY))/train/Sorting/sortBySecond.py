def sortBySecond(arr):
    n = len(arr)

    for j in range(n - 1):
        swap = False
        for i in range(n - 1 - j):
            if arr[i + 1][1] < arr[i][1]:
                swap = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                # print(arr)
        if not swap:
            break
    
    return arr

arr = [[2,8],[5,1],[1,3],[7,2]]
print(*sortBySecond(arr))