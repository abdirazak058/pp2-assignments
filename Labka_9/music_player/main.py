import pygame
import sys
from player import MusicPlayer

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

player = MusicPlayer()

running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                player.play()
            elif event.key == pygame.K_p:
                player.pause()
            elif event.key == pygame.K_n:
                player.next_track()
            elif event.key == pygame.K_b:
                player.prev_track()
            elif event.key == pygame.K_q:
                running = False

    track_name = player.get_track_name()
    status = player.get_status()
    time_text = player.get_time_text()

    text1 = font.render(f"Track: {track_name}", True, (255, 255, 255))
    text2 = font.render(f"Status: {status}", True, (200, 200, 200))
    text3 = font.render(time_text, True, (180, 180, 180))
    text4 = font.render("R=Resume P=Pause N=Next B=Back Q=Quit", True, (255, 0, 255))

    screen.blit(text1, (20, 40))
    screen.blit(text2, (20, 90))
    screen.blit(text3, (20, 140))
    screen.blit(text4, (20, 220))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()