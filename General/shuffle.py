def solucionar(arr:list, n:int):
    myDiv = int(len(arr)/n)
    newList = []
    #bucle
    for i in range(n):
        aux = 0 + i
        for k in range(myDiv):
            newList.append(arr[aux])
            aux+= n
    
    return newList






def testCode():
    casosPrueba = [
        [
            [2,5,1,3,4,7],
            3
        ],
        [
            [1,2,3,4,4,3,2,1],
            4
        ]

        
    ]

    salidas = [
        [2,3,5,4,1,7],
        [1,4,2,3,3,2,4,1]
    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(casosPrueba[i][0],casosPrueba[i][1])
            assert solution == salidas[i]
            print(
                f"respuesta correcta: test {casosPrueba[i]}, result {solution}")
        except Exception as error:
            print(
                f"Error, test {casosPrueba[i]}, expected {salidas[i]}, calculated {solution}", error)


testCode()