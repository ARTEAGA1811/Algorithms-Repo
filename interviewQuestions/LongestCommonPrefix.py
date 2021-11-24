#https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/

def solucionar(mystrs:list):
    if len(mystrs) == 1:
        return mystrs[0]
    selected:str = mystrs[0]

    while selected != '':
        flag = True
        for k in range(1,len(mystrs)):
            if len(selected) > len(mystrs[k]):
                selected = selected[:-1*(len(selected)-len(mystrs[k]))]
                flag = False
                break

            if selected not in mystrs[k][:len(selected)]:
                selected = selected[:-1]
                flag = False
                break
        if flag:
            return selected
    return ''



    

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        ["flower","flow","flight"],
        ["dog","racecar","car"],
        ["c","acc","ccc"]
    ]

    salidas = [
        'fl','',''
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