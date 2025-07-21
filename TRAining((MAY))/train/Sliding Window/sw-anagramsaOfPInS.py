from collections import Counter

def findAnagrams(s, p):
    p_count = Counter(p)
    s_count = Counter()
    result = []
    for i in range(len(s)):
        s_count[s[i]] += 1
        if i >= len(p):
            if s_count[s[i - len(p)]] == 1:
                del s_count[s[i - len(p)]]
            else:
                s_count[s[i - len(p)]] -= 1
        if s_count == p_count:
            result.append(i - len(p) + 1)
    return result

p = input('P: ')
s = input('S: ')
print(findAnagrams(s, p))
