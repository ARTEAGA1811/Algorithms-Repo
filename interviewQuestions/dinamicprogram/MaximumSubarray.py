#https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/566/

# def solucionar(nums:list):
#     if len(nums) == 1:
#         return nums[0]
#     largSum = nums[0]
#     aux = nums[0]
#     for i in range(1,len(nums)):
#         aux += nums[i] 
#         if aux > largSum:
#             largSum = aux
    
#     aux = largSum
#     for k in range(len(nums)):
#         aux +=nums[k]*-1
#         if aux>largSum:
#             largSum = aux
#     return largSum
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
    print(simpli)

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

def soluuu(nums:list):
    largSuma = max(nums)
    for i in range(1,len(nums)+1):
        for k in range(0,len(nums)-i+1):
            sumaAux = 0
            for j in range(k,i+k):
                sumaAux+=nums[j]
            if sumaAux>largSuma:
                largSuma = sumaAux
    print(largSuma)
    return largSuma





class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        [-2,1,-3,4,-1,2,1,-5,4],
        [1],
        [5,4,-1,7,8],
        [-2,-1]
    ]

    salidas = [
        6,1,23,
        -1

    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(casosPrueba[i]) #parameters
            assert solution == salidas[i]
            print(
                bcolors.OK+"\nCORRECT ANSWER:"+bcolors.RESET+f"\ntest {casosPrueba[i]}, result {solution}")
        except Exception as error:
            print(
                bcolors.FAIL+"\nERROR: "+bcolors.RESET+f"\ntest {casosPrueba[i]}, "+bcolors.WARNING+"\nExpected "+bcolors.RESET+f"{salidas[i]}, "+bcolors.WARNING+"\nCalculated "+bcolors.RESET+f"{solution}", error)

#testCode()


casosPrueba = [
    [-2,1,-3,4,-1,2,1,-5,4],
    [1],
    [5,4,-1,7,8],
    [-2,-1]
]

for u in casosPrueba:
    soluuu(u)
