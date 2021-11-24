def solucionar(words:list):
    if len(words) == 1:
        return []
    valids = []
    aux = {x:0 for x in words[0]}
    selected = words[0]
    for i in range(len(selected)): #iterate over the first word
        flag = True
        aux[selected[i]] += 1
        for j in range(1,len(words)): #iterate over the rest of the words
            if selected[i] not in words[j]:
                flag = False
                break
            if words[j].count(selected[i]) < aux[selected[i]]:
                flag = False
                break
        if flag:
            valids.append(selected[i])
    return valids



class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        ["bella","label","roller"],
        ["cool","lock","cook"]
    ]

    salidas = [
        ["e","l","l"],
        ["c","o"]
    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(casosPrueba[i]) #parameters
            assert solution == salidas[i]
            print(
                bcolors.OK+"\nCORRECT ANSWER:"+bcolors.RESET+f"\ntest {casosPrueba[i]}, result {solution}")
        except Exception as error:
            print(
                bcolors.FAIL+"\nERROR: "+bcolors.RESET+f"\ntest {casosPrueba[i]}, "+bcolors.WARNING+"\nExpected "+bcolors.RESET+f"{salidas[i]}, "+bcolors.WARNING+"\nCalculated "+bcolors.RESET+f"{solution}", error)

testCode()