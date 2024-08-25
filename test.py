import pygame

# Inicializa o Pygame
pygame.init()

# Configurações da tela
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jogo da Memória com Sombra no Texto")

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
cinza = (50, 50, 50)

# Fonte
fonte = pygame.font.Font(None, 74)  # Você pode usar uma fonte específica aqui

# Texto com sombra
texto = "Memória dos Estados"
texto_superficie = fonte.render(texto, True, branco)
sombra_superficie = fonte.render(texto, True, cinza)

# Posição do texto
posicao_texto = (100, 50)
deslocamento_sombra = (3, 3)  # Deslocamento da sombra

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Preenche a tela com uma cor de fundo
    screen.fill(preto)

    # Desenha a sombra
    screen.blit(sombra_superficie, (posicao_texto[0] + deslocamento_sombra[0], 
                                    posicao_texto[1] + deslocamento_sombra[1]))
    
    # Desenha o texto principal
    screen.blit(texto_superficie, posicao_texto)

    # Atualiza a tela
    pygame.display.flip()

# Finaliza o Pygame
pygame.quit()
