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
x = int(largura/2)
y = int(altura/2)

x_azul = randint(40, 600)
y_azul = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)

tela = pygame.display.set_mode((largura, altura)) # Tamanho da tela do jogo
pygame.display.set_caption('Jogão')
relogio = pygame.time.Clock()

while True: # Loop Principal
    relogio.tick(30)
    tela.fill((0, 0, 0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, False, (0, 255, 0))
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
        if x>0:
            x = x - 20
    if pygame.key.get_pressed()[K_d]:
        if x < (largura - 40):
            x = x + 20
    if pygame.key.get_pressed()[K_w]:
        if y > 0:    
            y = y - 20
    if pygame.key.get_pressed()[K_s]:
        if y < (altura - 50):    
            y = y + 20
    #
    if pygame.key.get_pressed()[K_LEFT]:
        if x>0:
            x = x - 20
    if pygame.key.get_pressed()[K_RIGHT]:
        if x < (largura - 40):
            x = x + 20
    if pygame.key.get_pressed()[K_UP]:
        if y > 0:    
            y = y - 20
    if pygame.key.get_pressed()[K_DOWN]:
        if y < (altura - 50):    
            y = y + 20


    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50)) # desenha retangulo
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 40, 50))
    #pygame.draw.circle(tela, (0, 0, 255), (300, 260), 40) # circulo
    #pygame.draw.line(tela, (255, 255, 0), (120, 0), (240, 120), 5)
    
    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos += 1
        som_colisao.play()

    tela.blit(texto_formatado, (430, 40))
    pygame.display.update() # a cada interação, atualiza o jogo