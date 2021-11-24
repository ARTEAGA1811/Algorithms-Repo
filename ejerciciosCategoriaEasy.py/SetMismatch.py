#https://leetcode.com/problems/set-mismatch/
def solucionar(nums:list):
    mySett =set()
    repeated = -1
    for i in range(len(nums)):
        if nums[i] not in mySett:
            mySett.add(nums[i])
        else:
            repeated = nums[i]
            break
    allNums = {x for x in range(1,len(nums)+1)}
    auxNUms = set(nums)
    allNums = allNums - auxNUms
    other = 0
    for i in allNums:
        other = i
        break
    return [repeated,other]



class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        [1,2,2,4],
        [1,1],
        [2,2],
        [3,2,2],
        [3,2,3,4,6,5],
        [8,7,3,5,3,6,1,4]
    ]

    salidas = [
        [2,3],
        [1,2],
        [2,1],
        [2,1],
        [3,1],
        [3,2]

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