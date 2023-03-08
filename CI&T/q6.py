'''
Dizemos que um número natural X esconde o Y quando, ao apagar alguns algarismos de X, o número Y aparece. Por exemplo, o número 12345 esconde o número 235, uma vez que pode ser obtido ao apagar os números 1 e 4. Por outro lado, ele não esconde o número 154.

A imagem demonstra números: 1,2,3,4,5 todos estão em azul, mas o número 1 e 4 estão com um risco vermelho.

Escreva um código que recebe dois números e que retorna um booleano dizendo se o primeiro esconde o segundo.
'''


def checa_numero_escondido(numero,numero_oculto):
    num = []
    num[:0] = str(numero)
    #print(num)
    #print(type(num))

    num_ocult = []
    num_ocult[:0] = str(numero_oculto)
    #print(num_ocult)

    #print(num_ocult)
    #print(num)

    index_ant = 0
    a = []
    b = False

    for i in range(len(num_ocult)):
        #print('i = ', i, ' index = ', num_ocult.index(i))
        for j in range(len(num)):
            #print('j = ', j, ' index = ', num.index(i))
            if num_ocult[i] == num[j]:
                if len(a) == 0:
                    a.append(num_ocult[i])
                    index_ant = j
                elif index_ant < j:
                    a.append(num[j])
                
                
                    
                
            if a == num_ocult:
                b = True
                break
                
                #print(num.index(j))
    #print(a)
   
    
    return b
                




print(checa_numero_escondido(12345, 125))
print(checa_numero_escondido(123455, 125))
print(checa_numero_escondido(55555, 555))
print(checa_numero_escondido(12345, 531))
print(checa_numero_escondido(54321, 125))
print(checa_numero_escondido(54321, 5316))
print(checa_numero_escondido(54321, 54321))

#num = '12345'
#print(num[2::2])
#print(num[1::3])

