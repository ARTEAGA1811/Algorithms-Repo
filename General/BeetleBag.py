#https://csacademy.com/ieeextreme-practice/task/ed8629419f140a5a2c923b049aba1224/statement/
import numpy as np

def solucionar(t:int, c:int,n:int,li:list):
    #t = int(input())
    todotodo = []
    for bucleOne in range(t):
        #a = input().split()

        total_wt = c
        wtList = [0]
        powerList = [0]
        # for bucleTwo in range(n):
        #     aux = input().split()
        #     wtList.append(int(aux[0]))
        #     powerList.append(int(aux[1]))

        for bucleTwo in li:
            wtList.append(bucleTwo[0])
            powerList.append(bucleTwo[1])
        #start with the algorythm
        #se crea una matriz con las dimensiones llenada en cero
        arr = np.zeros((len(wtList),total_wt+1))
        for i in range(1,len(arr)):
            for j in range(1,len(arr[0])):
                if j<wtList[i]:
                    arr[i][j] = arr[i-1][j]
                else:
                    arr[i][j] = max(powerList[i]+arr[i-1][j-wtList[i]],arr[i-1][j])
        
        todotodo.append(arr[-1][-1])
    
    return todotodo









def testCode():
    casosPrueba = [
      [
        1,7,4,[[1,1],[3,4],[4,5],[5,7]]
      ],
      [
        1,6,2,[[1,17],[6,15]]
      ],
      [
         1,5,5,[[1,1],[2,2],[3,3],[4,4],[5,5]] 
      ]
    ]

    salidas = [
        [9],[17],[5]
    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(casosPrueba[i][0],casosPrueba[i][1],casosPrueba[i][2],casosPrueba[i][3])
            assert solution == salidas[i]
            print(
                f"respuesta correcta: test {casosPrueba[i]}, result {solution}")
        except Exception as error:
            print(
                f"Error, test {casosPrueba[i]}, expected {salidas[i]}, calculated {solution}", error)

testCode()