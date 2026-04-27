import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 22)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 180, 0)
BLUE = (0, 0, 220)
YELLOW = (255, 255, 0)

screen.fill(WHITE)

current_color = BLACK
mode = "brush"
drawing = False
brush_size = 5

running = True

while running:
    clock.tick(200)

    # Жағдайаттар чек
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Баскару кловератураы
        if event.type == pygame.KEYDOWN:

            # инструменттер баскаратын
            if event.key == pygame.K_1:
                mode = "brush"
            elif event.key == pygame.K_2:
                mode = "eraser"

            # түстер
            elif event.key == pygame.K_r:
                current_color = RED
                mode = "brush"
            elif event.key == pygame.K_g:
                current_color = GREEN
                mode = "brush"
            elif event.key == pygame.K_b:
                current_color = BLUE
                mode = "brush"
            elif event.key == pygame.K_y:
                current_color = YELLOW
                mode = "brush"
            elif event.key == pygame.K_k:
                current_color = BLACK
                mode = "brush"

            # Кетіру
            elif event.key == pygame.K_c:
                screen.fill(WHITE)

        # Мышкамен томенге басып турып
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True

        # Мышкамен жогыры басып турып
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

    #экранга шыгару 
    if drawing:
        mouse_pos = pygame.mouse.get_pos()

        if mode == "brush":
            pygame.draw.circle(screen, current_color, mouse_pos, brush_size)

        elif mode == "eraser":
            pygame.draw.circle(screen, WHITE, mouse_pos, 15)

    # информация манелдегі
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, 35))
    info = font.render(
        "1 Brush | 2 Eraser | R G B Y K colors | C Clear",
        True,
        BLACK
    )
    screen.blit(info, (10, 5))

    pygame.display.update()

pygame.quit()