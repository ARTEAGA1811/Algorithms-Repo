#https://leetcode.com/contest/weekly-contest-123/problems/satisfiability-of-equality-equations/

def solucionar(equations: list[str]):
    counter = 0
    logs = {}
    for k in equations:
        #no hay ninguna registrada
        if k[0] not in logs and k[3] not in logs:
            #verifico si son las mismas
            if k[0] == k[3]:
                if k[1] == '!':
                    return False
                else:
                    counter+=1
                    logs[k[0]] = counter
                    logs[k[3]] = counter
            else:
                counter+=1
                logs[k[0]] = counter
                if k[1] == '!':
                    counter+=1
                    logs[k[3]] = counter
                else:
                    logs[k[3]] = counter
        
        #hay solo una registrada
        elif (k[0] not in logs and k[3] in logs):
            if k[1] == '!':
                counter +=1
                logs[k[0]] = counter
            else:
                logs[k[0]] = logs[k[3]]
        
        elif (k[0] in logs and k[3] not in logs):
            if k[1] == '!':
                counter +=1
                logs[k[3]] = counter
            else:
                logs[k[3]] = logs[k[0]]
        
        #ya estan los dos registrados
        elif (k[0] in logs and k[3] in logs):
            if k[1] == '!':
                if logs[k[0]] != logs[k[3]]:
                    continue
                else:
                    return False
            else:
                if logs[k[0]] == logs[k[3]]:
                    continue
                else:
                    return False
    return True
        
                

def testCode():
    casosPrueba = [
    #   ["a==b","b!=a"],
    #   ["b==a","a==b"],
    #   ["a==b","b==c","a==c"],
    #   ["a==b","b!=c","c==a"],
    #   ["c==c","b==d","x!=z"],
      ["c==c","f!=a","f==b","b==c"]
    ]

    salidas = [
        # False, True, True, False,True,
        True
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

testCode()