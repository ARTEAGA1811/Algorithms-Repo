#https://leetcode.com/contest/weekly-contest-232/problems/check-if-one-string-swap-can-make-strings-equal/

def solucionar(s1:str, s2:str):
    if s1 == s2:
        return True
    changes = 0
    expS1 = ''
    expS2 = ''
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if changes == 0:
                expS1 = s2[i]
                expS2 = s1[i]
                changes+=1
            elif(changes == 1):
                if s1[i] != expS1 or s2[i] != expS2:
                    return False
                changes+=1
            else:
                return False
    
    if changes == 2:
        return True
    return False

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        ['bank','kanb'],
        ['caa','aaz']
    ]

    salidas = [
        True,False
    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(casosPrueba[i][0], casosPrueba[i][1]) #parameters
            assert solution == salidas[i]
            print(
                bcolors.OK+"\nCORRECT ANSWER:"+bcolors.RESET+f"\ntest {casosPrueba[i]}, result {solution}")
        except Exception as error:
            print(
                bcolors.FAIL+"\nERROR: "+bcolors.RESET+f"\ntest {casosPrueba[i]}, "+bcolors.WARNING+"\nExpected "+bcolors.RESET+f"{salidas[i]}, "+bcolors.WARNING+"\nCalculated "+bcolors.RESET+f"{solution}", error)

testCode()