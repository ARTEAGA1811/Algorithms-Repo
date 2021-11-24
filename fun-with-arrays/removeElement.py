def solucionar(nums: list, val:int):
    nums = [x for x in nums if x != val]
    print(nums)
    return len(nums)


print(solucionar([3,2,2,3],3))