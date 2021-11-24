#https://leetcode.com/problems/container-with-most-water/
def solucionar(height:list):
    maxArea = 0
    myLeftMin = height[0]-1 
    lastChecked = len(height)-1
    for i in range(0,len(height)-1):
        if height[i]<=myLeftMin:
            continue
        myLeftMin = height[i]
        mymin = height[-1]-1
        for k in range(lastChecked,i,-1):
            lastChecked = k
            if height[k]>=height[i]:
                newArea= height[i]*(k-i)
                if newArea>maxArea:
                    maxArea = newArea
                
                break
            if height[k]>mymin:
                newArea = height[k]*(k-i)
                if newArea>maxArea:
                    maxArea = newArea
                mymin = height[k]
    return maxArea

#solucion 'optimizada' un poco, una resolucion mejor planteada. O(n)        
def newSolution(height:list):
    left = 0
    right = len(height)-1
    maxArea = 0
    while(left!=right):
        auxArea = min(height[left],height[right]) * (right-left)
        if auxArea>maxArea:
            maxArea = auxArea
        if height[left]>height[right]:
            right-=1
        else:
            left+=1
    return maxArea


            



class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        [1,8,6,2,5,4,8,3,7],
        [1,1],
        [4,3,2,1,4],
        [1,2,1],
        [0,1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1]
    ]

    salidas = [
        49,
        1,
        16,
        2,
        50
    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = newSolution(casosPrueba[i]) #parameters
            assert solution == salidas[i]
            print(
                bcolors.OK+"\nCORRECT ANSWER:"+bcolors.RESET+f"\ntest {casosPrueba[i]}, result {solution}")
        except Exception as error:
            print(
                bcolors.FAIL+"\nERROR: "+bcolors.RESET+f"\ntest {casosPrueba[i]}, "+bcolors.WARNING+"\nExpected "+bcolors.RESET+f"{salidas[i]}, "+bcolors.WARNING+"\nCalculated "+bcolors.RESET+f"{solution}", error)

testCode()