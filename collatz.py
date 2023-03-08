a = int(input('Digite um número: '))

while a != 1:
    if a % 2 == 0:
        a //= 2
    elif a % 2 == 1:
        a = 3 * a + 1
    print(a)
