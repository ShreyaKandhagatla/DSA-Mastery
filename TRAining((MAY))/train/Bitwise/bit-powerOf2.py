def isPowerOf2(n):
    if n == 0:
        return 0
    return n & (n - 1) == 0

n = int(input())
if isPowerOf2(n):
    print(n,"is a power of 2")
else:
    print(n,"is not a power of 2")

# 8 => 1000
# 7 => 0111

# 16 => 10000
# 15 => 01111
