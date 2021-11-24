#https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/722/

def solucionar(nums:list):
    setNums = set(nums)
    aux = {x for x in range(len(nums)+1)}
    c = 0
    for i in aux-setNums:
        c = i
    return c

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        [3,0,1],
        [0,1],
        [9,6,4,2,3,5,7,0,1],
        [0]

    ]

    salidas = [
        2,2,8,1
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