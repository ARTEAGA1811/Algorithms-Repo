#https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/745/
import math
def solucionar(n:int):
    if n<=0:
        return False

    x = math.log(n,3)
    if x-int(x) == 0:
        return True

    if x-int(x)>=0.9999999999 or x-int(x)<=0.00000001:
        x = round(x)
        if 3**x == n:
            return True
        return False
    else:
        return False


class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        # 27,
        # 0,
        # 9,
        # 45,
        # 59049,
        # 243,
        # 19682,
        4,
        2
    ]

    salidas = [
        # True,
        # False,
        # True,
        # False,
        # True,
        # True,
        # False,
        False,
        False
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