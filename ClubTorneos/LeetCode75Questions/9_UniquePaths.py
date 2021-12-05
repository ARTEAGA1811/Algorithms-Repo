#https://leetcode.com/problems/unique-paths/

def myFunction(m:int, n:int) -> int:
    #total = 0
    logs = {(m-1,n-1):1}
    def dfs(i,j):
        #BASE CASES
        if (i,j) in logs:
            return logs[(i,j)]
        #llega a los limites
        if i==m or j==n:
            logs[(i,j)] = 1
            return 1           

        #RECURSIVE CASES
        return dfs(i+1,j) + dfs(i,j+1)

    return dfs(0,0)



        
        




class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        # [7,3],
        [3,3],
        [1,1]
    ]

    salidas = [
        # 28,
        6,
        1

    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = myFunction(casosPrueba[i][0], casosPrueba[i][1]) #parameters
            assert solution == salidas[i]
            print(
                bcolors.OK+"\nCORRECT ANSWER:"+bcolors.RESET+f"\ntest {casosPrueba[i]}, result {solution}")
        except Exception as error:
            print(
                bcolors.FAIL+"\nERROR: "+bcolors.RESET+f"\ntest {casosPrueba[i]}, "+bcolors.WARNING+"\nExpected "+bcolors.RESET+f"{salidas[i]}, "+bcolors.WARNING+"\nCalculated "+bcolors.RESET+f"{solution}", error)

testCode()