def getSimpleList(nums:list):
    simpleList = []
    flag = False
    if nums[0] >0:
        flag = True
    auxOne = 0
    for i in range(len(nums)-1):
        if flag:
            if nums[i] >=0:
                auxOne+=nums[i]
            else:
                simpleList.append(auxOne)
                auxOne = nums[i]
                flag = False
        else:
            if nums[i]<0:
                auxOne+=nums[i]
            else:
                simpleList.append(auxOne)
                auxOne = nums[i]
                flag = True
    if flag == True:
        if nums[-1]>=0:
            simpleList.append(auxOne+nums[-1])
        else:
            simpleList.append(auxOne)
            simpleList.append(nums[-1])
    else:
        if nums[-1]<0:
            simpleList.append(auxOne+nums[-1])
        else:
            simpleList.append(auxOne)
            simpleList.append(nums[-1])
    return simpleList

def solucionar(nums:list):
    simpli = getSimpleList(nums)
    #print(simpli)

    #algorith
    sumaAux = 0
    largSum = max(nums)
    for i in range(len(simpli)):
        if sumaAux+simpli[i]<0:
            sumaAux = 0
            continue
        else:
            if simpli[i]<0:
                if i == len(simpli)-1:
                    break
                else:
                    if simpli[i+1]>simpli[i]:
                        sumaAux+=simpli[i]
                    else:
                        sumaAux = 0
            else:
                sumaAux+=simpli[i]
                if sumaAux>largSum:
                    largSum = sumaAux

    return largSum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return solucionar(nums)