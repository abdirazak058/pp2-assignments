import pygame
import random
import sys

pygame.init()

# Бет настрока
WIDTH = 600
HEIGHT = 600
BLOCK_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Түс
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (220, 0, 0)
WHITE = (255, 255, 255)

# Жазу ностр
font = pygame.font.SysFont("Arial", 28)

# FPS
clock = pygame.time.Clock()

# Aruzhanнын настройкасы хахаха!
snake = [(300, 300)]
dx = BLOCK_SIZE
dy = 0

# Ойын ностройка
score = 0
level = 1
speed = 8


def Aru_tamak():
    # Рандом тамак шыгару жане тамак жылан устинен туспеу керек
    while True:
        x = random.randrange(0, WIDTH, BLOCK_SIZE)
        y = random.randrange(0, HEIGHT, BLOCK_SIZE)

        if (x, y) not in snake:
            return x, y


food_x, food_y = Aru_tamak()


def Aru_dene():
    # Аружан(Жылан) денесңн салу
    for block in snake:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))


def Aru_tamak_shugary():
    # Тамак шыгару
    pygame.draw.rect(screen, RED, (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))


def show_score_level():
    # Упай мен уривень корсетет
    text = font.render(f"Score: {score}   Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))


def game_over():
    # Утылып калгандагы
    screen.fill(BLACK)

    text = font.render("Аружан олди xaxaxa", True, RED)
    score_text = font.render(f"Final Score: {score}", True, WHITE)

    screen.blit(text, (220, 250))
    screen.blit(score_text, (200, 290))

    pygame.display.update()
    pygame.time.delay(2500)


running = True

while running:
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Keyboard control
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx = 0
                dy = -BLOCK_SIZE

            elif event.key == pygame.K_DOWN and dy == 0:
                dx = 0
                dy = BLOCK_SIZE

            elif event.key == pygame.K_LEFT and dx == 0:
                dx = -BLOCK_SIZE
                dy = 0

            elif event.key == pygame.K_RIGHT and dx == 0:
                dx = BLOCK_SIZE
                dy = 0

    # Аружанның (Жыланның) басына косу осуі
    head_x, head_y = snake[0]
    new_head = (head_x + dx, head_y + dy)

    # Шекара тексеру
    if (
        new_head[0] < 0 or
        new_head[0] >= WIDTH or
        new_head[1] < 0 or
        new_head[1] >= HEIGHT
    ):
        game_over()
        break

    # Аружан(Жылан) өзіне согылдыма
    if new_head in snake:
        game_over()
        break

    # Жана бас косылып жылан оседі
    snake.insert(0, new_head)

    # Тамакпен жыланнын басы бир рандом кардинатада болса жылан оны жеди деп басына бас косамызжыланның
    if new_head == (food_x, food_y):
        score += 1

        # Әр 3 ояко сайын аружан оседі
        level = score // 3 + 1

        # Аружан оскен сайын тез журеди
        speed = 8 + level * 2

        food_x, food_y = Aru_tamak()
    else:
        # Аружан тамак жемесе салмак тастайды
        snake.pop()

    # Экран шыгару!
    screen.fill(BLACK)
    Aru_dene()
    Aru_tamak_shugary()
    show_score_level()

    pygame.display.update()

pygame.quit()