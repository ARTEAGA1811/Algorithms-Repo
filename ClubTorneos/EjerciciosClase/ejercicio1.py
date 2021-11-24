def solucionar(numbers:list):
    mydic = {}
    for i in range(len(numbers)):
        if numbers[i] in mydic:
            mydic[numbers[i]] += numbers[i]
        else:
            mydic[numbers[i]] = numbers[i]
    
    
    minSuma = mydic[numbers[0]]
    for i in mydic:
        if mydic[i] < minSuma:
            minSuma = mydic[i]
    
    valids =[]
    for i in mydic:
        if mydic[i] == minSuma:
            valids.append(i)
    return max(valids)

    
    

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        [1,1,2,3,4,5,5,5,6],
        [1,-1,2,-3,4,-5,5,5,-6, 6, 6, -5, 3],
        [4,-10,6,-3,-2,-4,-9,10,0,-7,-4,-9,-4,2,-6,-7,10,1,8,10,5,1,2,-8,2,-10,0,-6,4,-2,-6,8,-3,0,9,-4,4,-5,4,-8,-1,-3,-8,8,-6,-7,8,6,0,9,2,-3,-4,4,-5,-2,0,3,0,-3,-6,-4,1,-4,-5,3,2,1,4,-8,-8,-3,-6,2,-4,9,-6,-9,0,9,9,-6,3,-4,0,-7,-5,0,6,-6,-10,4,-2,6,-3,-1,4,1,-3,-7],
        [2,-10,0,-8,4,-5,10,0,8,-9,4,-6,3,4,8,10,6,-5,2,-6,9,-10,4,-1,6,-1,7,10,-10,-3,-6,1,7,-1,9,-1,2,3,4,8,-3,-3,-5,5,-8,-1,9,8,8,0,-5,3,-6,-9,10,-8,-3,-4,-1,-8,-6,4,-10,1,7,-1,0,10,1,-1,-6,-2,-2,5,-1,-7,4,5,-5,6,-7,6,-2,-5,5,7,-4,8,0,8,-10,-7,-2,0,9,10,5,5,-8,9]
    ]

    salidas = [
        2,
        -5,
        -6,
        -10

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