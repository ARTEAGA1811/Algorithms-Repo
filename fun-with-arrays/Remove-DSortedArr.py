def solucionar(nums:list):
    nums2 = list(set(nums))
    nums2.sort()
    for i in range(len(nums2)):
        nums[i] = nums2[i]
    print(nums)
    print(nums2)
    return len(nums2)    
    

solucionar([-1,0,0,0,0,3,3])