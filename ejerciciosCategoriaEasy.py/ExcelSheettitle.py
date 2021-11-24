#https://leetcode.com/problems/excel-sheet-column-title/submissions/
def solucionar(columnNumber:int):
    #generate a dictionary with all the 26 capital letters and their respective number
    alphabet = {}
    for i in range(26):
        alphabet[i+1] = chr(i+65)

    numLetters = 1
    exp = 1
    ant = 0
    while True:
        if columnNumber <= ant+(26**exp):
            break
        ant = ant+(26**exp)
        exp += 1
        numLetters += 1
    
    aux = columnNumber%26
    if aux == 0:
        aux = 26
    myLetters = alphabet[aux]

    for i in range(numLetters-1):
        columnNumber = (columnNumber-aux)/26
        aux = columnNumber%26
        if aux == 0:
            aux = 26
        myLetters = alphabet[aux] + myLetters
    
    return myLetters
  



class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        1,
        28,
        701,
        2147483647
    ]

    salidas = [
        "A",
        "AB",
        "ZY",
        "FXSHRXW"

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