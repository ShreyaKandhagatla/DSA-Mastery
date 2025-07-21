def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

arr=[[4,13,12],[8,10,5],[7,9,20],[14,8,3]]
prime_map = {}  

for idx, row in enumerate(arr):
    for num in row:
        if is_prime(num):
            prime_map[idx] = num
            break

n = len(arr)
for i in range(n):
    swap = False
    for j in range(0, n-i-1):
        if prime_map[j] > prime_map[j+1]:
            swap = True
            arr[j], arr[j+1] = arr[j+1], arr[j]
            prime_map[j], prime_map[j+1] = prime_map[j+1], prime_map[j]
    if not swap:
        break

for row in arr:
    print(row)

