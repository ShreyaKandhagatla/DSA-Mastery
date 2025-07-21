def search(matrix, k):
    r, c = len(matrix), len(matrix[0])
    l, r = 0, r - 1
    while l <= r:
        midRow = (l + r) // 2
        if matrix[midRow][0] <= k <= matrix[midRow][c-1]:
            l1, r1 = 0, c - 1
            while l1 <= r1:
                midCol = (l1 + r1) // 2
                if matrix[midRow][midCol] == k:
                    return f'Found at {midRow}, {midCol}'
                elif k < matrix[midRow][midCol]:
                    r1 = midCol - 1
                else:
                    l1 = midCol + 1
            return 'Not Found'
        elif k < matrix[midRow][0]:
            r = midRow - 1
        else:
            l = midRow + 1
    return 'Not Found'
matrix = [[2,3,7,8], [9,15,20,22], [23,26,35,37],[38,39,42,43]]
k = 23
# k = 50
# k = 21
print(search(matrix, k))