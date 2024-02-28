import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura_tela = 1800
altura_tela = 900
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# Inicializa variáveis do bloco
x_bloco = largura_tela // 2
y_bloco = altura_tela // 2
largura_bloco = 50
altura_bloco = 50
velocidade_x = 0
velocidade_y = 0
aceleracao_x = 0
aceleracao_y = 0
movimento_acelerado = False  # Inicia sem aceleração

# Fonte para o display da velocidade
fonte = pygame.font.Font(None, 36)

# Relógio para controlar os FPS
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Verifica teclas pressionadas
    keys = pygame.key.get_pressed()

    # Reseta acelerações
    aceleracao_x, aceleracao_y = 0, 0

    if keys[pygame.K_LEFT]:
        if movimento_acelerado:
            aceleracao_x = -0.1
        else:
            velocidade_x = -5
            velocidade_y = 0  # Reseta a velocidade Y para movimento exclusivamente horizontal
    elif keys[pygame.K_RIGHT]:
        if movimento_acelerado:
            aceleracao_x = 0.1
        else:
            velocidade_x = 5
            velocidade_y = 0
    if keys[pygame.K_UP]:
        if movimento_acelerado:
            aceleracao_y = -0.1
        else:
            velocidade_y = -5
            velocidade_x = 0  # Reseta a velocidade X para movimento exclusivamente vertical
    elif keys[pygame.K_DOWN]:
        if movimento_acelerado:
            aceleracao_y = 0.1
        else:
            velocidade_y = 5
            velocidade_x = 0

    if keys[pygame.K_SPACE]:  # Pressione espaço para alternar entre movimento acelerado ou não
        movimento_acelerado = not movimento_acelerado
        # Reseta velocidades e acelerações ao alternar o modo
        velocidade_x, velocidade_y = 0, 0

    # Aplica aceleração
    velocidade_x += aceleracao_x
    velocidade_y += aceleracao_y

    # Atualiza a posição do bloco
    x_bloco += velocidade_x
    y_bloco += velocidade_y

    # Garante que o bloco não saia da tela
    x_bloco = max(0, min(x_bloco, largura_tela - largura_bloco))
    y_bloco = max(0, min(y_bloco, altura_tela - altura_bloco))

    # Limpa a tela
    tela.fill(preto)

    # Desenha o bloco
    pygame.draw.rect(tela, branco, (x_bloco, y_bloco, largura_bloco, altura_bloco))

    # Calcula a velocidade total (magnitude do vetor velocidade)
    velocidade_total = (velocidade_x**2 + velocidade_y**2)**0.5

    # Display da velocidade
    texto_velocidade = fonte.render(f"Velocidade: {velocidade_total:.2f}", True, vermelho)
    tela.blit(texto_velocidade, (10, 10))

    # Atualiza a tela
    pygame.display.flip()

    # Limita a 60 FPS
    clock.tick(60)
