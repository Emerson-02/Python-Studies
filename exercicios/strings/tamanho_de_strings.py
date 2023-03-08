a = input("String 1: ")
b = input("String 2: ")

print("Tamanho de {}: {} caracteres" .format(a, len(a)))
print("Tamanho de {}: {} caracteres" .format(b, len(b)))

if len(a) == len(b):
    print("As duas strings são do mesmo tamanho")
else:
    print("As duas strings são de tamanhos diferentes.")

if a == b:
    print("As duas strings possuemo mesmo conteúdo")
else:
    print("As duas strings possuem conteúdo diferente.")

        