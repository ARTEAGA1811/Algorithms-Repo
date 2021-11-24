def solucionar():
    #para mantener todos los bits con sus 0's a la izq, se utiliza en formato de 32 bits
    #ejemplo:
    x = 9
    aux = str(f'{x:032b}')
    print(aux)  
    #output: 00000000000000000000000000001001
    

solucionar()