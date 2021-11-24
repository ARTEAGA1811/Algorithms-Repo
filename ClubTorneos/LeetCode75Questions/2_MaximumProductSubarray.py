#https://leetcode.com/problems/maximum-product-subarray/
from functools import reduce
def myFunction(nums:list):
    def multiply(myList):
        if len(myList) == 1:
            return myList[0]
        elif len(myList) == 0:
            return 0
        else:
            product = 1
            for i in range(len(myList)):
                product = product * myList[i]
            return product
    
    maxProduct = multiply(nums)
    indZeros = [x for x in range(len(nums)) if nums[x] == 0]
    listWithoutZeros = [nums.copy()]
    if len(indZeros)>0:
        listWithoutZeros = [nums[:indZeros[0]], nums[indZeros[-1]+1:]]

    
    for i in range(1, len(indZeros)):
        if indZeros[i] - indZeros[i-1] > 1:
            listWithoutZeros.append(nums[indZeros[i-1]+1:indZeros[i]])
    

    for i in range(len(listWithoutZeros)):
        countNegatives = len(list(filter(lambda x:(x < 0), listWithoutZeros[i])))
        if countNegatives%2 == 0:
            maxProduct = max(maxProduct, multiply(listWithoutZeros[i]))
        else:
            if len(listWithoutZeros[i]) == 1:
                maxProduct = max(maxProduct, listWithoutZeros[i][0])
                continue
            for j in range(len(listWithoutZeros[i])):
                if listWithoutZeros[i][j] < 0:
                    maxProduct = max(maxProduct, multiply(listWithoutZeros[i][:j]), multiply(listWithoutZeros[i][j+1:]))
    return maxProduct

def functionOptimized(nums):
    res = max(nums)
    curMin, curMax = 1,1
    for n in nums:
        if n == 0:
            curMin, curMax = 1,1
            continue
        tmp = curMax * n
        curMax = max(n*curMax, n * curMin, n)
        curMin = min(tmp, n * curMin, n)
        res = max(res, curMax)
    return res




class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        [2,3,-2,4],
        [-2,0,-1],
        [0,0,0,2,-1],
        [-2]
    ]

    salidas = [
        6,
        0,
        2,
        -2

    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = functionOptimized(casosPrueba[i]) #parameters
            assert solution == salidas[i]
            print(
                bcolors.OK+"\nCORRECT ANSWER:"+bcolors.RESET+f"\ntest {casosPrueba[i]}, result {solution}")
        except Exception as error:
            print(
                bcolors.FAIL+"\nERROR: "+bcolors.RESET+f"\ntest {casosPrueba[i]}, "+bcolors.WARNING+"\nExpected "+bcolors.RESET+f"{salidas[i]}, "+bcolors.WARNING+"\nCalculated "+bcolors.RESET+f"{solution}", error)

testCode()