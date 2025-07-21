n = list(map(int, input().split()))
s = set()
new = []

for i in n:
    if i not in s:
        s.add(i)
        new.append(i)

print(new)
#time O(n)
#space O(n)