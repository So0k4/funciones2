def cuenta_regresiva(num):
    resultado = []
    for i in range(num,-1, -1):
        resultado.append(i)
    return resultado

print(cuenta_regresiva(5))

def lista_numeros(lista):
    print(lista[0])
    return lista[1]

valor_back = lista_numeros([10, 20])

def longitud(lista):
    suma = lista[0] + len(lista)
    return suma

print(longitud([10,20,21,40]))

def lista_original(lista):
    if len(lista) < 2:
        return False
    
    nueva_lista =[]
    for i in lista:
        if i > lista[1]:
            nueva_lista.append(i)
    print(f"Son{len(nueva_lista)} valores mayores al segundo que es {lista[1]}")
    return nueva_lista
print(lista_original([5,2,3,2,1,4]))
print(lista_original([5]))

def tam_y_longa(lista):
    lista_nueva = []
    for i in range(0, lista[0], 1):
        lista_nueva.append(lista[1])
    return lista_nueva
    
print(tam_y_longa([4,7]))
    