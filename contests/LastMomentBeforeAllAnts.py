def solucionar(n:int, left:list, right:list):
    woodMin = 0
    woodMax = n
    t = 0
    myArr =[0 for i in range(n+1)]
    #fill myArr with 1s by using left and right
    for i in left:
        myArr[i] = 1
    for i in right:
        myArr[i] = 2
    while myArr.count(0)<len(myArr):
        for i in range(len(myArr)):
            if myArr[i] == 1:
                



                



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