import pygame

pygame.init()

WIDTH,HEIGHT = 500,400

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Pygame Circles")

WHITE = (255,255,255)
GREEN = (0,255,0)

solid_circle_center = (200,200)
solid_circle_radius = 50

hollow_circle_center = (350,200)
hollow_circle_radius = 50
hollow_circle_width = 3

running = True

while running:
    screen.fill(WHITE)
    pygame.draw.circle(screen, GREEN, solid_circle_center, solid_circle_radius)
    pygame.draw.circle(screen, GREEN, hollow_circle_center, hollow_circle_radius, hollow_circle_width)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    pygame.display.flip()      

pygame.quit()  
