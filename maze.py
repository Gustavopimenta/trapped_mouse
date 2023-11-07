import pygame
import sys

# Configurações iniciais do Pygame e janela
pygame.init()
largura, altura = 800, 600
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Labirinto")

# Defina as cores
cor_parede = (0, 0, 0)
cor_caminho = (255, 255, 255)

# Defina a matriz do labirinto e as dimensões das células
labirinto = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
]

largura_celula = largura // len(labirinto[0])
altura_celula = altura // len(labirinto)

def desenhar_labirinto():
    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[0])):
            if labirinto[linha][coluna] == 1:
                pygame.draw.rect(janela, cor_parede, (coluna * largura_celula, linha * altura_celula, largura_celula, altura_celula))
            else:
                pygame.draw.rect(janela, cor_caminho, (coluna * largura_celula, linha * altura_celula, largura_celula, altura_celula))

cor_de_fundo = (255, 255, 255)

# Loop principal do Pygame
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    janela.fill(cor_de_fundo)
    desenhar_labirinto()
    pygame.display.update()
