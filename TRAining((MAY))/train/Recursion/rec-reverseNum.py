def reverseNumber(rev, num):
    if num == 0:
        return rev
    return reverseNumber(rev*10 + num%10, num//10)