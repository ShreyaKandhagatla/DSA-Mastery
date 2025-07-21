nums = list(map(int, input().split()))

xor = 0
for num in nums:
    xor ^= num
print(xor)

# hm = {}
# for num in nums:
#     if num in hm:
#         hm[num] += 1
#     else:
#         hm[num] = 1

# for k, v in hm.items():
#     if v == 1:
#         print(k)