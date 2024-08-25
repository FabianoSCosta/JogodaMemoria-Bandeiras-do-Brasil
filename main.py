import random
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

fundo = pygame.image.load("imagens/fundo.jpg")
running = True
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

colunas=5
linhas=5
espaçamento=27
largura_carta=130
altura_carta=86.531

carta_aberta = 0
tentativas = 0
cartas_abertas = []

class Cartas(pygame.sprite.Sprite):
    def __init__(self,image_path):
        super(Cartas, self).__init__()
        self.imagem=image_path
        self.surf = pygame.Surface((largura_carta, altura_carta))
        self.surf = pygame.image.load("imagens/fundocarta2.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.smoothscale(self.surf, (largura_carta, altura_carta))
        self.rect = self.surf.get_rect()
        self.aberta = False
        

    def posicao(self,posicao):
        self.rect.topleft = posicao 

    def update(self, event_list):
        global carta_aberta
        global cartas_abertas
        global tentativas
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    cartas_abertas.append(self)
                    self.aberta = True
                    carta_aberta=carta_aberta+1
                    self.surf = pygame.image.load(self.imagem).convert()
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)
                    self.surf = pygame.transform.smoothscale(self.surf, (largura_carta, altura_carta))
                    tentativas = tentativas + 1

    def fechar(self):
        self.surf = pygame.image.load("imagens/fundocarta2.png").convert_alpha()
        self.surf = pygame.transform.smoothscale(self.surf, (largura_carta, altura_carta))
        self.aberta = False

def verificar_cartas_iguais(carta1, carta2):
    return carta1.imagem == carta2.imagem

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

imagens= []

# Obtém o caminho da pasta no mesmo diretório do script
pasta = Path.cwd() / r"imagens/bandeiras"
for caminho_arquivo in pasta.iterdir():
    if caminho_arquivo.is_file():
        imagens.append(caminho_arquivo.resolve())

imagens_selecionadas= random.sample(imagens, 10)


cartas_instant=[]
for path in imagens_selecionadas:
    cartas_instant.append(Cartas(path))
    cartas_instant.append(Cartas(path))
cartas_instant = random.sample(cartas_instant,20)


cartas = []

for i in range(linhas):
    for j in range(colunas):
        if not cartas_instant:
            break
        carta_selec = cartas_instant.pop()
        x = j * (largura_carta + espaçamento) + espaçamento
        y = i * (altura_carta + espaçamento) + espaçamento + 40
        carta_selec.posicao((x,y))
        cartas.append(carta_selec)
        

all_sprites.add(cartas)

font = pygame.font.Font(None, 34)
font_rodape = pygame.font.Font(None, 25)

while running:
    clock.tick(4)
    event_list=pygame.event.get()
    for event in event_list:
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    
        mouse_pos = pygame.mouse.get_pos()        

    rect = fundo.get_rect()
    rect.center = 200, 150
    screen.blit(fundo, rect)
    for entity in all_sprites:
        entity.update(event_list)
        screen.blit(entity.surf, entity.rect)
    
    if carta_aberta == 2:
        if verificar_cartas_iguais(cartas_abertas[0],cartas_abertas[1]) and cartas_abertas[0] != cartas_abertas[1]:
            print("Cartas Iguais!")
        else:
            cartas_abertas[0].fechar()
            cartas_abertas[1].fechar()
        cartas_abertas=[]
        carta_aberta= 0


    img = font_rodape.render('TENTATIVAS:'+str(tentativas), True,
                  pygame.Color(0, 0, 0))  
    
    nome = font.render('JOGO DA MEMÓRIA', True,
                  pygame.Color(0, 0, 0))  
    screen.blit(img, (40,550))
    screen.blit(nome, (287,20))

    pygame.display.flip()