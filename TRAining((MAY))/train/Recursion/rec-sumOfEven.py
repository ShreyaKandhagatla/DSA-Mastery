def even_sum(a, i):
    if i == len(a):
        return 0
    
    return even_sum(a, i+1) + (a[i] if a[i] % 2 == 0 else 0)

# a = [2, 5, 6, 7, 3]
# a = [1,3,5,7]
a = [2, 4, 6, 8]
print(even_sum(a, 0))