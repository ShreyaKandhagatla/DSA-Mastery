def primeOrNot(n, i):
    if i == (n//2) + 1:
        return True
    if n % i == 0:
        return False
    return primeOrNot(n, i+1)

def prime(nums):
    if 0 == len(nums):
        return 0
    return (1 if primeOrNot(nums[0], 2) else 0) + prime(nums[1:])

nums = [13, 17, 21, 23, 22, 7, 29]
print(prime(nums))