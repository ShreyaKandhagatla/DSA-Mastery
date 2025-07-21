def merge_sort(x):
    m = len(x) // 2
    if len(x) == 1:
        return x
    l = merge_sort(x[:m])
    r = merge_sort(x[m:])
    return merge(l, r)

def merge(l, r):
    p1, p2 = 0, 0
    res = []

    while p1 < len(l) and p2 < len(r):
        if l[p1] <= r[p2]:
            res.append(l[p1])
            p1 += 1
        else:
            res.append(r[p2])
            p2 += 1
    
    while p1 < len(l):
        res.append(l[p1])
        p1 += 1
    
    while p2 < len(r):
        res.append(r[p2])
        p2 += 1
    
    return res