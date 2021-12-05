# strs = ["eat","tea","tan","ate","nat","bat"]
# # uno = {'e','a','t'}
# # dos = {'a','t','e'}
# # dicc = {{'a','t','e'}:1}


aux = {0:{3,2}, 1:{0}, 2:{0,1}, 3:{2}}

for clave, valor in aux.items():
    for i in valor:
        if clave in aux[i]:
            print(False)
            break