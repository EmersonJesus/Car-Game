import pygame
from pygame.locals import *
import random

pygame.init()

# Criando a Janela ------------------------------------
largura = 500
altura = 500
tela_tamanho = (largura, altura)
tela_jogo = pygame.display.set_mode(tela_tamanho)
pygame.display.set_caption('Car Game')

# Cores ------------------------------------------------
cinza = (100, 100, 100)
verde = (76, 208, 56)
vermelho = (200, 0, 0)
preto = (0, 0, 0)
branco = (255, 255, 255)
amarelo = (255, 232, 0)

# Configurações do Jogo --------------------------------
fim_de_jogo = False
velocidade = 0
pontos = 0

# Loop do Jogo -----------------------------------------
relogio = pygame.time.Clock()
fps = 120
rodando = True
while rodando:
    relogio.tick(fps)
    
    for evento in pygame.event.get():
        if evento.type == QUIT:
            rodando = False
            
    pygame.display.update()

oygame.quit()