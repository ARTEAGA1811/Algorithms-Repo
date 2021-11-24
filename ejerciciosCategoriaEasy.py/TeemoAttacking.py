def solucionar(timeSeries:list, duration:int) -> int:
    cont = 0
    for i in range(len(timeSeries)-1):
        if timeSeries[i]+duration-1 >= timeSeries[i+1]:
            cont += timeSeries[i+1] - timeSeries[i]
        else:
            cont+=duration
    cont+=duration
    return cont


class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        [
            [1,4],2
        ],
        [
            [1,2],2
        ],
        [
            [1,2],5
        ]
        
        
        
    ]

    salidas = [
        4,3,6


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