#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/
def getTwoSumOptimized(nums:list, target:int)->list:
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    """
    dic = {}
    for i, num in enumerate(nums,1):
        if num in dic:
            return [dic[num], i]
        else:
            dic[target - num] = i
    return []

#create a test case for the function
nums = [2,7,11,15]
target = 9
print(getTwoSumOptimized(nums, target))