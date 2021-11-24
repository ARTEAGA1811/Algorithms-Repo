def solucionar(candidates:list, target:int):
    cont = []
    def getGG(indMycand:int, mysum:int, auxStr:str):
        for k in range(indMycand,len(candidates)):
            if mysum+candidates[k]<target:
                getGG(k,mysum+candidates[k],auxStr+str(candidates[k])+',')
            elif(mysum+candidates[k] == target):
                cont.append(auxStr+str(candidates[k]))


            
    for i in range(len(candidates)):
        if candidates[i]<target:
            getGG(i,candidates[i],str(candidates[i])+',')
        elif(candidates[i] == target):
            cont.append(str(candidates[i]))

    finalList = []
    for bucle in range(len(cont)):
        arrAux = [int(xd) for xd in cont[bucle].split(',')]
        finalList.append(arrAux)

    return finalList    


class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        [[2,3,6,7],7],
        [[2,3,5],8],
        [[2],1],
        [[1],1],
        [[1],2]
    ]

    salidas = [
        [[2,2,3],[7]],
        [[2,2,2,2],[2,3,3],[3,5]],
        [],
        [[1]],
        [[1,1]]
    

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