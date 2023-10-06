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
        imagem = pygame.image.load('imagens/Audi.png')
        super().__init__(imagem=imagem, x=x, y=y)

# Coordenadas Inicial do Jogador -----------------------
jogador_x = 250
jogador_y = 400

# Criando Carro do Jogador -----------------------------
grupo_jogador = pygame.sprite.Group()
jogador = CarroJogador(jogador_x, jogador_y)
grupo_jogador.add(jogador)

# Carregando Outros Carros -----------------------------
nomes_imagens = ['Mini_truck.png', 'Mini_van.png', 'taxi.png', 'truck.png']
imagem_carros = []
for nome in nomes_imagens:
    imagem = pygame.image.load("imagens/" + nome)
    imagem_carros.append(imagem)
    
# Grupo de Sprites para os Carros ----------------------
grupo_carros = pygame.sprite.Group()

# Loop do Jogo -----------------------------------------
relogio = pygame.time.Clock()
fps = 120
rodando = True
while rodando:
    relogio.tick(fps)
    
    for evento in pygame.event.get():
        if evento.type == QUIT:
            rodando = False
            
        # Mover o Carro do jogador usando setas direita/esquerda
        if evento.type == KEYDOWN:
            if evento.key == K_LEFT and jogador.rect.center[0] > pista_esquerda:
                jogador.rect.x -= 100
            elif evento.key == K_RIGHT and jogador.rect.center[0] < pista_direita:
                jogador.rect.x += 100
        
        
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
    
    # Desenhando o Carro do Jogador --------------------
    grupo_jogador.draw(tela_jogo)    
    
    # Adicionar no topo dois carros ----------------------
    if len(grupo_carros) < 2:
        # Garantir que tenha espaço entre os carros ------
        adiciona_carro = True
        for carro in grupo_carros:
            if carro.rect.top < carro.rect.height * 1.5:
                adiciona_carro = False
        
        if adiciona_carro:
            # Seleciona pista Aleatoria ------------------
            pista = random.choice(pistas)
            # Seleciona a imagem do carro aleatoria ------
            img = random.choice(imagem_carros)
            inimigo = Carro(img, pista, altura / -2)
            grupo_carros.add(inimigo)
            
    # Faz o movimento dos carros -------------------------
    for carro in grupo_carros:
        carro.rect.y += velocidade
        
        # Remove o carro quando sai da tela --------------
        if carro.rect.top >= altura:
            carro.kill()
            
            # Adiciona Pontuação -------------------------
            pontos += 1
            
            # Aumenta Velocidade do Jogo a cada 5 carros --
            if pontos > 0 and pontos % 5 == 0:
                velocidade += 1
        
    # Desenha os Carros do topo ---------------------------
    grupo_carros.draw(tela_jogo)
    
    # Mostrar Pontos --------------------------------------
        
            
    pygame.display.update()

pygame.quit()