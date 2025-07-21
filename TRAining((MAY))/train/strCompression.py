s = input()
prev, freq = s[0], 0
res = ''

for c in s:
    if c == prev:
        freq += 1
    else:
        res += (prev + str(freq))
        prev, freq = c, 1
res += (prev + str(freq))
print(res)