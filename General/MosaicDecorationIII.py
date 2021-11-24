#https://csacademy.com/ieeextreme-practice/task/mosaic3/
def moveColumn(arr:list, r,ce):
    for i in range(r):
        for j in range(ce-1):
            aux = arr[i][j+1]
            arr[i][j+1] = arr[i][j]
            arr[i][j] = aux

def moveRow(arr:list,r,ce):
    for i in range(r-1):
        aux = arr[i+1]
        arr[i+1] = arr[i]
        arr[i] = aux

def solucionar(r,ce,n,m,arr: list):
    a = int(m/ce)
    c = m%ce
    b = int(n/r)
    d = n%r

    def getCost(Myarr:list):
        #se cuenta el total de cada forma.
        #matriz completa
        tT = 0
        for i in Myarr:
            tT += sum(i)
        #la incompleta de C
        tC = 0
        for i in range(len(Myarr)):
            for j in range(c):
                tC += Myarr[i][j]
        #la incompleta de D
        tD = 0
        for i in range(d):
            for j in range(len(Myarr[i])):
                tD +=Myarr[i][j]
        #la restante c y d
        tF = 0
        for i in range(d):
            for j in range(c):
                tF+=Myarr[i][j]
        
        #se calcula el total de costo juntando todas.
        #completos
        cost = a*b*tT
        #incompletos
        cost+=(tC*b)+(tD*c)+(tF)
        return cost

    minCost = getCost(arr)

    #mover filas
    for bucleOne in range(r):
        auxi = getCost(arr)
        if auxi<minCost:
            minCost = auxi
        #mover columnas
        for bucleTwo in range(ce-1):
            moveColumn(arr,r,ce)
            aux = getCost(arr)
            if aux<minCost:
                minCost = aux
        
        moveRow(arr,r,ce)
    
    return minCost


            










class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    teCa = [
        [
            2,3,5,8,
            [
                [5,2,3],
                [2,3,1]
            ]
        ],
        [
            2,3,6,9,
            [
                [5,2,3],
                [2,3,1]
            ]
        ]
    ]

    salidas = [
        98,98
    ]

    for i in range(len(teCa)):
        solution = None
        try:
            solution = solucionar(teCa[i][0],teCa[i][1],teCa[i][2],teCa[i][3],teCa[i][4],) #parameters
            assert solution == salidas[i]
            print(
                bcolors.OK+"\nCORRECT ANSWER:"+bcolors.RESET+f"\ntest {teCa[i]}, result {solution}")
        except Exception as error:
            print(
                bcolors.FAIL+"\nERROR: "+bcolors.RESET+f"\ntest {teCa[i]}, "+bcolors.WARNING+"\nExpected "+bcolors.RESET+f"{salidas[i]}, "+bcolors.WARNING+"\nCalculated "+bcolors.RESET+f"{solution}", error)

testCode()