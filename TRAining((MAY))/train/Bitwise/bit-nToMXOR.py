def findXORTillN(n):
    rem = n % 4
    if rem == 0:
        return n
    if rem == 1:
        return 1
    if rem == 2:
        return n+1
    return 0

n = int(input())
m = int(input())
print(findXORTillN(n-1) ^ findXORTillN(m))