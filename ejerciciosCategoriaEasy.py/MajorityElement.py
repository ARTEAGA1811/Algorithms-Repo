#https://leetcode.com/problems/majority-element/submissions/
def getMajorityElement(nums:list):
    logs = {}
    for i in nums:
        if i in logs:
            logs[i] += 1
        else:
            logs[i] = 1
    #return the key who has the majority
    for key, value in logs.items():
        if value > len(nums)//2:
            return key
    return -1



