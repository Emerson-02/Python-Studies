import random
import os

erros=0
sorteado=random.randrange(0, 100)
jogador=int(input("Digite seu número: "))

while(sorteado!=jogador):
    os.system('cls')
    if(sorteado > jogador):
        print("ERRO, numero e maior")
    elif sorteado < jogador:
        print("ERRO, numero e menor")
    erros+=1
    jogador=int(input("Digite seu número: "))

print("Numero {}, voce acertou em {} tentativas" .format(str(jogador), str(erros+1)))

