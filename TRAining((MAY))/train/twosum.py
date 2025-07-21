def twosum(n,tar):
    i=0
    j=len(n)-1
    sum=0
    while i<j:
        sum=n[i]+n[j]
        if sum==tar:
            return f"{n[i]},{n[j]}"
        if sum<tar:
            i+=1
        else:
            j-=1
    return "False"
n=list(map(int,input().split()))
tar=int(input())
print(twosum(n,tar))

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [i, pair_idx[target - num]]
            pair_idx[num] = i
'''









'''