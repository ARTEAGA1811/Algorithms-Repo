#https://csacademy.com/ieeextreme-practice/task/d48ada9a7213299f1b24b22b2fb9443f/



def solucionar(r, li:list):
    import re
    import math
    regex = re.compile('[^a-zA-Z]')
    #r = int(input())
    letterDeg = {}
    # for i in range(26):
    #     aux = input().split()
    #     letterDeg[aux[0].upper()] = float(aux[1])

    for i in range(26):
        letterDeg[li[i][0].upper()] = float(li[i][1])
    
    #a= input()
    a = li[26]
    phrase = regex.sub('', a)
    phrase = phrase.upper()

    #start algorythm
    lenThread = r
    firDeg:float = letterDeg[phrase[0]]

    for i in range(1,len(phrase)):
        secDeg:float = letterDeg[phrase[i]]
        midDeg = secDeg-firDeg
        if midDeg<0:
            midDeg = midDeg*-1      
        #aumento la distancia del hilo
        lenThread+= float(math.sqrt(2*(r**2)-(2*(r**2)*math.cos(math.radians(midDeg)))))
        #le agrego los nuevos valores.
        firDeg = secDeg
    
    return round(lenThread)






def testCode():
    casosPrueba = [
        [
            52,
            [
                ['A', 168.05],
                ['B', 41.27],
                ['C' ,119.19],
                ['D' ,312.43],
                ['E' ,236.94],
                ['F' ,269.85],
                ['G' ,318.46],
                ['H' ,206.02],
                ['I' ,140.19],
                ['J' ,162.81],
                ['K' ,199.80],
                ['L' ,207.06],
                ['M' ,217.69],
                ['N' ,220.22],
                ['O' ,282.10],
                ['P' ,80.42],
                ['Q' ,312.29],
                ['R' ,324.76],
                ['S' ,348.38],
                ['T' ,311.84],
                ['U' ,289.66],
                ['V' ,137.41],
                ['W' ,175.23],
                ['X' ,0.47],
                ['Y' ,198.07],
                ['Z', 251.39],
                'IEEEXtreme rocks!'
            ]
        ]    


    ]

    salidas = [
        763
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