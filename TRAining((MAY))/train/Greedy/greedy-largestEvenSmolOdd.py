nums = list(map(int, input().split()))
even, odd = float('-inf'), float('inf')

for num in nums:
    if num % 2 == 0:
        even = max(num, even)
    else:
        odd = min(num, odd)

print(f"Even: {even}, Odd: {odd}")