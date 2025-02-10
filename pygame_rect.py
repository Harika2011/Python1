import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600  
BLACK = (0, 0, 0)        
BLUE = (0, 125, 255)      

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Rectangle Example")

rect_x = 200 
rect_y = 150   
rect_width = 100  
rect_height = 80  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))

    pygame.display.flip()

pygame.quit()
