#https://leetcode.com/problems/next-greater-element-i/
def solucionar(nums1:list, nums2:list):
    dic = {}
    for i in enumerate(nums2):
        dic[i[1]] = i[0]
    for j in range(len(nums1)):
        indFound = dic[nums1[j]]
        if indFound == len(nums2)-1:
            nums1[j] = -1
        else:
            nums1[j] = -1
            for k in range(indFound+1, len(nums2)):
                if nums2[k] > nums2[indFound]:
                    nums1[j] = nums2[k]
                    break
    return nums1


class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    casosPrueba = [
        [
            [2,4],[1,2,3,4]
        ],
        [
            [4,1,2],[1,3,4,2]
        ],
        [
            [1,3,5,2,4],
            [6,5,4,3,2,1,7]
        ]
    ]

    salidas = [
        [3,-1],
        [-1,3,-1],
        [7,7,7,7,7]
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