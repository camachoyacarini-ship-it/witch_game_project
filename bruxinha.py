import pygame

pygame.init()

# Criar a janela
janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("The Little Witch")

# Definir cores
ROXO = (35, 20, 55)
LILAS = (170, 110, 210)
PELE = (255, 220, 190)
PRETO = (20, 15, 25)
CASTANHO = (120, 70, 35)

# Função para desenhar a bruxinha
def desenhar_bruxinha(janela, x, y):

    # Vassoura
    pygame.draw.line(janela, CASTANHO,
                     (x + 30, y + 35),
                     (x + 100, y + 65), 6)

    # Palha da vassoura
    pygame.draw.polygon(janela, LILAS, [
        (x + 95, y + 60),
        (x + 120, y + 45),
        (x + 115, y + 75)
    ])

    # Corpo (vestido)
    pygame.draw.polygon(janela, LILAS, [
        (x - 25, y + 5),
        (x + 25, y + 5),
        (x + 40, y + 65),
        (x - 40, y + 65)
    ])

    # Cabeça
    pygame.draw.circle(janela, PELE, (x, y - 20), 23)

    # Cabelo
    pygame.draw.circle(janela, PRETO, (x - 17, y - 20), 9)
    pygame.draw.circle(janela, PRETO, (x + 17, y - 20), 9)

    # Chapéu
    pygame.draw.polygon(janela, LILAS, [
        (x - 30, y - 38),
        (x + 30, y - 38),
        (x, y - 100)
    ])

    pygame.draw.ellipse(janela, PRETO,
                        (x - 35, y - 43, 70, 12))

    # Olhos
    pygame.draw.circle(janela, PRETO, (x - 8, y - 22), 3)
    pygame.draw.circle(janela, PRETO, (x + 8, y - 22), 3)

# Posição inicial da bruxinha
x = 400
y = 300

# Velocidade de movimento
velocidade = 5
executando = True

while executando:


    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Limpar o ecrã
    janela.fill(ROXO)

    # Verificar as teclas pressionadas
    teclas = pygame.key.get_pressed()

    # Movimento para a esquerda
    if teclas[pygame.K_LEFT]:
        x -= velocidade

    # Movimento para a direita
    if teclas[pygame.K_RIGHT]:
        x += velocidade

    # Movimento para cima
    if teclas[pygame.K_UP]:
        y -= velocidade

    # Movimento para baixo
    if teclas[pygame.K_DOWN]:
        y += velocidade

    # Desenhar a bruxinha
    desenhar_bruxinha(janela, x, y)

    pygame.display.update()

pygame.quit()