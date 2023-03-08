'''
Você e seu time estão desenvolvendo um sistema de indicações de postos de gasolina que ficam próximos da localização atual do veículo. No modo de direção “viagem”, a funcionalidade a ser desenvolvida é de indicar ao condutor o posto mais distante possível dentro do limite atual de combustível. E caso não exista posto de gasolina, retornar -1

A pessoa responsável por fazer a especificação do sistema informou que você terá as seguintes informações: consumo médio de combustível, quantidade de combustível restante no veículo e um array contendo distâncias dos postos de gasolinas.

Exemplo:
Combustivel (em litros): 2
Consumo médio (km/l): 8
Postos de Gasolina (km): [2, 15, 22, 10.2]
'''

def ultima_parada(combustivel,consumo,postos_de_gasolina):
    distancia = combustivel * consumo
    postos_de_gasolina.sort()
    num_postos = len(postos_de_gasolina)
    postos_perto = []
    for i in reversed(range(num_postos)):
        if postos_de_gasolina[i] <= distancia:
            postos_perto.append(postos_de_gasolina[i])
    postos_perto.sort()
    if len(postos_perto) == 0:
        return -1
    else:
        return postos_perto[-1]



print(ultima_parada(2, 8, [2, 8, 17, 1, 15, 34]))
print(ultima_parada(3, 1, [2, 3, 17, 1, 15, 34]))
print(ultima_parada(3, 1, [9, 22, 17, 45, 15, 34]))