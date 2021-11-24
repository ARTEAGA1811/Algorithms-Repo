import tkinter

class MyOption:
    def __init__(self, my_position, my_victories, my_defeats, my_ties):
        self.my_position = my_position
        self.my_victories = my_victories
        self.my_defeats = my_defeats
        self.my_ties = my_ties
    
    def getNumOfVictories(self):
        return len(self.my_victories)

    def getNumOfDefeats(self):
        return len(self.my_defeats)
    
    def getNumOfTies(self):
        return len(self.my_ties)
    
    def getAllLevels(self, myList:list):
        listwithoutRepetion = list(set(myList))
        listwithoutRepetion.sort()
        return listwithoutRepetion
    
    def getCountOf(self, numMin: int, nuewList:list):
        return nuewList.count(numMin)

    def getDictLevelsVictories(self):
        miDiccVic = {}
        for i in self.getAllLevels(self.my_victories):
            miDiccVic[i] = self.my_victories.count(i)
        return miDiccVic

    def getDictLevelsTies(self):
        miDiccTies = {}
        for i in self.getAllLevels(self.my_ties):
            miDiccTies[i] = self.my_ties.count(i)
        return miDiccTies

    def getDictLevelsDefeats(self):
        miDiccDef = {}
        for i in self.getAllLevels(self.my_defeats):
            miDiccDef[i] = self.my_defeats.count(i)
        return miDiccDef
        
         
    def myToString(self):
        print('My position: ', self.my_position)
        # print('\nVictories: ', self.my_victories)
        # print('\nDefeates: ', self.my_defeats)
        # print('\nTies: ', self.my_ties)
        print('\nTotal Victories: ', self.getNumOfVictories())
        for i in self.getAllLevels(self.my_victories):
            print('Level '+str(i)+': '+ str(self.my_victories.count(i)))
        print('\nTotal Defeates: ', self.getNumOfDefeats())
        for i in self.getAllLevels(self.my_defeats):
            print('Level '+str(i)+': '+ str(self.my_defeats.count(i)))
        print('\nTotal Ties: ', self.getNumOfTies())
        for i in self.getAllLevels(self.my_ties):
            print('Level '+str(i)+': '+ str(self.my_ties.count(i)))
        

def draw():
    ventana = tkinter.Tk()
    ventana.geometry("600x600")
    #ventana.resizable(False,False)
    etiqueta = tkinter.Label(ventana, text="3 EN RAYA", bg="Yellow", padx=40, font="Helvetica 40")
    ventana.title("Juego 3 en raya")
    def getIndice(myInd):
        i = myInd.split()
        if myInd == '0 0':
            btn1["state"] = "disabled"
            btn1["bg"] = "Gray"
        elif(myInd == '0 1'):
            btn2["state"] = "disabled"
            btn2["bg"] = "Gray"
        elif(myInd == '0 2'):
            btn3["state"] = "disabled"
            btn3["bg"] = "Gray"
        elif(myInd == '1 0'):
            btn4["state"] = "disabled"
            btn4["bg"] = "Gray"
        elif(myInd == '1 1'):
            btn5["state"] = "disabled"
            btn5["bg"] = "Gray"
        elif(myInd == '1 2'):
            btn6["state"] = "disabled"
            btn6["bg"] = "Gray"
        elif(myInd == '2 0'):
            btn7["state"] = "disabled"
            btn7["bg"] = "Gray"
        elif(myInd == '2 1'):
            btn8["state"] = "disabled"
            btn8["bg"] = "Gray"
        elif(myInd == '2 2'):
            btn9["state"] = "disabled"
            btn9["bg"] = "Gray"
        #print([int(i[0]), int(i[1])])
        return [int(i[0]), int(i[1])]

    btn1 = tkinter.Button(ventana, text="", font = "Helvetica", padx=60, pady=60, bg="Yellow", command= lambda: getIndice("0 0"))
    btn2 = tkinter.Button(ventana, text="", font = "Helvetica 10", padx=60, pady=60, bg="Yellow",command= lambda: getIndice("0 1"))
    btn3 = tkinter.Button(ventana, text="", font = "Helvetica 10", padx=60, pady=60, bg="Yellow", command= lambda: getIndice("0 2"))
    btn4 = tkinter.Button(ventana, text="", font = "Helvetica 10", padx=60, pady=60, bg="Yellow",command= lambda: getIndice("1 0"))
    btn5 = tkinter.Button(ventana, text="", font = "Helvetica 10", padx=60, pady=60, bg="Yellow",command= lambda: getIndice("1 1"))
    btn6 = tkinter.Button(ventana, text="", font = "Helvetica 10", padx=60, pady=60, bg="Yellow",command= lambda: getIndice("1 2"))
    btn7 = tkinter.Button(ventana, text="", font = "Helvetica 10", padx=60, pady=60, bg="Yellow",command= lambda: getIndice("2 0"))
    btn8 = tkinter.Button(ventana, text="", font = "Helvetica 10", padx=60, pady=60, bg="Yellow",command= lambda: getIndice("2 1"))
    btn9 = tkinter.Button(ventana, text="", font = "Helvetica 10", padx=60, pady=60, bg="Yellow",command= lambda: getIndice("2 2"))

    btn1.grid(row = 1, column = 0)
    btn2.grid(row = 1, column = 1)
    btn3.grid(row = 1, column = 2)
    btn4.grid(row = 2, column = 0)
    btn5.grid(row = 2, column = 1)
    btn6.grid(row = 2, column = 2)
    btn7.grid(row = 3, column = 0)
    btn8.grid(row = 3, column = 1)
    btn9.grid(row = 3, column = 2)

    ventana.mainloop()

def getAnalysis(listaRegistros: list):
    counter = 1
    for bucle in listaRegistros:
        print("NUMBER ", counter)
        bucle.myToString()
        print('\n')
        print('************************')
        print('************************')
        print('************************')
        counter += 1
        print('------------------------------------------------------------------\n')

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
            if matriz[i][k] == 0:
                return False
    return True

def getAllPosiblesCases(matriz, row, col, turnOf, other, level, reg):
    #BASE CASES
    if thereAre3Completed(matriz, 2):
        reg['V'].append(level)
        return 10
    if thereAre3Completed(matriz, 1):
        reg['D'].append(level)
        return -2
    if isFullMatriz(matriz):
        reg['T'].append(level)
        return 1
    if matriz[row][col] == 0:
        return 0

    #RECURSIVE CASES
    #there are 9 positions in the matrix, so i'm going to check all of this ones.
    total = []
    for i in range(len(matriz)): #iterate rows
        for k in range(len(matriz[i])): #iterate columns
            if matriz[i][k] == 0:
                #change the matriz for a while
                matriz[i][k] = turnOf
                aux = getAllPosiblesCases(matriz, i, k, other, turnOf, level+1, reg)
                #Return to its original model
                matriz[i][k] = 0
                total.append(aux)
    #return again to its original model
    matriz[row][col] = 0
    return sum(total)

def getBestMove(logList: list[MyOption]):
    #check if there are logs with victories.
    thereareVictories = False
    thereAreTies = False
    for a in logList:
        if a.getNumOfVictories()>0:
            thereareVictories = True
        if a.getNumOfTies()>0:
            thereAreTies = True
    
    if thereareVictories:
        regVic = [] #all objects which have the min level.
        filtOneV = []
        validOptions = []
        for b in logList:          
            if b.getNumOfVictories()>0:
                minVict = min(b.getAllLevels(b.my_victories))
                if b.getNumOfTies()>0:
                    minTies = min(b.getAllLevels(b.my_ties))
                    if minTies<minVict:
                        continue
                if b.getNumOfDefeats()>0:
                    minDef = min(b.getAllLevels(b.my_defeats))
                    if minDef<minVict:
                        continue
                validOptions.append(minVict)
                filtOneV.append(b)
        
        if len(validOptions)>0:
 
            minValid = min(validOptions)
            #guardo los objetos que tengan este minimo.
            for b in filtOneV:
                if b.getNumOfVictories()>0:
                    if min(b.getAllLevels(b.my_victories)) == minValid:
                        regVic.append(b)
            
            if len(regVic)>1:

                #elijo el que mas tenga victorias en este nivel.
                regValidTwo = [] #guardo el numero de victorias en el nivel, de cada opcion.
                
                for i in regVic:
                    aux = i.getCountOf(minValid, i.my_victories)     
                    regValidTwo.append(aux)
                
                myMaxvalue = max(regValidTwo) #elijo al mayor numero de victorias en ese level.
                #recorro la lista y selecciono el unico que cumple.
                if regValidTwo.count(myMaxvalue) == 1:
                    for i in regVic:
                        if i.getCountOf(minValid,i.my_victories) == myMaxvalue:
                            #return i.my_position
                            return [i] #*****
                    
                    print('algo paso mal aqui.')
                else:
                    print('Mensaje de alerta 1, hay mas de una posibilidad.')
                    new_objectsValids = []
                    for i in regVic:
                        if i.getCountOf(minValid,i.my_victories) == myMaxvalue:
                            new_objectsValids.append(i)
                    return new_objectsValids #*******
                
            elif(len(regVic) == 1):
                #elijo este como el mejor y retorno la posicion.
                #return regVic[0].my_position
                return regVic #******
            else:
                print('Error grave, analisis profundo 1.')
                return [] #******
        else:
            print('Error, caso extranio numero 1.')
            return [] #******

    elif(thereAreTies):
        regTies = []
        filtOneT = []
        validOptions = []
        for c in logList:
            if c.getNumOfTies()>0:
                minTies = min(c.getAllLevels(c.my_ties))
                if c.getNumOfDefeats()>0:
                    minDef = min(c.getAllLevels(c.my_defeats))
                    if minDef<minTies:
                        continue
                validOptions.append(minTies)
                filtOneT.append(c)
        
        if len(validOptions)>0:
            minValid = min(validOptions)
            #guardo los objetos que tengan este minimo
            for c in filtOneT:
                if c.getNumOfTies()>0:
                    if min(c.getAllLevels(c.my_ties)) == minValid:
                        regTies.append(c)

            if len(regTies)>1:
                                #elijo el que mas tenga victorias en este nivel.
                regValidTwo = [] #guardo el numero de victorias en el nivel, de cada opcion.
                for i in regTies:
                    aux = i.getCountOf(minValid, i.my_ties)     
                    regValidTwo.append(aux)
                
                myMaxvalue = max(regValidTwo) #elijo al mayor numero de victorias en ese level.
                #recorro la lista y selecciono el unico que cumple.
                if regValidTwo.count(myMaxvalue) == 1:
                    for i in regTies:
                        if i.getCountOf(minValid,i.my_ties) == myMaxvalue:
                            #return i.my_position
                            return [i] #***********
                    
                    print('algo paso mal aqui.')
                else:
                    print('Mensaje de alerta 2, hay mas de una posibilidad.')
                    new_objectsValids = []
                    for i in regTies:
                        if i.getCountOf(minValid,i.my_ties) == myMaxvalue:
                            new_objectsValids.append(i)
                    return new_objectsValids #*******

              
            elif(len(regTies) == 1):
                #elijo este como el mejor y retorno la posicion.
                #return regTies[0].my_position
                return regTies #********
            else:
                print('Error grave, analisis profundo 2.')
                return [] #******
        else:
            print('Error, caso extranio numero 2.')
            return [] #******
    else:
        #aqui es que solo hay derrotas
        print('Mensaje grave, solo existieron posibles derrotas.')
        return [] #******




def solucionar(matriz):
    #I must obtain the best total of the possible moves.
    listaRegistros = []
    for i in range(len(matriz)): #iterate rows
        for k in range(len(matriz[i])): #iterate columns
            if matriz[i][k] == 0: #if this space is empty
                matriz[i][k] = 2 #I set my X here.
                miReg = {'V': [], 'D': [], 'T': [] } #start a log.
                getAllPosiblesCases(matriz, i, k, 1, 2, 1, miReg)
                miReg['V'].sort()
                miReg['D'].sort()
                miReg['T'].sort()
                listaRegistros.append(MyOption([i,k],miReg['V'],miReg['D'],miReg['T']))
                #I must return to the original, because
                #I have to calculate the other posibilities.
                matriz[i][k] = 0 

    print("*********************************ANALISIS DE TODOS LOS REGISTROS.**********************************")
    getAnalysis(listaRegistros) 
    print("\n\n*********************************************ANALISIS DE LOS CASOS ELEGIDOS.***************************************")
    auxLIst =  getBestMove(listaRegistros)
    getAnalysis(auxLIst)   
    gg = [1,1]
    return(gg)
    
    

def testCode():
    casosPrueba = [
        [
            [1,0,0],
            [0,0,0],
            [2,0,0]
        ]
      
    ]

    salidas = [
        [1,1]
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

# testCode()


a = [
        [1,0,0],
        [0,0,0],
        [2,0,0]
    ]

b = [
        [1,0,0],
        [0,0,0],
        [2,1,2]
    ]

c = [
        [1,0,2],
        [0,1,0],
        [2,1,2]
    ]

d = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

e = [
         [1,2,1],
         [2,0,0],
         [2,0,1]
     ]

#solucionar(a)
#solucionar(b)
#solucionar(c)
#solucionar(e)


##########################333
def newTest():
    print("*********JUEGO 3 EN RAYA********")
    m = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    print("Modelo Actual: ")
    for i in m:
        print(i)
    while(True):
        enX = input('Posicion a colocar la X: ')
        enX = enX.split(',')
        #se coloca la X
        m[int(enX[0])][int(enX[1])] = 2
        print("Modelo Actual: ")
        for i in m:
            print(i)
        
        enY = input('Posicion a colocar la Y: ')
        enY = enY.split(',')
        #se coloca la Y
        m[int(enY[0])][int(enY[1])] = 1
        print("Modelo Actual: ")
        for i in m:
            print(i)

        #se realiza el analisis de best move.
        solucionar(m)



newTest()
