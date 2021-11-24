def solucionar(s:str):
    auxString = ''
    for i in s:
        if i.isalnum():
            if i.isupper():
                auxString+=i.lower()
                continue
            auxString+=i
    print(auxString)
    for k in range(int(len(auxString)/2)):
        if auxString[k] != auxString[-1*k-1]:
            return False
    return True

print(solucionar("A man, a plan, a canal: Panama"))