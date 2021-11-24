#1,2,3,4,3,4,5,6,5,6,7,8,7,...
def solucionar(n:int):
    if n ==1:
        return 1
    if n == 2:
        return 2
    
    aux = n//4
    aux2 = 2*aux+1
    k = n%4
    if k%2 == 0:
        k = aux2+1
        return k
    return aux2

    


    

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        545421,
        87123641123172368
    ]

    salidas = [
        272711,
        43561820561586186
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