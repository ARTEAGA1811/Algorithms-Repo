def solucionar(nums:list):
    nums = {int(x,2) for x in nums}
    aux = {int(x) for x in range(0,2**len(nums))}
    aux = aux - nums
    for i in aux:
        newAux = bin(i)[2:]
        #add n zeros to the left
        newAux = "0"*(len(nums)-len(newAux))+newAux
        return newAux
    

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        ["01","10"],
        ["111","011","001"]
    ]

    salidas = [
        "11",
        "101"

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