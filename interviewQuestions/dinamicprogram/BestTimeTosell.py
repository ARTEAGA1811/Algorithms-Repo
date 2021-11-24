#https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/572/
def solucionar(prices:list):
    maxEarn = 0
    selected = prices[0]
    for i in range(len(prices)-1):
        if prices[i]>selected:
            continue
        selected = prices[i]
        if prices[i]>=prices[i+1]:
            continue
        else:
            for k in range(i+1,len(prices)):
                if prices[i]<prices[k]:
                    if prices[k]-prices[i] > maxEarn:
                        maxEarn = prices[k]-prices[i]
    return maxEarn



    

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        [7,1,5,3,6,4],
        [7,6,4,3,1],
        [2,2,5],
        [2,11,1,4,7]
    ]

    salidas = [
        5,0,
        3,
        9,

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