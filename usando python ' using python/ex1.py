# Numeros divisiveis por 7 mas não multiplos de 5

numbers = []

for i in range(2000, 32001):
    if (i % 7 == 0) and (i % 5 != 0):
        numbers.append(str(i))

print(', '.join(numbers))

'''
for i in range(2000, 3200):
    if i % 7 == 0 and i % 5 != 0:
        print(f'{i}', end=',')
'''