def solucionar(s: str):
    dp = {len(s): 1} #last position in the string

    def dfs(i):
        if i in dp: # si esta ruta ya ha sido pasada.
            return dp[i]
        if s[i] == '0':
            return 0
        res = dfs(i+1)
        # si no esta en el limite, y si cumple con el formato del numero.
        if(i+1< len(s) and (s[i] == '1' or s[i] == '2' and s[i+1] in '0123456')):
            res +=dfs(i+2)
        
        dp[i] = res
        return res

    return dfs(0)


def solucionar2(s: str) -> int:
    dp = {len(s): 1}
    for i in range(len(s)-1,-1,-1):
        if  s[i] == '0':
            dp[i] = 0
        else:
            dp[i] = dp[i+1]
    
        if(i+1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i+1] in "0123456")):
            dp[i] += dp[i+2]
    
    return dp[0]

#print(solucionar('1220125'))    


def testCode():
    casosPrueba = [
        '1220125',
        '11106',
        '12',
        '226',
        '0',
        '06',
        '1220125',
        '121'
    ]

    salidas = [
        6,2, 2, 3, 0, 0, 6,3
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
