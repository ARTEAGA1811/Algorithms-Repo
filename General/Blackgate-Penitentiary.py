#https://csacademy.com/ieeextreme-practice/task/8761fb7efefcf1d890df1d8d91cae241/




def solucionar(n:int, arr:list):
    #n = int(input())
    gangMembers = {}
    for i in arr:
        if i[1] not in gangMembers:
            gangMembers[i[1]] = [i[0]]
        else:
            gangMembers[i[1]].append(i[0])
      
    listHeights = list(set(list(gangMembers.keys())))
    listHeights.sort()
    aux = 1
    listAux = []
    for i in listHeights:
        gangMembers[i].sort()
        textAux = ''
        for k in gangMembers[i]:
            textAux += k +' '

        textAux+= str(aux) + ' ' + str(aux+len(gangMembers[i])-1)
        #print(textAux)
        listAux.append(textAux)
        aux = aux + len(gangMembers[i])
    return listAux


    
    
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        [
            6,
            [
                ['TheJoker', 180],
                ['HarleyQuin',160],
                ['MrHammer', 220],
                ['Boody', 220],
                ['Muggs', 180],
                ['Paulie', 180]
            ] 
        ],
        [
            10,
            [
                ['a',200],
                ['aa',200],
                ['ab',200],
                ['aba', 200],
                ['aaa' ,200],
                ['b',200],
                ['A',200],
                ['Aa',200],
                ['AB',200],
                ['B',200]
            ]

        ]
    ]

    salidas = [
        [
            'HarleyQuin 1 1',
            'Muggs Paulie TheJoker 2 4',
            'Boody MrHammer 5 6'
        ],
        [
            'A AB Aa B a aa aaa ab aba b 1 10'
        ]
    ]


    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(casosPrueba[i][0],casosPrueba[i][1] )
            assert solution == salidas[i]
            print(
                bcolors.OK+"\nCORRECT ANSWER:"+bcolors.RESET+f"\ntest {casosPrueba[i]}, result {solution}")
        except Exception as error:
            print(
                bcolors.FAIL+"\nERROR: "+bcolors.RESET+f"\ntest {casosPrueba[i]}, "+bcolors.WARNING+"\nExpected "+bcolors.RESET+f"{salidas[i]}, "+bcolors.WARNING+"\nCalculated "+bcolors.RESET+f"{solution}", error)

testCode()