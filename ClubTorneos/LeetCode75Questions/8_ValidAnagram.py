#https://leetcode.com/problems/valid-anagram/
def solucionar(s:str, t:str):
    #aqui voy eliminando las coincidencias en t.
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] in t:
            indFound = t.find(s[i])
            t = t[:indFound]+t[indFound+1:]
        else:
            return False
    return True


def optimizedFunction(s:str, t:str):
    #si los strings son de diferente longitud, no pueden ser anagramas
    if len(s) != len(t):
        return False
    #creo un diccionario con las letras de s
    dic = {}
    for i in range(len(s)):
        if s[i] in dic:
            dic[s[i]] += 1
        else:
            dic[s[i]] = 1

    #recorro t y voy restando las letras de dic
    #en caso que no exista esa letra en dic, retorno False
    for i in range(len(t)):
        if t[i] in dic:
            dic[t[i]] -= 1
        else:
            return False
    #si todas las letras de dic son 0, retorno True
    for i in dic:
        if dic[i] != 0:
            return False
    return True

print(solucionar("anagram", "nagaram"))
print(solucionar("rat", "car"))