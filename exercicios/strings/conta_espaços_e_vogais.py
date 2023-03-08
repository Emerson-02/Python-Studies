a = input("Digite uma frase: ").lower()

vogal = 0
espaco = 0

for x in a:
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        vogal += 1
    elif x == ' ':
        espaco += 1

print("Vogais: {}" .format(vogal))
print("Espacos: {}" .format(espaco))
