def squareRoot(n):
    l, r = 0, n

    while l <= r:
        mid = (l + r)//2

        if mid * mid == n:
            return mid
        elif mid * mid < n:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    
    return ans

n = int(input())
print(squareRoot(n))