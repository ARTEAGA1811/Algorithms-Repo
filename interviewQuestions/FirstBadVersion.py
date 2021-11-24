#https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/774/
import random
def getRAndomArray(n:int):
    arr = []
    firstBad = random.randint(0,n-1)
    #print("first: ", firstBad)
    for i in range(firstBad):
        arr.append('V')
    for k in range(firstBad,n):
        arr.append('X')
    return arr 

def isBadVersion(arr:list,num:int):
    return arr[num-1] == 'X'
    

def solucionar(n: int):
    #arr = getRAndomArray(n)
    arr = ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'X']
    print(arr)
    if n == 1:
        return 1
    
    restantes = n
    leftPart = 1
    rightPart = n 
    while leftPart!=rightPart:
        center = int((rightPart+leftPart)/2)
        if isBadVersion(arr,center):
            rightPart = center
        else:
            leftPart = center+1
    if isBadVersion(arr,leftPart):
        return leftPart
    return leftPart+1






print(solucionar(10))


class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
    ]

    salidas = [

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

testCode()