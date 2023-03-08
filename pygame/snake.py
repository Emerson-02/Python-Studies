import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
pygame.mixer.init()

pygame.mixer.music.set_volume(0.05)
musica_fundo = pygame.mixer.music.load('BoxCat_Games_-_CPU_Talk.mp3')
# Só a música de fundo pode ser .mp3
pygame.mixer.music.play(-1)

som_colisao = pygame.mixer.Sound('smw_coin.wav')
som_colisao.set_volume(0.1)


largura = 640
altura = 480
x_cobra = int(largura/2)
y_cobra = int(altura/2)

x_maca = randint(40, 600)
y_maca = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)

tela = pygame.display.set_mode((largura, altura)) # Tamanho da tela do jogo
pygame.display.set_caption('Jogão')
relogio = pygame.time.Clock()
lista_cobra = []
comprimento_inicial = 5


def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        #XeY = [x, y]
        #XeY[0] = x
        #XeY[1] = y
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))

while True: # Loop Principal
    relogio.tick(30)
    tela.fill((255, 255, 255))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        """"
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20 """
    if pygame.key.get_pressed()[K_a]:
        if x_cobra>0:
            x_cobra = x_cobra - 20
    if pygame.key.get_pressed()[K_d]:
        if x_cobra < (largura - 40):
            x_cobra = x_cobra + 20
    if pygame.key.get_pressed()[K_w]:
        if y_cobra > 0:    
            y_cobra = y_cobra - 20
    if pygame.key.get_pressed()[K_s]:
        if y_cobra < (altura - 50):    
            y_cobra = y_cobra + 20
    #
    if pygame.key.get_pressed()[K_LEFT]:
        if x_cobra>0:
            x_cobra = x_cobra - 20
    if pygame.key.get_pressed()[K_RIGHT]:
        if x_cobra < (largura - 40):
            x_cobra = x_cobra + 20
    if pygame.key.get_pressed()[K_UP]:
        if y_cobra > 0:    
            y_cobra = y_cobra - 20
    if pygame.key.get_pressed()[K_DOWN]:
        if y_cobra < (altura - 50):    
            y_cobra = y_cobra + 20


    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20)) # desenha retangulo
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))
    #pygame.draw.circle(tela, (0, 0, 255), (300, 260), 40) # circulo
    #pygame.draw.line(tela, (255, 255, 0), (120, 0), (240, 120), 5)
    
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        som_colisao.play()

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    
    lista_cobra.append(lista_cabeca)

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado, (430, 40))
    pygame.display.update() # a cada interação, atualiza o jogo