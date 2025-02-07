# Import Necessary Libraries
import pygame

# Initialize required modules
pygame.init()

# Setup window geometry
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Pygame Window")

# Create a loop to run till the game is quit by the user
running = True
while running:
    # Clear the event queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False

    # Make the changes visible
    pygame.display.flip()  

# Quit Pygame properly
pygame.quit()
