# 350. Intersection of Two Arrays II

def intersect(nums1, nums2):
    # time comp --> O(N) space comp --> O(1)
    hm1 = Counter(nums1)
    arr = []
    for ele in nums2:
        if hm1[ele] > 0:
            hm1[ele] -= 1
            arr.append(ele)
    return arr


    # brute force solution time comp --> O(N) space comp --> O(N+M)
    hm1 = Counter(nums1)
    hm2 = Counter(nums2)
    arr = []
    for item in hm1:
        if item in hm2:
            n = min(hm1[item], hm2[item])
            for i in range(n):
                arr.append(item)
    
    return arr

if __name__ == '__main__':
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    res = intersect(nums1, nums2)
    print(res)