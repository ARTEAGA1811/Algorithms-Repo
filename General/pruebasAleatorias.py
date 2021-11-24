# import string

# def textToNumberGenerator(s:str):
#     if s == '-':
#         return 0
#     return string.ascii_lowercase.index(s.lower())+1

# x = [
#             'ABCDE-FGHIJ',
#             'ACEGI-BDFHJ',
#             'ABCKL-FDEMN',
#             'EGOBH-IJLMN',
#             'DEGKL-FMIBC'
#         ]

# balanceList = []
# for i in range(len(x)):
#     balanceList.append(list(map(textToNumberGenerator, x[i])))

# print(balanceList)

# import itertools

# a = [1+i for i in range(11)]
# print(a)


# aux = {elemento:[]  for elemento in itertools.combinations(a, 2)}

# print(aux)

# for i in aux:
#     numChosen = i[0]
    

# arrUno = [1,5,7,9]
# arrDos = [1,5,7,1]

# print(arrUno == arrDos)


# def main():
#     e = input().split(',')
#     print(e)
#     mybalanceList = []
#     for i in range(int(e[1])):
#         aux = input()
#         mybalanceList.append(aux)
    
#     print(mybalanceList)

# main()



# #https://csacademy.com/ieeextreme-practice/task/xtreme-fake-coins/
# import string
# import itertools

# def textToNumberGenerator(s:str):
#     if s == '-':
#         return 0
#     return string.ascii_lowercase.index(s.lower())+1

# def numbersToLetters(t: tuple):
#     one = chr(ord('@')+t[0])
#     two = chr(ord('@')+t[1])
#     return one+two

# def solucionar(num:int,values: list):
#     if len(values) == 0:
#         return []
    
#     balanceList = []
#     for i in range(len(values)):
#         balanceList.append(list(map(textToNumberGenerator, values[i])))

#     aux = [1+i for i in range(num)]
#     allCombinations = {elemento:[]  for elemento in itertools.combinations(aux, 2)}

#     if len(allCombinations)  == 1:
#         return []
    
#     #recorro el diccionario.
#     for i in allCombinations:
#         #recorro la listaDeBalance
#         for k in balanceList:
#             numAux = 0
#             indCenter = int((len(k)-1)/2)
#             #accedo al primer valor de la clave , ejm: (1,2) -> accedo a 1.
#             numChosen = i[0]
#             #busco en el array d balance list.
#             if numChosen in k:             
#                 myPos = k.index(numChosen)
#                 if myPos<indCenter: 
#                     numAux = 1
#                 else:
#                     numAux = -1
            
#             #accedo al primer valor de la clave , ejm: (1,2) -> accedo a 2
#             numChosen = i[1]
#             #busco en el array d balance list.
#             if numChosen in k:
#                 myPos = k.index(numChosen)
#                 if myPos<indCenter: 
#                     numAux += 1
#                 else: 
#                     numAux += -1
            
#             #agrego mayor, menor o igual
#             if numAux>0:
#                 allCombinations[i].append(1)
#             elif(numAux<0):
#                 allCombinations[i].append(2)
#             else:
#                 allCombinations[i].append(3)

#     # ahora comparo los arrays que sean iguales
#     myKeyList = list(allCombinations.keys())
#     coincidences = []
#     for x in range(len(allCombinations)-1):
#         for y in range(x+1, len(allCombinations)):
#             if allCombinations[myKeyList[x]] == allCombinations[myKeyList[y]]:
#                 coincidences.append(numbersToLetters(myKeyList[x]) + '='+numbersToLetters(myKeyList[y]))
                
    
#     return coincidences


# #####################

# def main():

    
#     e = input().rstrip('\n').split(',')
#     mybalanceList = []
#     for i in range(int(e[1])):
#         aux = input()
#         mybalanceList.append(aux)
    
#     newList = solucionar(int(e[0]), mybalanceList)
#     for i in newList:
#         print(i)
        
    
# main()
    
    
# for i in range(3,3,-1):
#     print('xd')

# a = [2,1,5]
# numStri = ''
# for k in a:
#     numStri+=str(k)

# mynumber = int(numStri) + 806
# nynumberStr = str(mynumber)
# l = []
# for i in nynumberStr:
#     l.append(i)

# print(l)

# import re
# regex = re.compile('[^a-zA-Z]')
# myTex = regex.sub('', '')
# print(myTex)

# import itertools
# a = [1,2,3,6]
# # arrAux = a[:3]+a[3+1:]
# # print(arrAux)

# # l = list(itertools.combinations(a,3))
# # print(l)

# a = set((28, 8, 49))
# b = set((28, 49, 8))

# if a == b:
#     print('a')

a = (0+3)//2
print(a)