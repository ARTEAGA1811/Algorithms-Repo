#https://leetcode.com/contest/weekly-contest-74/problems/number-of-subarrays-with-bounded-maximum/


def solucionar(nums: list[int], left: int, right: int):
    increase = 1
    total = 0
    aux = False
    maxValue = 0
    reduce = 1
    notValid = 0
    for i in nums:
        if not aux:
            #busca el maxValue
            if i>=left and i<=right:
                total+=increase
                increase+=1
                maxValue = i
                aux = True
        else:
            if i<=maxValue:
                total+=increase
                increase+=1
                if i<left or i>right:
                    notValid += reduce
                    reduce+=1

            else:
                reduce = 1
                if i>=left and i<=right:
                    total+=increase
                    increase+=1
                    maxValue = i
                else:
                    increase = 1
                    aux = False
    return total-notValid

        



def testCode():
    casosPrueba = [
        # [
        #     [2,1,4,3],
        #     2,
        #     3
        # ],
        # [
        #     [2,9,2,5,6],
        #     2,
        #     8
        # ],
        [
            [73,55,36,5,55,14,9,7,72,52]
            ,32
            ,69
        ]
    ]

    salidas = [
        # 3,7,
        22
    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(casosPrueba[i][0],casosPrueba[i][1],casosPrueba[i][2])
            assert solution == salidas[i]
            print(
                f"respuesta correcta: test {casosPrueba[i]}, result {solution}")
        except Exception as error:
            print(
                f"Error, test {casosPrueba[i]}, expected {salidas[i]}, calculated {solution}", error)

testCode()