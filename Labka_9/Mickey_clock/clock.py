import pygame
from datetime import datetime


class MickeyClock:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.center = (width // 2, height // 2)

        self.bg = pygame.image.load("images/mickey_body.png").convert()
        self.bg = pygame.transform.scale(self.bg, (width, height))

        self.minute_hand = pygame.image.load("images/hand.png").convert_alpha()
        self.second_hand = pygame.image.load("images/hand.png").convert_alpha()

        self.minute_hand = pygame.transform.smoothscale(
            self.minute_hand,
            (self.minute_hand.get_width() // 3, self.minute_hand.get_height() // 3)
        )

        self.second_hand = pygame.transform.smoothscale(
            self.second_hand,
            (self.second_hand.get_width() // 3, self.second_hand.get_height() // 3)
        )

    def rotate_from_edge(self, image, angle, center):
        rotated = pygame.transform.rotate(image, -angle)

        rect = rotated.get_rect()

        pivot_offset = pygame.math.Vector2(0, rect.height // 2.5)
        rotated_offset = pivot_offset.rotate(angle)

        rect.center = (
            center[0] - rotated_offset.x,
            center[1] - rotated_offset.y
        )

        return rotated, rect

    def get_time_angles(self):
        now = datetime.now()

        seconds = now.second + now.microsecond / 1_000_000
        minutes = now.minute + seconds / 60

        sec_angle = (seconds / 60) * 360
        min_angle = (minutes / 60) * 360

        return sec_angle, min_angle

    def draw(self, screen):
        screen.blit(self.bg, (0, 0))

        sec_angle, min_angle = self.get_time_angles()

        sec_img, sec_rect = self.rotate_from_edge(self.second_hand, sec_angle, self.center)
        min_img, min_rect = self.rotate_from_edge(self.minute_hand, min_angle, self.center)

        screen.blit(min_img, min_rect)
        screen.blit(sec_img, sec_rect)