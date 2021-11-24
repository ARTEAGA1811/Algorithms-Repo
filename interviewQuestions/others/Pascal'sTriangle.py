#Ejercicio pascal I
# def solucionar(numRows:int):
#     if numRows == 1:
#         return [[1]]
#     pascal = [[1],[1,1]]
#     for i in range(2,numRows):
#         aux = [1]
#         for k in range(0,len(pascal[i-1])-1): #recorro el pascal [1,1] solo el primer 1
#             aux.append(pascal[i-1][k]+pascal[i-1][k+1])
#         aux.append(1)
#         #agrego a pascal
#         pascal.append(aux)
#     return pascal

#Ejercicio Pascal II
def solucionar(numRows:int):
    if numRows == 0:
        return [1]
    lastpascal = [1,1]
    for i in range(1,numRows):
        aux = [1]
        for k in range(0,len(lastpascal)-1): #recorro el pascal [1,1] solo el primer 1
            aux.append(lastpascal[k]+lastpascal[k+1])
        aux.append(1)
        #agrego a pascal
        lastpascal = aux
    return lastpascal 

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        3,5,1,
        8,

    ]

    salidas = [
        [1,3,3,1],
        [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]],
        [[1]],
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1]]


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