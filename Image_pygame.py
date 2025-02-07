import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Window with Image")

WHITE = (255, 255, 255)

image = pygame.image.load("Code.png")  
image = pygame.transform.scale(image, (300, 300))  
image_rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False

   
    screen.fill(WHITE)

    screen.blit(image, image_rect)

    pygame.display.flip()

pygame.quit()
