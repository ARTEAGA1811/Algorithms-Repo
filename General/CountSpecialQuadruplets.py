#https://j2logo.com/python/tutorial/tipo-set-python/
import itertools
def solucionar(nums:list):
    cont = 0
    for i in range(3,len(nums)):
        if nums[i]>=3:
            ob = nums[i]
            arrAux = nums[:i]
            li = list(itertools.combinations(arrAux,3))
            for k in li:
                sumat = sum(k)
                if sumat == ob:
                    #print('elegido: ', k, "seleccionado", ob)
                    cont+=1               
    return cont





class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        [1,2,3,6],
        [3,3,6,4,5],
        [1,1,1,3,5],
        [28,8,49,85,37,90,20,8]


    ]

    salidas = [
        1,0,4,
        1
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