import random

matriz_mae = []
a = [1,2,3,4,5,6,7,8,9]
random.shuffle(a)
print(a)



def compara_listas(lista1, lista2):
    if(lista1[0] != lista2[0] and lista1[1] != lista2[1] and lista1[2] != lista2[2] and lista1[3] != lista2[3] and lista1[4] != lista2[4] and lista1[5] != lista2[5] and lista1[6] != lista2[6] and lista1[7] != lista2[7] and lista1[8] != lista2[8]):
        return True
    else:
        #matriz_mae.append(lista2)
        return False


'''
contador = 0
for i in range(0, len(matriz_mae)-1):
    if compara_listas(matriz_mae[i], a) is False:
        pass
    else:
        contador = contador + 1
'''


def cria_sudoku(lista):
    a = []
    a = lista
    random.shuffle(a)
    matriz_mae.append(a)
    #print("mae = ", matriz_mae[0])
    i = 0
    contador = 0
    while i <= 8:
        b = a.copy()
        random.shuffle(b)
        tam = len(matriz_mae)
        print("b = ", b)
        print("tam = ", tam)
        print("i = ", i)
        #random.shuffle(a)
        print("mae = ", matriz_mae[0])
        #print("shuffled = ", a)
        #print("comp = ", compara_listas(matriz_mae[i], b))
        for i in range(0, tam):
            if compara_listas(matriz_mae[i], b) is False:
                contador = contador + 1
            else:
                pass
        print("Contador = ", contador)
        if contador == 0:
            matriz_mae.append(b)
            i = i + 1
        contador = 0


cria_sudoku(a)
print(matriz_mae)
