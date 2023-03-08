'''
Durante uma expedição tecnológica, sua equipe encontrou o que parece ser a senha que lhes dá acesso a um grande tesouro digital. Por sorte, sua equipe é formada pelas pessoas mais feras em programação e vocês rapidamente descobriram como decifrá-la.

Com a possibilidade de que vocês encontrem mais códigos contendo outras senhas, você foi designado à tarefa de desenvolver um algoritmo que decifra os códigos para não precisarem fazer isso de forma manual.

A senha é representada por um número binário de 10 dígitos formado pelo dígito predominante de cada coluna. Caso a coluna tenha a mesma quantidade de dígitos 0 e 1, deve se considerar o número 1.

Exemplo: A primeira coluna da lista tem como dígito predominante o número 1, sendo assim, o primeiro dígito - dos 10 - da senha é 1.

0110100000
1001011111
1110001010
0111010101
0011100110
1010011001
1101100100
1011010100
1001100111
1000011000

Desenvolva um algoritmo que receba um array de valores binários (como o exemplo acima) e retorne a representação decimal da senha.
'''

def calcula_numero_da_senha(senha):
    # Numero de arrays: 10
    # Numero predominante em cada coluna
    dig_um = []
    dig_dois = []
    dig_tres = []
    dig_quatro = []
    dig_cinco = []
    dig_seis = []
    dig_sete = []
    dig_oito= []
    dig_nove = []
    dig_dez = []
    zero = []
    um = []
    binary_list = []

    for i in senha:
        dig_um.append(int(i[0]))
        dig_dois.append(int(i[1]))
        dig_tres.append(int(i[2]))
        dig_quatro.append(int(i[3]))
        dig_cinco.append(int(i[4]))
        dig_seis.append(int(i[5]))
        dig_sete.append(int(i[6]))
        dig_oito.append(int(i[7]))
        dig_nove.append(int(i[8]))
        dig_dez.append(int(i[9]))

    def repeat(lista):
        for i in lista:
            if i == 1:
                um.append(1)
            elif i == 0:
                zero.append(0)
        if len(um) >= len(zero):
            binary_list.append(1)
        else:
            binary_list.append(0)
        um.clear()
        zero.clear()

    repeat(dig_um)
    repeat(dig_dois)
    repeat(dig_tres)
    repeat(dig_quatro)
    repeat(dig_cinco)
    repeat(dig_seis)
    repeat(dig_sete)
    repeat(dig_oito)
    repeat(dig_nove)
    repeat(dig_dez)


    binary_num = ''
    for i in binary_list:
        binary_num = binary_num + str(i)

    # bin to dec
    n = len(binary_num)
    binary_copy = int(binary_num)
    dec = 0
    i = 0

    while n >= 0:
        resto = binary_copy % 10
        dec = dec + resto * 2**i
        n = n-1
        i = i+1
        binary_copy = binary_copy // 10
    return dec






    




print(calcula_numero_da_senha(["1111111111","1111111111","1111111111","1111111111","0111111111","0111111111","0111111111","0111111111","0111111111","0111111111"]))

print(calcula_numero_da_senha(["1111111111","0000000001","0111011101","0001001111","1010101010","0101010100","0000010000","0110111110","1010110110","0011001100"]))

print(calcula_numero_da_senha([[1,1,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,1],[0,1,1,1,0,1,1,1,0,1],[0,0,0,1,0,0,1,1,1,1],[1,0,1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1,0,0],[0,0,0,0,0,1,0,0,0,0],[0,1,1,0,1,1,1,1,1,0],[1,0,1,0,1,1,0,1,1,0],[0,0,1,1,0,0,1,1,0,0]]))

print(calcula_numero_da_senha([[0,1,1,0,1,0,0,0,0,0],[1,0,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,1,0,1,0],[0,1,1,1,0,1,0,1,0,1],[0,0,1,1,1,0,0,1,1,0],[1,0,1,0,0,1,1,0,0,1],[1,1,0,1,1,0,0,1,0,0],[1,0,1,1,0,1,0,1,0,0],[1,0,0,1,1,0,0,1,1,1],[1,0,0,0,0,1,1,0,0,0]]))



# Pegar o elemento i de cada lista