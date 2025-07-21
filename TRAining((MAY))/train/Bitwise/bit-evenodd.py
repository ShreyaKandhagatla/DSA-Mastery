n = int(input("Enter a number: "))

# n^1==n-1 => odd
# n&1==1 => odd
# n^1==n+1 => even
# if n is odd, n^n-1 is always 1
if n ^ 1 == n + 1:
    print("The number is even")
else:
    print("The number is odd")