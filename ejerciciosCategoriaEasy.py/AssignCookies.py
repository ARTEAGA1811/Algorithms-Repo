def solucionar(g: list,s:list):
    if len(g) == 0 or len(s) == 0:
        return 0
    g.sort()
    s.sort()
    g.reverse()
    s.reverse()
    suma = 0
    lastInd = 0
    for i in range(len(g)):
        for j in range(lastInd,len(s)):
            if g[i] <= s[j]:
                suma += 1
                lastInd = j+1
                break

    return suma

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        [
            [1,2,3],[1,1]
        ],
        [
            [1,2],[1,2,3]
        ],
        [
            [10,9,8,7],[5,6,7,8]
        ]
    ]

    salidas = [
        1,
        2,
        2

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