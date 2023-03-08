def menor_string_maior(name):
    a = []
    b = []
    a[:0]= name.lower()
    a.sort()
    b[:0] = name.lower()
    print(b)
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z']



print(menor_string_maior('ab'))
print(menor_string_maior('abcde'))
print(menor_string_maior('ba'))
print(menor_string_maior('nextgen'))
print(menor_string_maior('Qualified'))