import pygame
import sys

pygame.init()

width, height = 600, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Personalized Message App")

font = pygame.font.Font(None, 36)
background_color = (255, 255, 255)
text_color = (0, 0, 0)

def display_message(name):
    window.fill(background_color)
    message = f"Hello, {name}!"
    text_surface = font.render(message, True, text_color)
    text_rect = text_surface.get_rect(center=(width // 2, height // 2))
    window.blit(text_surface, text_rect)
    pygame.display.flip()

def get_user_name():
    input_box = pygame.Rect(150, height // 2, 300, 40)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = True
                    color = color_active
                else:
                    active = False
                    color = color_inactive

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        window.fill(background_color)
        txt_surface = font.render(text, True, text_color)
        width_input_box = max(200, txt_surface.get_width()+10)
        input_box.w = width_input_box
        window.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(window, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)

def main():
    user_name = get_user_name()
    if user_name:
        display_message(user_name)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
