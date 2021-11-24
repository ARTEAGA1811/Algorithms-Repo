#https://leetcode.com/problems/summary-ranges/

def solucionar(nums:list):
    if len(nums) == 0:
        return []
    aux = nums[0]
    valIni = nums[0]
    mydic = {nums[0]:0}
    for i in range(1,len(nums)):
        if nums[i] == aux + 1:
            aux +=1
            mydic[valIni]+=1
        else:
            valIni = nums[i]
            aux = nums[i]
            mydic[valIni] = 0
    myList = []
    for i in mydic:
        if mydic[i] == 0:
            myList.append(str(i))
        else:
            myList.append(str(i)+"->"+str(i+mydic[i]))
    return myList

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        [0,1,2,4,5,7],
        [0,2,3,4,6,8,9],
        [],
        [-1],
        [0]
    ]

    salidas = [
        ["0->2","4->5","7"],
        ["0","2->4","6","8->9"],
        [],
        ["-1"],
        ["0"]

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