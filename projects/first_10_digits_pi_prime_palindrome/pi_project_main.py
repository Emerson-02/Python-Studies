

arquivo = open('./projects/first_10_digits_pi_prime_palindrome/pi1b.txt', 'r') 

print(arquivo.readable())
#
#lista = arquivo.read()

i = 0
'''
for x in arquivo:
    print(x)                          #consertar
    if x == ".":
        continue
'''

#print(lista[0])
#

#print(arquivo.read())





'''
# Verifica se um numero eh primo
num = 0
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
'''

divisores = []

def prime(nmr):
    for i in range(1, nmr+1):
        if (nmr % i) == 0:
            divisores.append(i)
        else:
            pass
    if len(divisores) == 2:
        print("é primo!")
        return True
    else:
        #print("não é primo!")
        return False
    divisores.clear()

#prime(7)
#print(divisores)


#Verifica se um numero é palindromo
'''
a = input("Digite algo: ").lower()

print(a[::-1])

for x in a:
    a = a.replace(" ", "")

if a == a[::-1]:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")
'''

def palindrome(nmr):
    if nmr == nmr[::-1]:
        #print(nmr)
        return True
    else:
        return False
    

#palindrome("aab")

# Separa 9 digitos de uma string
numT = "111122223333"  # numero para teste
num = arquivo.read()
print(num[0])
str = ""

#print(num[1])
#print(pivo)

a = 0
x1 = 0
x2 = 10
#str = str + num[a]

for a in range(10):
    i = 0   
    for i in range(x1, x2):
        if num[i] != ".":
            pivo = num[i]
            str = str + pivo
            
    print(str)
    str = ""
    x1+=1
    x2+=1
    

#print(str)


arquivo.close