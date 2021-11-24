def getNumberArr(arr:list):
    newArr = []
    for i in arr:
        aux = []
        for k in i:
            if k == ' ':
                aux.append(0)
            elif(k =='X'):
                aux.append(1)
            else:
                aux.append(2)
        newArr.append(aux)
    
    return newArr
           
def thereAre3Completed(matriz, who):
    caseOne = matriz[0][0] == who and matriz[0][1] == who and matriz[0][2] == who
    caseTwo = matriz[1][0] == who and matriz[1][1] == who and matriz[1][2] == who
    caseThree = matriz[2][0] == who and matriz[2][1] == who and matriz[2][2] == who
    caseFour = matriz[0][0] == who and matriz[1][0] == who and matriz[2][0] == who
    caseFive = matriz[0][1] == who and matriz[1][1] == who and matriz[2][1] == who
    caseSix = matriz[0][2] == who and matriz[1][2] == who and matriz[2][2] == who
    caseSeven = matriz[0][0] == who and matriz[1][1] == who and matriz[2][2] == who
    caseEight = matriz[2][0] == who and matriz[1][1] == who and matriz[0][2] == who
    if(caseOne or caseTwo or caseThree or caseFour or caseFive or caseSix or caseSeven or caseEight):
        return True
    return False

def isFullMatriz(matriz):
    for i in range(len(matriz)):
        for k in range(len(matriz[i])):
            if matriz[i][k] == 1 or matriz[i][k] == 2:
                return False
    return True

def solucionar(a:list):
    arr = getNumberArr(a)

    def myFunct(farr:list, turnOf: int, nextTurn: int):
        #verifico que gano.
        if thereAre3Completed(farr,3):
            #verifico que ya este vacia.
            if isFullMatriz(farr):
                return True
            else:
                return False
        
        if thereAre3Completed(farr,4):
            #verifico que ya este vacia.
            if isFullMatriz(farr):
                return True
            else:
                return False
        #verifico que ya esten llenos.
        if isFullMatriz(farr):
            return True
        
        #recursive cases
        finalResult = False
        #aqui analizo el siguiente turno. todas las posibles.
        for i in range(len(farr)): #iterate rows
            for k in range(len(farr[i])): #iterate columns
                if farr[i][k] == turnOf:
                    #aqui entra al siguiente analisis.
                    #lo convierto.
                    if turnOf == 1:
                        farr[i][k] = 3
                    else:
                        farr[i][k] = 4
                    
                    #recursiva
                    result = myFunct(farr, nextTurn, turnOf)
                    finalResult = finalResult or result
                    
                    #regreso la posision.
                    if turnOf == 1:
                        farr[i][k] = 1
                    else:
                        farr[i][k] = 2
                
        return finalResult

    myAux = False
    for a in range(len(arr)):
        for b in range(len(arr[a])):
            if arr[a][b] == 1:
                arr[a][b] = 3
                myAux = myAux or myFunct(arr,2,1)
                arr[a][b] = 1
    
    return myAux
        







def testCode():
    casosPrueba = [
        ["O  ","   ","   "],
        ["XOX"," X ","   "],
        ["XXX","   ","OOO"],
        ["XOX","O O","XOX"]


        
    ]

    salidas = [
        False, 
        False,
        False,
        True
    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(casosPrueba[i])
            assert solution == salidas[i]
            print(
                f"respuesta correcta: test {casosPrueba[i]}, result {solution}")
        except Exception as error:
            print(
                f"Error, test {casosPrueba[i]}, expected {salidas[i]}, calculated {solution}", error)


testCode()