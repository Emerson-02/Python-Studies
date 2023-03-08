def calcula_top_ocorrencias_de_queries(texto,queries,k):
    #print("--------------")
    #print(queries)
    ini = 0
    fim = 1
    lista = []
    txt = texto.lower()
    #print(txt[ini:fim])
    #print(len(txt))

    tamanho_texto = len(txt)
    i=0
    while(i != tamanho_texto):
        for a in txt:
            #print(txt[ini:fim])
            for x in queries:
                if txt[ini:fim] == x:
                    lista.append(txt[ini:fim])
            fim+=1
            if fim == tamanho_texto+1:
                break
        ini+=1
        fim = ini + 1
        i+=1
    #print('lista = ',lista)


    #Tirar repetidos da lista: 
    element_list = []
    for y in lista:
        if y not in element_list:
            element_list.append(y)
    #print("element_list = ", element_list)

    lista_final = []
    count = 0
    count2 = 0

    lista_repetidos = []

    for z in element_list:
        for j in lista:
            if z == j:
                count +=1
        lista_repetidos.append(count)
        count2 = count
        count = 0
        #print(lista_repetidos)

    #lista_repetidos_dec = []

    for c in range(len(lista_repetidos)):
        for h in range(len(lista_repetidos)):
            if lista_repetidos[c] <= lista_repetidos[h]:
                temp = lista_repetidos[c]
                temp2 = element_list[c]
                lista_repetidos[c] = lista_repetidos[h]
                element_list[c] = element_list[h]
                lista_repetidos[h] = temp
                element_list[h] = temp2
    
    lista_repetidos.reverse()
    element_list.reverse()
    #print(element_list)
    #print(lista_repetidos)
    #print(lista_repetidos_dec)
    #print(lista_final)

    return element_list[0:k]

            

    

#calcula_top_ocorrencias_de_queries("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua", ["a","em","i","el"], 5)

print(calcula_top_ocorrencias_de_queries("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua", ["a","em","i","el"], 4))

print(calcula_top_ocorrencias_de_queries("Emerson do Nascimento Rodrigues", ["a","em","i","el"], 5))
#calcula_top_ocorrencias_de_queries("Emerson do Nascimento Rodrigues", ["a","em","i","el"], 2)