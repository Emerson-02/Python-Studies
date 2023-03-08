# way 1

fat = int(input("Digite um numero: "))
tot = 0
while fat >= 1:
    if tot == 0:
        tot = fat
        fat-=1
        continue
    tot *= fat
    fat -= 1

print(tot)

# way 2

def fatorial(x):
    if x == 0:
        return 1 
    return x * fatorial(x - 1)
    
x = int(input("Digite um numero: "))
print(fatorial(x))