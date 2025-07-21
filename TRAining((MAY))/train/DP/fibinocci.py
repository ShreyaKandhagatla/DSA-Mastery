def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib(n - 1) + fib(n - 2)
    return dp[n]

n = int(input("Enter n: "))
dp = [-1] * (n + 1)
'''creates a memorization table which consistes of -1 with size of n+1(the table is n+1 size with values embedded as -1)'''
print(fib(n))



'''
#Fibinocci Tabulation
#8th element = 21 (0 index)
dp = [1,1]
n = 8
for i in range(2, n):
    dp.append(dp[i-1]+dp[i-2])
print(dp[n-1])

'''



'''
#Printing fibinocci values till a given range
def print_fibonacci_upto_n(n):
    fib = [0, 1]
    if n == 0:
        print(0)
        return
    elif n == 1:
        print("0 1")
        return
    print("0 1", end=' ')
    for i in range(2, n+1):
        next_fib = fib[-1] + fib[-2]
        print(next_fib, end=' ')
        fib.append(next_fib)

# Example usage:
n = int(input("Enter the value of n: "))
print_fibonacci_upto_n(n)
'''
