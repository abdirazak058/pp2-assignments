import pygame
import sys
import math

pygame.init()

# Screen settings
WIDTH = 900
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 180, 0)
BLUE = (0, 90, 255)
YELLOW = (255, 220, 0)

# Basic settings
screen.fill(WHITE)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 22)

# Current tool and color
current_color = BLACK
current_tool = "pencil"
brush_size = 5

# Toolbar buttons
buttons = {
    "pencil": pygame.Rect(10, 10, 90, 35),
    "rect": pygame.Rect(110, 10, 90, 35),
    "circle": pygame.Rect(210, 10, 90, 35),
    "eraser": pygame.Rect(310, 10, 90, 35),
}

# Color buttons
color_buttons = [
    (BLACK, pygame.Rect(430, 10, 30, 30)),
    (RED, pygame.Rect(470, 10, 30, 30)),
    (GREEN, pygame.Rect(510, 10, 30, 30)),
    (BLUE, pygame.Rect(550, 10, 30, 30)),
    (YELLOW, pygame.Rect(590, 10, 30, 30)),
]

drawing = False
start_pos = None


def draw_toolbar():
    # Toolbar background
    pygame.draw.rect(screen, (230, 230, 230), (0, 0, WIDTH, 55))

    # Tool buttons
    for name, rect in buttons.items():
        color = (180, 180, 180) if current_tool == name else (210, 210, 210)
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)

        text = font.render(name, True, BLACK)
        screen.blit(text, (rect.x + 10, rect.y + 6))

    # Color buttons
    for color, rect in color_buttons:
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)

    # Current color indicator
    pygame.draw.rect(screen, current_color, (650, 10, 35, 30))
    pygame.draw.rect(screen, BLACK, (650, 10, 35, 30), 2)


def get_rect(start, end):
    # Rectangle дұрыс бағытта шығуы үшін
    x1, y1 = start
    x2, y2 = end

    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x2 - x1)
    h = abs(y2 - y1)

    return pygame.Rect(x, y, w, h)


def draw_final_shape(start, end):
    # Rectangle немесе circle салу
    if current_tool == "rect":
        rect = get_rect(start, end)
        pygame.draw.rect(screen, current_color, rect, 3)

    elif current_tool == "circle":
        x1, y1 = start
        x2, y2 = end

        radius = int(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
        pygame.draw.circle(screen, current_color, start, radius, 3)


running = True

while running:
    clock.tick(60)

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Mouse button down
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicked_toolbar = False

                # Check tool buttons
                for name, rect in buttons.items():
                    if rect.collidepoint(event.pos):
                        current_tool = name
                        clicked_toolbar = True

                # Check color buttons
                for color, rect in color_buttons:
                    if rect.collidepoint(event.pos):
                        current_color = color
                        current_tool = "pencil"
                        clicked_toolbar = True

                if not clicked_toolbar and event.pos[1] > 55:
                    drawing = True
                    start_pos = event.pos

        # Mouse movement
        if event.type == pygame.MOUSEMOTION:
            if drawing:
                if current_tool == "pencil":
                    pygame.draw.circle(screen, current_color, event.pos, brush_size)

                elif current_tool == "eraser":
                    pygame.draw.circle(screen, WHITE, event.pos, 15)

        # Mouse button up
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                end_pos = event.pos

                if current_tool in ["rect", "circle"]:
                    draw_final_shape(start_pos, end_pos)

                drawing = False
                start_pos = None

    # Draw toolbar every frame
    draw_toolbar()

    pygame.display.update()

pygame.quit()