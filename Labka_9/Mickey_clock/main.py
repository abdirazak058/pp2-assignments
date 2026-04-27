import pygame
import sys
from clock import MickeyClock

pygame.init()

WIDTH, HEIGHT = 700, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Сагат")

clock = pygame.time.Clock()

mickey_clock = MickeyClock(WIDTH, HEIGHT)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mickey_clock.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()