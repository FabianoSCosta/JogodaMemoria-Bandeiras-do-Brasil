# Simple pygame program
import time

import random
# Import and initialize the pygame library
import pygame
from pathlib import Path

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

colunas=6
linhas=8
espaçamento=100
largura_carta=20
altura_carta=14.25



class Cartas(pygame.sprite.Sprite):
    def __init__(self,image_path):
        super(Cartas, self).__init__()
        self.imagem=image_path
        self.surf = pygame.image.load(image_path).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (60, 48))
        self.rect = self.surf.get_rect()

    def posicao(self,posicao):
        self.rect.center = posicao 




pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

imagens= []

# Obtém o caminho da pasta no mesmo diretório do script
pasta = Path.cwd() / r"bandeiras/imagens"
for caminho_arquivo in pasta.iterdir():
    if caminho_arquivo.is_file():
        imagens.append(caminho_arquivo.resolve())

imagens_selecionadas= random.sample(imagens, 10)


cartas_instant=[]
for path in imagens_selecionadas:
    cartas_instant.append(Cartas(path))

cartas = []

for i in range(colunas):
    for j in range(linhas):
        if not cartas_instant:
            break
        carta_selec = cartas_instant.pop()
        x = j * (largura_carta + espaçamento) + espaçamento
        y = i * (altura_carta + espaçamento) + espaçamento
        carta_selec.posicao((x,y))
        cartas.append(carta_selec)
        print(len(imagens))
        

#carta = [Cartas(r"bandeiras\imagens\DF.png")]
all_sprites = pygame.sprite.Group()
all_sprites.add(cartas)
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
            
        screen.fill((135, 206, 250))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()