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
velocidade = 2
pontos = 0

# Marcadores de Tamanho --------------------------------
marcador_largura = 10
marcador_altura = 50

# Estrada e Bordas -------------------------------------
estrada = (100, 0, 300, altura)
marcador_borda_esquerda = (95, 0, marcador_largura, altura)
marcador_borda_direita = (395, 0, marcador_largura, altura)

# Coordenadas X das pistas -----------------------------
pista_esquerda = 150
pista_centro = 250
pista_direita = 350
pistas = [pista_esquerda, pista_centro, pista_direita]

# Animação de Movimento da Pista -----------------------
marcador_pista_y = 0

class Carro(pygame.sprite.Sprite):
    def __init__(self, imagem, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        # Reduzindo a imagem para caber na pista -------
        imagem_escala = 45 / imagem.get_rect().width
        nova_largura = imagem.get_rect().width * imagem_escala
        nova_altura = imagem.get_rect().height * imagem_escala
        self.image = pygame.transform.scale(imagem, (nova_largura, nova_altura))
        
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

class CarroJogador(Carro):
    def __init__(self, x, y):
        pass
    

# Loop do Jogo -----------------------------------------
relogio = pygame.time.Clock()
fps = 120
rodando = True
while rodando:
    relogio.tick(fps)
    
    for evento in pygame.event.get():
        if evento.type == QUIT:
            rodando = False
        
    # Desenhando a grama -------------------------------
    tela_jogo.fill(verde)    
    
    # Desenhando estrada -------------------------------
    pygame.draw.rect(tela_jogo, cinza, estrada)
    
    # Desenhando bordas --------------------------------
    pygame.draw.rect(tela_jogo, amarelo, marcador_borda_esquerda)
    pygame.draw.rect(tela_jogo, amarelo, marcador_borda_direita)
    
    # Desenhando Marcadores das Pistas -----------------
    marcador_pista_y += velocidade * 2
    if marcador_pista_y >= marcador_altura * 2:
        marcador_pista_y = 0
        
    for y in range(marcador_altura * -2, altura, marcador_altura * 2):
        pygame.draw.rect(tela_jogo, branco, (pista_esquerda + 45, y + marcador_pista_y, marcador_largura, marcador_altura))
        pygame.draw.rect(tela_jogo, branco, (pista_centro + 45, y + marcador_pista_y, marcador_largura, marcador_altura))
        
    
    pygame.display.update()

pygame.quit()