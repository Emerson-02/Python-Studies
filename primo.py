num = int(input('Digite um numero: '))
divisores = []

for i in range(1, num+1):
    if (num % i) == 0:
        divisores.append(i)
    else:
        pass

if len(divisores) == 2:
    print("é primo!")
else:
    print("não é primo!")

