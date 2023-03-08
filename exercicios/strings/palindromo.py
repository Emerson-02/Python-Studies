a = input("Digite algo: ").lower()

print(a[::-1])

for x in a:
    a = a.replace(" ", "")

if a == a[::-1]:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")