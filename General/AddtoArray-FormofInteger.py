#https://leetcode.com/contest/weekly-contest-123/problems/add-to-array-form-of-integer/

def solucionar(num: list[int], k: int):
    numStri = ''
    for a in num:
        numStri+=str(a)
    mynumber = int(numStri) + k
    nynumberStr = str(mynumber)
    l = []
    for i in nynumberStr:
        l.append(i)
    return l

    

def testCode():
    casosPrueba = [
      
    ]

    salidas = [

    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(casosPrueba[i])
            assert solution == salidas[i]
            print(
                f"respuesta correcta: test {casosPrueba[i]}, result {solution}")
        except Exception as error:
            print(
                f"Error, test {casosPrueba[i]}, expected {salidas[i]}, calculated {solution}", error)


print(solucionar([2,1,5],806))