#Write a Python program to create a Game screen and add two rectangular sprites to it using the Pygame library. 
# Add controls to one of the sprites as well for up, down, left and right movements.


import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Rectangular Sprite Game")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

sprite_speed = 5

sprite1 = pygame.Rect(100, 100, 50, 50)

sprite2 = pygame.Rect(400, 300, 50, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        sprite2.x -= sprite_speed
    if keys[pygame.K_RIGHT]:
        sprite2.x += sprite_speed
    if keys[pygame.K_UP]:
        sprite2.y -= sprite_speed
    if keys[pygame.K_DOWN]:
        sprite2.y += sprite_speed

    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, sprite1)
    pygame.draw.rect(screen, BLUE, sprite2)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
