def sort(nums1, nums2):
    p1, p2 = 0, 0
    res = []

    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] <= nums2[p2]:
            res.append(nums1[p1])
            p1 += 1
        else:
            res.append(nums2[p2])
            p2 += 1
    
    while p1 < len(nums1):
        res.append(nums1[p1])
        p1 += 1
    
    while p2 < len(nums2):
        res.append(nums2[p2])
        p2 += 1
    
    return res

nums1 = [2,4,5,8,9]
nums2 = [3,5,6,9,11,12,13]
print(*sort(nums1, nums2))
