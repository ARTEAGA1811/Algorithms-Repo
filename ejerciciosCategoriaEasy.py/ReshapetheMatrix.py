#https://leetcode.com/problems/reshape-the-matrix/
def solucionar(mat:list,r:int,c:int):
    if len(mat)*len(mat[0]) != r*c:
        return mat
    auxList = []
    for i in range(len(mat)):
        auxList.extend(mat[i])
    cont = 0
    newMatriz = []
    for i in range(r):
        newMatriz.append([])
        for j in range(c):
            newMatriz[i].append(auxList[cont])
            cont += 1
    return newMatriz
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        [
            [[1,2],[3,4]],1,4
        ],
        [
            [[1,2],[3,4]],2,4
        ]
    ]

    salidas = [
        [[1,2,3,4]],
        [[1,2],[3,4]]
    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(casosPrueba[i][0],casosPrueba[i][1],casosPrueba[i][2]) #parameters
            assert solution == salidas[i]
            print(
                bcolors.OK+"\nCORRECT ANSWER:"+bcolors.RESET+f"\ntest {casosPrueba[i]}, result {solution}")
        except Exception as error:
            print(
                bcolors.FAIL+"\nERROR: "+bcolors.RESET+f"\ntest {casosPrueba[i]}, "+bcolors.WARNING+"\nExpected "+bcolors.RESET+f"{salidas[i]}, "+bcolors.WARNING+"\nCalculated "+bcolors.RESET+f"{solution}", error)

testCode()