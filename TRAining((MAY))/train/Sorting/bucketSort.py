def sort(arr):
    hm = {}

    for num in arr:
        if num not in hm.keys():
            hm[num] = 0
        hm[num] += 1

    bucket = [[] for _ in range(len(arr))]
    for k, v in hm.items():
        bucket[v].append(k)
    print(bucket)

    new = []
    for i in range(len(bucket)):
        for j in range(len(bucket[i])):
            new.extend([bucket[i][j]] * i)
    
    print(new)

sort([1,2,2,3,1,1,5,3,2])
