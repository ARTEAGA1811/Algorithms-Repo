#https://leetcode.com/problems/can-place-flowers/
def solucionar(flowerbed, n):
    if n == 0:
        return True
    if len(flowerbed) == 1:
        if flowerbed[0] == 0:
            return n == 1
        else:
            return False
    if flowerbed[0] == 0 and flowerbed[1] == 0:
        flowerbed[0] = 1
        n -=1
        if n == 0:
            return True
    for i in range(1,len(flowerbed)-1):
        if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
            flowerbed[i] = 1
            n -= 1
            if n == 0:
                return True
    if flowerbed[-1] == 0 and flowerbed[-2] == 0:
        flowerbed[-1] = 1
        n -= 1
        return n == 0
    return False
    
    
#thanks github copilot, you are the best

    

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        # [
        #     [1,0,0,0,1],1
        # ],
        # [
        #     [1,0,0,0,1],2
        # ],
        [
            [0,0,1,0,0],2
        ]

    ]

    salidas = [
        #True,False
        True
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