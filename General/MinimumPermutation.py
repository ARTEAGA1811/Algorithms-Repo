#https://csacademy.com/ieeextreme-practice/task/minimum-permutation/statement/

def solucionar(a:list,s:list):
    s.sort()
    lastIndex = 0
    for i in range(len(s)):
        found = False
        for k in range(lastIndex,len(a)):
            if a[k] > s[i]:
                found = True
                a.insert(k,s[i])
                lastIndex = k+1
                break

        if not found:
            a.extend(s[i:])
            break
    return a




class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        [
            [3,1,5],
            [4,2,9,10,34]
        ]
    ]

    salidas = [
        [2,3,1,4,5]
    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(casosPrueba[i][0],casosPrueba[i][1]) #parameters
            assert solution == salidas[i]
            print(
                bcolors.OK+"\nCORRECT ANSWER:"+bcolors.RESET+f"\ntest {casosPrueba[i]}, result {solution}")
        except Exception as error:
            print(
                bcolors.FAIL+"\nERROR: "+bcolors.RESET+f"\ntest {casosPrueba[i]}, "+bcolors.WARNING+"\nExpected "+bcolors.RESET+f"{salidas[i]}, "+bcolors.WARNING+"\nCalculated "+bcolors.RESET+f"{solution}", error)

testCode()