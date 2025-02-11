#Write a Python program to create a Game screen and add elements like - rectangle and text using the Pygame library.


import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Game Screen")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

font = pygame.font.Font(None, 36)  

running = True
while running:
    screen.fill(WHITE)  

    pygame.draw.rect(screen, BLUE, (150, 200, 200, 100))

    text_surface = font.render("Hello, Pygame!", True, RED)
    screen.blit(text_surface, (300, 100)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()  

pygame.quit()
