import pygame
import random

pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Sprite:
    def __init__(self):
        self.x, self.y = WIDTH // 2, HEIGHT // 2
        self.size = 50
        self.color = (0, 255, 0)
        self.speed_x, self.speed_y = 5, 5

    def move(self, keys):
        if keys[pygame.K_LEFT]: self.x -= self.speed_x
        if keys[pygame.K_RIGHT]: self.x += self.speed_x
        if keys[pygame.K_UP]: self.y -= self.speed_y
        if keys[pygame.K_DOWN]: self.y += self.speed_y
        self.check_boundary()

    def check_boundary(self):
        if self.x <= 0 or self.x + self.size >= WIDTH:
            self.speed_x = -self.speed_x
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
        if self.y <= 0 or self.y + self.size >= HEIGHT:
            self.speed_y = -self.speed_y
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

sprite = Sprite()
running = True
while running:
    screen.fill((0, 0, 0))
    keys = pygame.key.get_pressed()
    sprite.move(keys)
    sprite.draw()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(30)

pygame.quit()
