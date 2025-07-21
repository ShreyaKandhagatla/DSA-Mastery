'''Finding number of ways
def frog_jump(n):
    if n == 0:
        return 1  # 1 way to stay at the 0th step
    if n == 1:
        return 1  # only one way: jump 1 step
    return frog_jump(n - 1) + frog_jump(n - 2)

n = int(input("Enter the number of steps: "))
print("Number of ways the frog can reach step", n, "is:", frog_jump(n))
'''

'''
#frog jump recursion
def frog(n):
    if n<=1:
        return dp[n]

    dp[n] = min(frog(n-1) + abs(a[n] - a[n-1]), frog(n-2) + abs(a[n] - a[n-2]))
    return dp[n]

a = [10, 20, 30, 10, 30, 20, 10]
n = len(a)
dp = [0] * n
dp[1] = abs(a[1] - a[0])
frog(n - 1)
print(dp)

'''

'''
#Tabulation
# Frog Jump - Tabulation (DP Bottom-Up)
a = [10, 20, 30, 10, 30, 20, 10]
n = len(a)
dp = [0] * n

# Base case
dp[0] = 0
dp[1] = abs(a[1] - a[0])

for i in range(2, n):
    jump_one = dp[i - 1] + abs(a[i] - a[i - 1])
    jump_two = dp[i - 2] + abs(a[i] - a[i - 2])
    dp[i] = min(jump_one, jump_two)

print("DP Table:", dp)
print("Minimum cost to reach step", n - 1, ":", dp[n - 1])
'''
'''
a=[10,20,30,10,30,20,10]
dp=[0]*len(a)
dp[1]=abs(a[0]-a[1])
for i in range(2,len(a)):
    dp[i]=min((dp[i-1]+abs(a[i]-a[i-1]),(dp[i-2]+abs(a[i]-a[i-2]))))
print(dp[len(a)-1])

'''
'''
MAking it More SPACE EFFICIENT By using variable rather than tables when comapred to above code

a = [10, 20, 30, 10, 30, 20, 10]
n = len(a)

prev2 = 0
prev1 = abs(a[1] - a[0])

for i in range(2, n):
    jump_one = prev1 + abs(a[i] - a[i - 1])
    jump_two = prev2 + abs(a[i] - a[i - 2])
    curr = min(jump_one, jump_two)
    
    # Update previous steps
    prev2 = prev1
    prev1 = curr

print("Minimum cost to reach last step:", prev1)
'''


#KR
#FOR k JUMPS
#recursion
def frog(n):
    if n == 0:
        return 0
    if dp[n] != -1:
        return dp[n]

    min_cost = float('inf')
    for j in range(1, k + 1):
        if n - j >= 0:
            cost = frog(n - j) + abs(a[n] - a[n - j])
            min_cost = min(min_cost, cost)

    dp[n] = min_cost
    return dp[n]

a = [10, 20, 30, 10, 30, 20, 10]
k = 3
n = len(a)
dp = [-1] * n
print(frog(n - 1))
#frog jump k


#recursion
def frog(n):
    if dp[n] != -1:
        return dp[n]
    if n == 0:
        return 0
    elif n == 1:
        return abs(a[1] - a[0])

    dp[n] = min(frog(n - 1) + abs(a[n] - a[n - 1]),
                frog(n - 2) + abs(a[n] - a[n - 2]))
    return dp[n]

#tabulation
a = [10, 20, 30, 10, 30, 20, 10]
n = len(a)
dp = [-1] * n
print(frog(n - 1))
print(dp)

a = [10, 20, 30, 10, 30, 20, 10]
n = len(a)
dp = [0] * n

for i in range(1, n):
    jump_one = dp[i - 1] + abs(a[i] - a[i - 1])
    jump_two = dp[i - 2] + abs(a[i] - a[i - 2]) if i > 1 else float('inf')
    dp[i] = min(jump_one, jump_two)

print(dp[-1])

#space optimized
a = [10, 20, 30, 10, 30, 20, 10]
n = len(a)

prev2 = 0
prev1 = abs(a[1] - a[0])

for i in range(2, n):
    jump_one = prev1 + abs(a[i] - a[i - 1])
    jump_two = prev2 + abs(a[i] - a[i - 2])
    curr = min(jump_one, jump_two)
    

    prev2 = prev1
    prev1 = curr

print(prev1)