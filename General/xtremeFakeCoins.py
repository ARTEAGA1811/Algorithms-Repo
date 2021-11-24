#https://csacademy.com/ieeextreme-practice/task/xtreme-fake-coins/
import string
import itertools

def textToNumberGenerator(s:str):
    if s == '-':
        return 0
    return string.ascii_lowercase.index(s.lower())+1

def numbersToLetters(t: tuple):
    one = chr(ord('@')+t[0])
    two = chr(ord('@')+t[1])
    return one+two

def solucionar(num:int,values: list):
    if len(values) == 0:
        return None
    
    balanceList = []
    for i in range(len(values)):
        balanceList.append(list(map(textToNumberGenerator, values[i])))

    aux = [1+i for i in range(num)]
    allCombinations = {elemento:[]  for elemento in itertools.combinations(aux, 2)}

    print(balanceList)
    print(allCombinations)   
    if len(allCombinations)  == 1:
        return None
    
    #recorro el diccionario.
    for i in allCombinations:
        #recorro la listaDeBalance
        for k in balanceList:
            numAux = 0
            indCenter = int((len(k)-1)/2)
            #accedo al primer valor de la clave , ejm: (1,2) -> accedo a 1.
            numChosen = i[0]
            #busco en el array d balance list.
            if numChosen in k:             
                myPos = k.index(numChosen)
                if myPos<indCenter: 
                    numAux = 1
                else:
                    numAux = -1
            
            #accedo al primer valor de la clave , ejm: (1,2) -> accedo a 2
            numChosen = i[1]
            #busco en el array d balance list.
            if numChosen in k:
                myPos = k.index(numChosen)
                if myPos<indCenter: 
                    numAux += 1
                else: 
                    numAux += -1
            
            #agrego mayor, menor o igual
            if numAux>0:
                allCombinations[i].append(1)
            elif(numAux<0):
                allCombinations[i].append(2)
            else:
                allCombinations[i].append(3)

    # ahora comparo los arrays que sean iguales
    print(allCombinations)
    myKeyList = list(allCombinations.keys())
    
    for x in range(len(allCombinations)-1):
        for y in range(x+1, len(allCombinations)):
            if allCombinations[myKeyList[x]] == allCombinations[myKeyList[y]]:
                
                print(numbersToLetters(myKeyList[x]) + '='+numbersToLetters(myKeyList[y]))

def testCode():
    casosPrueba = [
        [
            'ABCDE-FGHIJ',
            'ACEGI-BDFHJ',
            'ABCKL-FDEMN',
            'EGOBH-IJLMN',
            'DEGKL-FMIBC'
        ]

        
    ]

    salidas = [

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

#####################

#11
a = [
    'ABCDE-FGHIJ',
    'AHJ-FBD',
    'AGI-KCE',
    'BJ-IE'
]
solucionar(11, a)

#15
b = [
             'ABCDE-FGHIJ',
             'ACEGI-BDFHJ',
             'ABCKL-FDEMN',
             'EGOBH-IJLMN',
             'DEGKL-FMIBC'
         ]
#solucionar(15, b)

c = [
    'ADE-BCG',
    'AG-BE',
    'AC-DG'
]
#solucionar(7, c)