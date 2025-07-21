a = []
d = {}
k = 3

for i in a:
    if (i not in d):
        d[i] = 1
    else:
        d[i] += 1

print(d)
m = max(d.values())
b = [0 for i in range(m + 1)]
for i in d:
    b[d[i]].append(i)

count = 0
kth_largest_freq = None
kth_largest_numbers = []

for freq in range(m, 0, -1):
    count += len(b[freq])
    if count >= k:
        kth_largest_freq = freq
        kth_largest_numbers = b[freq]
        break

print(f"The {k}-th largest frequency is: {kth_largest_freq}")
print(f"The numbers with the {k}-th largest frequency are: {kth_largest_numbers}")