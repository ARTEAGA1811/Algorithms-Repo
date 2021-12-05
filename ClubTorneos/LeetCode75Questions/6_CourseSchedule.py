#https://leetcode.com/problems/course-schedule/
def myFunction(numCourses, prerequisites):
    myDict = {}
    for i in range(numCourses):
        myDict[i] = set()
    for i in range(len(prerequisites)):
        if prerequisites[i][0] == prerequisites[i][1]:
            return False
        if prerequisites[i][1] in myDict[prerequisites[i][0]]:
            return False
        myDict[prerequisites[i][1]].add(prerequisites[i][0])
        myDict[prerequisites[i][1]].update(myDict[prerequisites[i][0]])

    #there are some case where the fail is not deteted, so I need to check if there's a 
    #fail when I finish the loop.
    for clave, valor in myDict.items():
        for i in valor:
            if clave in myDict[i]:
                return False   
    return True



class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        [
            2,[[1,0]]
        ],
        [
            2,[[1,0],[0,1]]
        ],
        [
            
            20,[[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
        ],
        [
            4,[[0,1],[2,3],[1,2],[3,0]]
        ]
    ]

    salidas = [
        True,
        False,
        False,
        False
    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = myFunction(casosPrueba[i][0],casosPrueba[i][1]) #parameters
            assert solution == salidas[i]
            print(
                bcolors.OK+"\nCORRECT ANSWER:"+bcolors.RESET+f"\ntest {casosPrueba[i]}, result {solution}")
        except Exception as error:
            print(
                bcolors.FAIL+"\nERROR: "+bcolors.RESET+f"\ntest {casosPrueba[i]}, "+bcolors.WARNING+"\nExpected "+bcolors.RESET+f"{salidas[i]}, "+bcolors.WARNING+"\nCalculated "+bcolors.RESET+f"{solution}", error)

testCode()