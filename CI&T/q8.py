'''
Um grande amigo seu mora numa cidade pequena, onde existem apenas duas empresas de táxi - a Empresa 1 e a Empresa 2. Ambas mudam suas taxas a cada dia e calculam o valor de suas corridas da seguinte forma: uma taxa fixa mais um valor por quilômetro rodado.
Seu amigo é fisioterapeuta e pega táxis diariamente para visitar seus clientes ao redor da cidade. Você decidiu escrever um código para ajudá-lo a decidir qual empresa escolher para cada uma das corridas, baseado no preço.

Sua função receberá 4 valores: TF1 (a taxa fixa da empresa 1), VQR1 (o valor por quilômetro rodado da empresa 1), TF2 (a taxa fixa da empresa 2), VQR2 (o valor por quilômetro rodado da empresa 2), todos em formato string. Seu retorno deve ser uma string em uma das seguintes formas:

“Tanto faz” - para o caso de o valor das duas empresas para qualquer corrida ser igual
“Empresa 1” - se o valor da Empresa 1 for sempre menor que o da Empresa 2
“Empresa 2” - para o caso contrário do citado acima
“Empresa Xpto quando a distância < N, Tanto faz quando a distância = N, Empresa Ypto quando a distância > N” para o caso de a escolha depender da distância a ser percorrida (onde Xpto e Ypto representa 1 ou 2 e N representa a distância).
Exemplo:
TF1 = 2,50
VQR1 = 1,00
TF2 = 5,00
VQR2 = 0,75
Output:
“Empresa 1 quando a distância < 10.0, Tanto faz quando a distância = 10.0, Empresa 2 quando a distância > 10.0”
'''

def escolhe_taxi(tf1,vqr1,tf2,vqr2):
    taxaf_1 = float(tf1.replace(",", '.'))
    val_km_1 = float(vqr1.replace(",", '.'))
    taxaf_2 = float(tf2.replace(",", '.'))
    val_km_2 = float(vqr2.replace(",", '.'))

    #print(taxaf_1)
    #print(val_km_1)
    #print(taxaf_2)
    #print(val_km_2)

    empresa1_menor = 0
    empresa2_menor = 0
    igual = 0
    a = ''
    empresa1_menor_list = []
    empresa2_menor_list = []
    igual_list = []


    for i in range(1, 100):
        empresa1 = taxaf_1 + (i * val_km_1)
        empresa2 = taxaf_2 + (i * val_km_2)
        #print('empresa 1: taxa fixa = {}, valor/km = {}, km = {}, valor total = {}'.format(taxaf_1,val_km_1, i, empresa1))
        #print('empresa 2: taxa fixa = {}, valor/km = {}, km = {}, valor total = {}'.format(taxaf_2,val_km_2, i, empresa2))
        if empresa1 < empresa2:
            empresa1_menor = i
            empresa1_menor_list.append(i)
        elif empresa2 < empresa1:
            empresa2_menor = i
            empresa2_menor_list.append(i)
        elif empresa1 == empresa2:
            igual = i
            igual_list.append(i)


    print(empresa1_menor_list)
    print(empresa2_menor_list)
    print(igual_list)

    a = ''

    if empresa1_menor == 0 and empresa2_menor == 0 and igual != 0:
        a = "Tanto faz"
    elif empresa1_menor != 0 and empresa2_menor == 0 and igual == 0:
        a = "Empresa 1"
    elif empresa1_menor == 0 and empresa2_menor != 0 and igual == 0:
        a = "Empresa 2"
    elif empresa1_menor > empresa2_menor and igual != 0:
        a = 'Empresa 2 quando a distância < {}, Tanto faz quando a distância = {}, Empresa 1 quando a distância > {}'.format(float(igual), float(igual), float(igual))
    elif empresa1_menor > empresa2_menor and igual == 0:
        a = 'Empresa 2 quando a distância < {}, Tanto faz quando a distância = {}, Empresa 1 quando a distância > {}'.format(float(empresa2_menor+1), float(empresa2_menor+1), float(empresa2_menor+1))
    elif empresa1_menor < empresa2_menor and igual != 0:
        a = 'Empresa 1 quando a distância < {}, Tanto faz quando a distância = {}, Empresa 2 quando a distância > {}'.format(float(igual), float(igual), float(igual))
    elif empresa1_menor < empresa2_menor and igual == 0:
        a = 'Empresa 1 quando a distância < {}, Tanto faz quando a distância = {}, Empresa 2 quando a distância > {}'.format(float(empresa1_menor+1), float(empresa1_menor+1), float(empresa1_menor+1))

    return a
    
    


'''
    if empresa1_menor != 0 and empresa2_menor == 0 and igual == 0:
        a = "Empresa 1"
    elif empresa1_menor == 0 and empresa2_menor != 0 and igual == 0:
        a = "Empresa 2"
    elif empresa1_menor == 0 and empresa2_menor == 0 and igual != 0:
        a = "Tanto faz"
    elif empresa1_menor > empresa2_menor:
        a = 'Empresa 2 quando a distância < {}, Tanto faz quando a distância = {}, Empresa 1 quando a distância > {}'.format(float(math.ceil(empresa2_menor+1)), float(math.ceil(empresa2_menor+1)), float(math.ceil(empresa2_menor+1)))
    elif empresa1_menor < empresa2_menor:
        a = 'Empresa 1 quando a distância < {}, Tanto faz quando a distância = {}, Empresa 2 quando a distância > {}'.format(float(math.ceil(empresa1_menor+1)), float(math.ceil(empresa1_menor+1)), float(math.ceil(empresa1_menor+1)))
'''



    #return a

    

print(escolhe_taxi('2,50','1,00','5,00','0,75'))

#(escolhe_taxi('2,50','1,00','5,00','0,85'))
#print(escolhe_taxi('2,50','1,00','2,50','1,00'))
#print(escolhe_taxi('2,50','1,00','5,50','1,00'))
#print(escolhe_taxi('2,50','1,00','2,50','1,74'))
#print(escolhe_taxi('5,50','1,00','2,50','1,00'))