def solucionar(nums1:list, m:int, nums2:list, n:int):
    for i in range(len(nums1)-1,m-1,-1):
        nums1.pop()
    nums1.extend(nums2)
    nums1.sort()
    return nums1


print(solucionar([1,2,3,0,0,0],3,[2,5,6],3))



