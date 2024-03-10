import pygame
import random
from pygame.locals import *
from random import choice

L = 800
H = 600

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (150, 170, 171)
VERMELHO = (182, 1, 41)
AMARELO = (255, 215, 45)
AMARELO_ESCURO = (173, 175, 0)
VERDE_ESCURO = (45, 109, 41)
VERDE_CLARO = (61, 202, 63)
VERMELHO_CLARO = (245, 0, 53)
AZUL = (42, 170, 210)
CORES = [AMARELO, AZUL, BRANCO, VERMELHO_CLARO, VERDE_CLARO]
CORES2 = [AMARELO, AZUL, BRANCO]
COR = choice(CORES)
COR2 = choice(CORES2)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Menu")
clock = pygame.time.Clock()

# Posição da maçã
def on_grid_random():
    x = (random.randint(0, 790))
    y = (random.randint(0, 590))
    return (x//20 * 20, y//20 * 20)

# Colisão entre a cobra e a maçã
def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def colisao(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def perdeu():
    fechar = False
    while not fechar:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    fechar = True

        screen.fill(PRETO)
        fonte = pygame.font.SysFont('comicsansms', 40)
        surface_text, rect_text = text_objects("GAME OVER", fonte, VERMELHO)
        rect_text = 200, 300
        screen.blit(surface_text, rect_text)


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jogo da Cobrinha - perera2k4")
clock = pygame.time.Clock()

# Definir botões do menu (botões que possam ser apertados
def botoes(msg, sqr, cor1, cor2, cor_text, acao = None):
    mouse = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pressed()

    if sqr[0] + sqr[2] > mouse[0] > sqr[0] and sqr[1] + sqr[3] > mouse[1] > sqr[1]:
        pygame.draw.rect(screen, cor2, sqr)
        if clique[0] == 1 and acao != None:
            acao()
    else:
        pygame.draw.rect(screen, cor1, sqr)

    fontePequena = pygame.font.SysFont('arial', 20)
    surface_text, rect_text = text_objects(msg, fontePequena, cor_text)
    rect_text.center = (sqr[0] + 60, sqr[1] + 20)
    screen.blit(surface_text, rect_text)

# Tela de créditos
def creditos():
    fechar = False
    while not fechar:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    fechar = True

        screen.fill(PRETO)
        fonte = pygame.font.SysFont('arial', 20)

        surface_text, rect_text = text_objects("- perera2k4 -", fonte, VERMELHO_CLARO)
        rect_text.center = ((L / 2), 200)
        screen.blit(surface_text, rect_text)
        
        
        voltar = fonte.render('Pressione ESC para voltar ao menu principal.', False, VERDE_ESCURO)
        screen.blit(voltar, (200, 500))
        pygame.display.update()
        clock.tick(15)


# Tela de como jogar o "Jogo da Cobrinha"
def como_jogar():
    fechar = False
    while not fechar:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    fechar = True

        screen.fill(PRETO)
        fonte = pygame.font.SysFont("arial", 20)
        surface_text, rect_text = text_objects("1- O objetivo do jogo é se tornar a maior cobra do mundo!", fonte, BRANCO)
        rect_text = (50, 50)
        screen.blit(surface_text, rect_text)
        surface_text, rect_text = text_objects("2- Coma maçãs e se torne cada vez maior!", fonte, BRANCO)
        rect_text = (50, 100)
        screen.blit(surface_text, rect_text)
        surface_text, rect_text = text_objects("3- Para se movimentar utilize W-A-S-D ou As setas de teclado.", fonte, BRANCO)
        rect_text = (50, 150)
        screen.blit(surface_text, rect_text)
        surface_text, rect_text = text_objects("4- Cada nível tem um tamanho e uma velocidade de movimentação diferentes:", fonte, BRANCO)
        rect_text = 50, 200
        screen.blit(surface_text, rect_text)
        fonte2 = pygame.font.SysFont("arial", 16)
        surface_text, rect_text = text_objects("Fácil = Velocidade em 15 FPS e tamanho 20x20", fonte2, BRANCO)
        rect_text = 70, 230
        screen.blit(surface_text, rect_text)
        surface_text, rect_text = text_objects("Médio = Velocidade em 25 FPS, Díficil = 35 FPS e tamanho 10x10", fonte2,BRANCO)
        rect_text = 70, 250
        screen.blit(surface_text, rect_text)

        voltar = fonte.render('Pressione ESC para voltar ao menu principal.', False, VERDE_ESCURO)
        screen.blit(voltar, (200, 500))
        pygame.display.update()
        clock.tick(15)

def niveis():
    fechar = False
    while not fechar:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    fechar = True

        screen.fill(PRETO)
        fonte = pygame.font.SysFont("arial", 30)
        surface_text, rect_text = text_objects("Escolha uma dificuldade", fonte, BRANCO)
        rect_text = (250, 150)
        screen.blit(surface_text, rect_text)
        botoes("Fácil", (200, 300, 120, 40), VERDE_CLARO, VERDE_ESCURO, BRANCO, facil)
        botoes("Médio", (350, 300, 120, 40), AMARELO, AMARELO_ESCURO, BRANCO, medio)
        botoes("Díficil", (500, 300, 120, 40), VERMELHO_CLARO, VERMELHO, BRANCO, dificil)
        fonte3 = pygame.font.SysFont("arial", 20)
        voltar = fonte3.render('Pressione ESC para voltar ao menu principal.', False, VERDE_ESCURO)
        screen.blit(voltar, (200, 500))
        pygame.display.update()
        clock.tick(15)

def facil():
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    snake = [(400, 300)]
    snake_skin = pygame.Surface((20, 20))
    snake_skin.fill(COR2)
    my_direction = None

    apple_pos = on_grid_random()
    apple = pygame.Surface((20, 20))
    apple.fill((255, 0, 0))
    fechar = False

    pontos = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    macas = font.render("Maças coletadas: " + str(pontos), True, BRANCO, PRETO)
    macasRect = macas.get_rect()
    macasRect.center = (10, 10)

    while not fechar:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                if event.key == K_BACKSPACE:
                    fechar = True
                if event.key == K_UP:
                    my_direction = UP
                if event.key == K_DOWN:
                    my_direction = DOWN
                if event.key == K_RIGHT:
                    my_direction = RIGHT
                if event.key == K_LEFT:
                    my_direction = LEFT
                if event.key == K_w:
                    my_direction = UP
                if event.key == K_s:
                    my_direction = DOWN
                if event.key == K_d:
                    my_direction = RIGHT
                if event.key == K_a:
                    my_direction = LEFT

        if collision(snake[0], apple_pos):
            apple_pos = on_grid_random()
            snake.append((0, 0))
            pontos = pontos+1
            macas = font.render("Maças coletadas: " + str(pontos), True, BRANCO, PRETO)


        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i - 1][0], snake[i - 1][1])

        if my_direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - 20)
        if my_direction == RIGHT:
            snake[0] = (snake[0][0] + 20, snake[0][1])
        if my_direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 20)
        if my_direction == LEFT:
            snake[0] = (snake[0][0] - 20, snake[0][1])

        screen.fill((0, 0, 0))
        screen.blit(apple, apple_pos)
        screen.blit(macas, (10, 10))
        for pos in snake:
            screen.blit(snake_skin, pos)
        pygame.display.update()
# Nível medio
def medio():
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    snake = [(400, 300)]
    snake_skin = pygame.Surface((10, 10))
    snake_skin.fill((217, 217, 25))
    my_direction = LEFT

    apple_pos = on_grid_random()
    apple = pygame.Surface((10, 10))
    apple.fill((255, 0, 0))

    veneno_pos = on_grid_random()
    veneno_pos != apple_pos
    veneno = pygame.Surface((10, 10))
    veneno.fill((0, 255, 0))

    while True:
        clock.tick(25)
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_UP:
                    my_direction = UP
                if event.key == K_DOWN:
                    my_direction = DOWN
                if event.key == K_RIGHT:
                    my_direction = RIGHT
                if event.key == K_LEFT:
                    my_direction = LEFT
                if event.key == K_w:
                    my_direction = UP
                if event.key == K_s:
                    my_direction = DOWN
                if event.key == K_d:
                    my_direction = RIGHT
                if event.key == K_a:
                    my_direction = LEFT

        if collision(snake[0], apple_pos):
            apple_pos = on_grid_random()
            snake.append((0, 0))
            veneno_pos = on_grid_random()

        if colisao(snake[0], veneno_pos):
            break

        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i - 1][0], snake[i - 1][1])

        if my_direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
        if my_direction == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])
        if my_direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
        if my_direction == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])

        screen.fill((0, 0, 0))
        screen.blit(apple, apple_pos)
        screen.blit(veneno, veneno_pos)
        for pos in snake:
            screen.blit(snake_skin, pos)
        pygame.display.update()

def dificil():
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    snake = [(400, 300)]
    snake_skin = pygame.Surface((10, 10))
    snake_skin.fill((217, 217, 25))
    my_direction = None

    apple_pos = on_grid_random()
    apple = pygame.Surface((10, 10))
    apple.fill((255, 0, 0))

    while True:
        clock.tick(35)
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_UP:
                    my_direction = UP
                if event.key == K_DOWN:
                    my_direction = DOWN
                if event.key == K_RIGHT:
                    my_direction = RIGHT
                if event.key == K_LEFT:
                    my_direction = LEFT
                if event.key == K_w:
                    my_direction = UP
                if event.key == K_s:
                    my_direction = DOWN
                if event.key == K_d:
                    my_direction = RIGHT
                if event.key == K_a:
                    my_direction = LEFT

        if collision(snake[0], apple_pos):
            apple_pos = on_grid_random()
            snake.append((0, 0))

        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i - 1][0], snake[i - 1][1])


        if my_direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
        if my_direction == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])
        if my_direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
        if my_direction == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])

        screen.fill((0, 0, 0))
        screen.blit(apple, apple_pos)
        for pos in snake:
            screen.blit(snake_skin, pos)
        pygame.display.update()

# Definir padrão dos textos
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

# Menuzinho
def menu_jogo():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()

        screen.fill(PRETO)
        fonte = pygame.font.SysFont('comicsansms', 40)
        surface_text, rect_text = text_objects("Jogo da Cobrinha", fonte, COR)
        rect_text.center = (300, 260)
        screen.blit(surface_text, rect_text)

        botoes("Iniciar", (600, 100, 120, 40), VERDE_CLARO, VERDE_ESCURO, BRANCO, niveis)
        botoes("Como Jogar", (600, 200, 120, 40), BRANCO, CINZA, PRETO, como_jogar)
        botoes("Créditos", (600, 300, 120, 40), BRANCO, CINZA, PRETO, creditos)
        botoes("Fechar", (600, 400, 120, 40), VERMELHO_CLARO, VERMELHO, BRANCO, fechar)

        pygame.display.update()
        clock.tick(15)


def fechar():
    quit()

menu_jogo()
quit()