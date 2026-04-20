import pygame


class Ball:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.radius = 25
        self.x = width // 2
        self.y = height // 2

        self.speed = 20
        self.color = (255, 0, 0)

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            if self.x - self.speed - self.radius >= 0:
                self.x -= self.speed

        if keys[pygame.K_RIGHT]:
            if self.x + self.speed + self.radius <= self.width:
                self.x += self.speed

        if keys[pygame.K_UP]:
            if self.y - self.speed - self.radius >= 0:
                self.y -= self.speed

        if keys[pygame.K_DOWN]:
            if self.y + self.speed + self.radius <= self.height:
                self.y += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)