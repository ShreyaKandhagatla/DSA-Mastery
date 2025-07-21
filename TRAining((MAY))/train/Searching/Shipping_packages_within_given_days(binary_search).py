def possibleOrNot(weights, days, capacity):
    sumOfWeights = 0
    dayCnt = 0
    for weight in weights:
        sumOfWeights += weight
        if sumOfWeights > capacity:
            dayCnt += 1
            sumOfWeights = weight
    dayCnt += 1
    if dayCnt == days:
        return dayCnt
    return False

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
capacity = 15
print(possibleOrNot(weights, days, capacity))

