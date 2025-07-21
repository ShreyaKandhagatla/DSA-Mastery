def reach1(n, a, b, c, path=[]):
    # print(c)
    if n < 1:
        return (float('inf'), [])
        # return False
    if n == 1:
        return (c, path)
        # return True
    ans1 = reach1(n-a, a, b, c+1, path + [n])
    ans2 = reach1(n-b, a, b, c+1, path + [n])
    return ans1 if ans1[0] <= ans2[0] else ans2
    # return reach1(n-a, a, b, c+1) or reach1(n-b, a, b, c+1)


n = int(input('n: '))
a = int(input('a: '))
b = int(input('b: '))

print(f'{reach1(n, a, b, 0, [])}')