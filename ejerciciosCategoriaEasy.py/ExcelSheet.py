import math
def solucionar(columnTitle:str):
    #generate a diccionary with all the 26 capital letters  of the alphabet and their respective number
    alphabet = {}
    for i in range(26):
        alphabet[chr(i+65)] = i+1
    exp = 0
    total = 0
    for i in range(len(columnTitle)-1,-1,-1):
        total+=alphabet[columnTitle[i]]*(26**exp)
        exp+=1
    return total



    

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        "A",
        "AB",
        "ZY",
        "FXSHRXW"
    ]

    salidas = [
        1,
        28,
        701,
        2147483647
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