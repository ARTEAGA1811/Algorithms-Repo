#https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/886/

def solucionar(n: int):
    numli = '1'
    if n == 1:
        return numli
    for i in range(n-1):
        cont = 0
        chosen = numli[0]
        aux = ''
        for k in range(len(numli)):
            if chosen == numli[k]:
                cont+=1
            else:
                aux+=str(cont)+chosen
                chosen = numli[k]
                cont=1
  
        if chosen == numli[-1]:
            aux+=str(cont)+chosen

        numli = aux
    return numli


class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        1,2,3,4,5,6,7,8
    ]

    salidas = [
        '1','1','1','1','1','1','1','1'

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