def bubbleSort(chars):
    n = len(chars)

    for j in range(n - 1):
        swap = False
        for i in range(n - 1 - j):
            if ord(chars[i + 1]) < ord(chars[i]):
                swap = True
                chars[i], chars[i + 1] = chars[i + 1], chars[i]
                # print(chars)
        if not swap:
            break
    
    return chars
    

chars = list(input().split())
print(*bubbleSort(chars))