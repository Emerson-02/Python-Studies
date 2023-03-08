'''
Sua equipe está trabalhando em um app de streaming de músicas e uma das funcionalidades é criar um embaralhador de músicas. Uma pesquisa feita pela equipe de UX (experiência do usuário) mostrou que essa é uma das funcionalidades mais importantes para os usuários e por isso foi priorizada a criação de um experimento para testar a melhor solução.

A ideia é criar vários embaralhadores diferentes e realizar um teste com partes dos usuários (chamado de teste A/B), onde cada grupo de usuários selecionado recebe uma versão e através de pesquisas e métricas de utilização saberemos qual terá a maior aceitação.

Sua tarefa será desenvolver um desses embaralhadores. Você deve criar uma função que receberá uma lista de pesos que representa as músicas mais ouvidas pelo usuário. Sua função deve retornar uma lista organizada intercalando as músicas mais ouvidas com as músicas menos ouvidas. Por exemplo:

Na situação onde a lista de pesos é: [2, 10, 5, 3] sua função deverá retornar [10, 2, 5, 3]
'''
import math

def shuffle_musicas(musicas_tocadas):
    musics = []
    musics = musicas_tocadas
    musics.sort()
    #print(musics)
    mixed = []
    tam = len(musics)
    #print(tam/2)
    #print(musics[len(musics)-1])
    for i in range(1, int(tam/2)+1):
        #print(i)
        mixed.append(musics[len(musics)-i])
        mixed.append(musics[i-1])
    
    

    if tam%2 == 1:
        aux = musics[math.ceil(tam/2)-1] 
        #print(aux)
        mixed.append(aux)
    
    #print(mixed)

    return mixed


print(shuffle_musicas([2, 10, 5, 3]))
print(shuffle_musicas([2, 10, 5, 3, 7]))
print(shuffle_musicas([2, 10, 5, 3, 7, 1, 6, 8]))