import os
import random
from colorama import Fore, Back, Style

jogarNovamente = "s"
jogadas = 0
quemJoga = 2
maxJogadas = 9
vit = "n"
velha = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

def tela():
    global velha
    global jogadas
    os.system("cls")
    print("    0   1   2")
    print("0:  {} | {} | {}" .format(velha[0][0], velha[0][1], velha[0][2]))
    print("   -----------")
    print("1:  {} | {} | {}" .format(velha[1][0], velha[1][1], velha[1][2]))
    print("   -----------")
    print("2:  {} | {} | {}" .format(velha[2][0], velha[2][1], velha[2][2]))
    print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)

tela()