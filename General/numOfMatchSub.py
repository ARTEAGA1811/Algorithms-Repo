
def solucionar(s:str, arr:list):
    totalAccepted = 0
    # newStri = getCleanedWord(s)
    logAccepted = []
    logRefused = []
    for word in arr:
        if word in logAccepted:
            totalAccepted+=1
            continue   
        if word in logRefused:
            continue
        
        #print('el new String es: ', newStri)
        conter = 0
        for letter in s:
            if letter == word[conter]:
                conter+=1
                if len(word)<=conter:
                    #aqui significa que NO hay mas letras.
                    #y que llegue a la ultima.
                    totalAccepted+=1
                    logAccepted.append(word)
                    break
        logRefused.append(word)
    return totalAccepted
                
        







    

def testCode():
    casosPrueba = [
        [
            "abcde",
            ["a","bb","acd","ace"]
        ],
        [
            "dsahjpjauf",
            ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
        ],
        [
            "rwpddkvbnnuglnagtvamxkqtwhqgwbqgfbvgkwyuqkdwhzudsxvjubjgloeofnpjqlkdsqvruvabjrikfwronbrdyyjnakstqjac",
            ["wpddkvbnn","lnagtva","kvbnnuglnagtvamxkqtwhqgwbqgfbvgkwyuqkdwhzudsxvju","rwpddkvbnnugln","gloeofnpjqlkdsqvruvabjrikfwronbrdyyj","vbgeinupkvgmgxeaaiuiyojmoqkahwvbpwugdainxciedbdkos","mspuhbykmmumtveoighlcgpcapzczomshiblnvhjzqjlfkpina","rgmliajkiknongrofpugfgajedxicdhxinzjakwnifvxwlokip","fhepktaipapyrbylskxddypwmuuxyoivcewzrdwwlrlhqwzikq","qatithxifaaiwyszlkgoljzkkweqkjjzvymedvclfxwcezqebx"]
        ]
      
    ]

    salidas = [
        3,2,5
    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(casosPrueba[i][0], casosPrueba[i][1])
            assert solution == salidas[i]
            print(
                f"respuesta correcta: test {casosPrueba[i]}, result {solution}")
        except Exception as error:
            print(
                f"Error, test {casosPrueba[i]}, expected {salidas[i]}, calculated {solution}", error)
            #print('error')

testCode()