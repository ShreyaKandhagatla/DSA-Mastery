def sort(strings):
    n = len(strings)

    for j in range(n - 1):
        swap = False
        for i in range(n - 1 - j):
            if ord(strings[i + 1][0]) < ord(strings[i][0]):
                swap = True
                strings[i], strings[i + 1] = strings[i + 1], strings[i]
            if ord(strings[i + 1][0]) == ord(strings[i][0]) and ord(strings[i + 1][1]) < ord(strings[i][1]):
                strings[i], strings[i + 1] = strings[i + 1], strings[i]
        if not swap:
            break
    
    return strings

strings = list(input().split())
print(*sort(strings))
    