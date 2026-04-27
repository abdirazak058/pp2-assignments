import pygame
import random
import sys

pygame.init()

# Бет настройкасы!
WIDTH = 600
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

# Түстер!
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
YELLOW = (255, 220, 0)
BLACK = (0, 0, 0)

# FPS
clock = pygame.time.Clock()
FPS = 60

# Жазу
font = pygame.font.SysFont("Arial", 30)

# Машина скорсть
player_width = 50
player_height = 90
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 120
player_speed = 7

# Load player car image
player_img = pygame.image.load("images/car.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (player_width, player_height))

# Enemy settings
enemy_width = 50
enemy_height = 90
enemy_x = random.randint(80, WIDTH - 130)
enemy_y = -100
enemy_speed = 5

# Мент машинасы!
try:
    enemy_img = pygame.image.load("images/car2.png").convert_alpha()
    enemy_img = pygame.transform.scale(enemy_img, (enemy_width, enemy_height))
except:
    enemy_img = None  # Егер сурет болмаса fallback болады

# Очко
coin_radius = 15
coin_x = random.randint(80, WIDTH - 80)
coin_y = -50
coin_speed = 4
coins = 0

coin_types = [
    {"color": (255, 220, 0), "value": 1},   # yellow
    {"color": (0, 150, 255), "value": 2},   # blue
    {"color": (255, 0, 0), "value": 3}      # red
]

current_coin = random.choice(coin_types)

score = 0
Basta = True


def Jol():
    screen.fill(GRAY)

    pygame.draw.line(screen, WHITE, (70, 0), (70, HEIGHT), 5)
    pygame.draw.line(screen, WHITE, (WIDTH - 70, 0), (WIDTH - 70, HEIGHT), 5)

    for y in range(0, HEIGHT, 80):
        pygame.draw.line(screen, WHITE, (WIDTH // 2, y), (WIDTH // 2, y + 40), 5)


def Car_kordinat(x, y):
    # Машина суретін шығару
    screen.blit(player_img, (x, y))


def Car_ment_kordinat(x, y):
    # Егер enemy.png бар болса – соны қолданамыз
    if enemy_img:
        screen.blit(enemy_img, (x, y))
    else:
        pygame.draw.rect(screen, (220, 0, 0), (x, y, enemy_width, enemy_height))


def Score_kordinate(x, y):
    pygame.draw.circle(screen, current_coin["color"], (coin_x, coin_y), coin_radius)


def show_text():
    score_text = font.render(f"Score: {score}", True, WHITE)
    coin_text = font.render(f"Coins: {coins}", True, YELLOW)

    screen.blit(score_text, (20, 20))
    screen.blit(coin_text, (WIDTH - 150, 20))


def game_over():
    screen.fill(BLACK)
    text = font.render("усталып калдын хахахахаха", True, (255, 0, 0))
    screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
    pygame.display.update()
    pygame.time.delay(2000)


while Basta:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Check клавература басылып турма!
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x > 80:
        player_x -= player_speed

    if keys[pygame.K_RIGHT] and player_x < WIDTH - 80 - player_width:
        player_x += player_speed

    # Enemy төмен түсу!
    enemy_y += enemy_speed

    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(80, WIDTH - 130)
        score += 1

    # Coin төмен түсуі!
    coin_y += coin_speed

    if coin_y > HEIGHT:
        coin_y = -50
        coin_x = random.randint(80, WIDTH - 80)

    # Тексеру RECT - каробка чтобы авария немесе упай тексеру!
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height) # Кедергі тидін
    coin_rect = pygame.Rect(coin_x - coin_radius, coin_y - coin_radius, coin_radius * 2, coin_radius * 2) # Мал упайын кутты болсын

    if player_rect.colliderect(enemy_rect):
        game_over()
        Basta = False

    if player_rect.colliderect(coin_rect):
        coins += current_coin["value"]

        coin_y = -50
        coin_x = random.randint(80, WIDTH - 80)

        current_coin = random.choice(coin_types)
    
    enemy_speed = min(10, 5 + coins // 5)
    coin_speed = min(9, 4 + coins // 5)

    # Барин шыгару!
    Jol()
    Car_kordinat(player_x, player_y)
    Car_ment_kordinat(enemy_x, enemy_y)
    Score_kordinate(coin_x, coin_y)
    show_text()

    pygame.display.update()

pygame.quit()