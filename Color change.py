#Write a Python program to add two sprites and create a custom event of changing the colour of the sprites.

import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def change_color(self):
        self.color = [random.randint(0, 255) for _ in range(3)]
        self.image.fill(self.color)

sprites = pygame.sprite.Group(
    Sprite(100, 200, (255, 0, 0)),
    Sprite(300, 200, (0, 0, 255))
)

running = True
while running:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == CHANGE_COLOR_EVENT:
            for sprite in sprites:
                sprite.change_color()

    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
