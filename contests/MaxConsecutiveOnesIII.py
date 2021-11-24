import itertools
def solucionar(nums:list, k:int) -> int:
    indFound = []
    
    def getMaxConsecutiveOnes():
        newCont = 0
        aux = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                aux+=1
                newCont = max(aux, newCont)
            else:
                aux = 0
        return newCont

    maxConsecutive = getMaxConsecutiveOnes()     
    for i in range(len(nums)):
        if nums[i] == 0:
            indFound.append(i)
    
    allCombinations = []
    for bucle in range(1,k+1):
        allCombinations.extend(list(itertools.combinations(indFound,bucle)))
    for i in range(len(allCombinations)):
        for j in range(len(allCombinations[i])):
            nums[allCombinations[i][j]] = 1
        maxConsecutive = max(maxConsecutive, getMaxConsecutiveOnes())
        for j in range(len(allCombinations[i])):
            nums[allCombinations[i][j]] = 0
    return maxConsecutive


class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        [
            [1,1,1,0,0,0,1,1,1,1,0],2
        ],
        [
            [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3
        ],
        [
            [0,0,0,1],4
        ],
        [
            [0,0,1,1,1,0,0],0
        ]
        
        
    ]

    salidas = [
        6,
        10,
        4,
        3

    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(casosPrueba[i][0],casosPrueba[i][1]) #parameters
            assert solution == salidas[i]
            print(
                bcolors.OK+"\nCORRECT ANSWER:"+bcolors.RESET+f"\ntest {casosPrueba[i]}, result {solution}")
        except Exception as error:
            print(
                bcolors.FAIL+"\nERROR: "+bcolors.RESET+f"\ntest {casosPrueba[i]}, "+bcolors.WARNING+"\nExpected "+bcolors.RESET+f"{salidas[i]}, "+bcolors.WARNING+"\nCalculated "+bcolors.RESET+f"{solution}", error)

testCode()