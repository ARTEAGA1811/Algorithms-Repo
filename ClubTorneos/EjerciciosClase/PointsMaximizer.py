def dfs(ind:int, logs:dict, rooms:list):
    #Base case
    if ind in logs:
        return logs[ind]
    #Recursive case
    aux = rooms[ind]
    for j in range(ind+2,len(rooms)):
        aux = max(aux, dfs(j,logs,rooms)+rooms[ind])
    logs[ind] = aux
    return aux

def myFunction(rooms:list):
    if len(rooms) == 1:
        return rooms[0]
    logs = {len(rooms)-1:rooms[-1], len(rooms)-2:rooms[-2]}
    return max(dfs(0, logs, rooms[:-1]), dfs(1, logs, rooms), dfs(len(rooms)-1, logs, rooms[1:]))



class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        # [1,2],
        # [2,1,3],
        [1,2,7,4,2]

    ]

    salidas = [
        # 2,
        # 3,
        9

    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = myFunction(casosPrueba[i]) #parameters
            assert solution == salidas[i]
            print(
                bcolors.OK+"\nCORRECT ANSWER:"+bcolors.RESET+f"\ntest {casosPrueba[i]}, result {solution}")
        except Exception as error:
            print(
                bcolors.FAIL+"\nERROR: "+bcolors.RESET+f"\ntest {casosPrueba[i]}, "+bcolors.WARNING+"\nExpected "+bcolors.RESET+f"{salidas[i]}, "+bcolors.WARNING+"\nCalculated "+bcolors.RESET+f"{solution}", error)

testCode()