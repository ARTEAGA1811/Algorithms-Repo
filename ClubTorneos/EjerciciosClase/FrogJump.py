def myFunction(arr:list):
    logs = {len(arr)-1:True}
    
    def dfs(i:int):
        #base cases
        if i in logs:
            return logs[i]
        if arr[i] == 0 or i>=len(arr):
            return False        
        
        #recursive case
        aux = False
        for j in range(1,arr[i]+1):
            aux = aux or dfs(i+j)
        logs[i] = aux
        return aux
    
    return dfs(0)




class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        [3,1,1,1],
        [1,0,1],
        [2,5,5,2,5,3,4,0,5,1,0,4,3,2,0,1,1,4,3,0,2,3,1,5,3,5,2,2,1,5,2,5,4,2,4,2,4,0,3,5,2,1,5,1,0,0,4,3,2,4,4,5,0,3,1,4,0,2,1,4,1,0,4,3,5,5,1,5,4,0,2,1,5,2,4,3,5,2,1,2,0,5,2,4,2,1,2,4,5,4,1,0,0,3,3,5,2,0,0,0],
        [1,2,2,5,2,5,2,5,5,4,4,4,4,4,2,4,0,3,3,3,4,2,4,3,2,3,5,0,3,4,2,2,1,1,3,5,2,2,4,4,1,4,1,3,5,3,1,3,1,5,2,0,3,5,5,2,4,0,4,3,1,4,5,0,3,4,5,2,4,5,4,4,1,5,0,4,5,0,5,2,0,5,0,3,3,4,1,5,3,4,1,1,1,2,5,0,3,5,2,1]
    ]

    salidas = [
        True,
        False,
        True,
        True
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