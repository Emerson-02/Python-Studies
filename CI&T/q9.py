'''
Ao se comparar se uma string é maior que outra, considera-se a ordem alfabética ou lexicográfica. No caso, “abcd” < “adbc” < “bacd”.

Escreva uma função que receba uma string A e retorne uma string B, sendo que B é composta pelos mesmos caracteres que A reordenados.

B deve obedecer às seguintes condições:

Ser maior que A
Ser a menor string possível que cumpra as condições acima
Caso não seja possível encontrar uma string que cumpra as condições, retorne a string “sem reposta”.
Por exemplo:

A = “ab”
Logo, o resultado será “ba”

A = “abcde”
Logo, o resultado será “abced”

A = “ba”
Nesse caso, o resultado será “sem resposta"
'''

def menor_string_maior(name):
    a = []
    b = []
    a[:0]= name
    a.sort()
    #print(a)
    b[:0] = name
    #b.sort()
    #print(b)
   # print(len(a))
   # print(a[len(a)-1])

    if len(b) >= 2:
        b[len(b)-1], b[len(b)-2] = b[len(b)-2], b[len(b)-1]

    #print(b)

    if b == a and len(b) > 2:
        b[len(b)-2], b[len(b)-3] = b[len(b)-3], b[len(b)-2]
    
    
    resp = ''

    if b == a:
        #print("Sem resposta")
        resp = "sem resposta"
    else:
        #print(b)
        for i in b:
            resp += i

    return resp

print(menor_string_maior('ab'))
print(menor_string_maior('abcde'))
print(menor_string_maior('ba'))
print(menor_string_maior('nextgen'))
print(menor_string_maior('Qualified'))
