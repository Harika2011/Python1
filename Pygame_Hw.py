#Write a Python program to create your first Game screen using the Pygame library.


import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("My First Pygame Screen")

WHITE = (0, 0, 0)
BLUE = (204, 255, 255)

running = True

while running:
    screen.fill(WHITE)  

    pygame.draw.rect(screen, BLUE, (350, 250, 100, 100)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

    pygame.display.update()  


pygame.quit()
