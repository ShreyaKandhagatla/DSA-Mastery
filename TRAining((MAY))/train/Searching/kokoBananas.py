import math

def minEatingSpeed(piles, H):
    left, right = 1, max(piles)
    
    def canEatAll(K):
        return sum(math.ceil(p / K) for p in piles) <= H
    
    while left < right:
        mid = (left + right) // 2
        if canEatAll(mid):
            right = mid
        else:
            left = mid + 1
    return left

piles = [3,6,7,11]
H = 8
print(minEatingSpeed(piles, H))