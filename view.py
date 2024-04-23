import pygame
import sys

pygame.init()

# Ustawienia okna
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
BACKGROUND_COLOR = (255, 255, 255)
FONT_COLOR = (0, 0, 0)
FONT_SIZE = 24
OPTIONS = ["Option 1", "Option 2", "Option 3"]

# Funkcja rysująca tekst
def draw_text(surface, text, font, color, rect):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)

# Funkcja główna
def main():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Rozwijana lista w Pygame")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, FONT_SIZE)

    dropdown_rect = pygame.Rect(100, 100, 200, 40)
    selected_option = None
    dropdown_expanded = False

    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)

        # Obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if dropdown_rect.collidepoint(event.pos):
                    dropdown_expanded = not dropdown_expanded
                elif dropdown_expanded:
                    option_index = (event.pos[1] - dropdown_rect.y) // dropdown_rect.height
                    if 0 <= option_index < len(OPTIONS):
                        selected_option = OPTIONS[option_index]
                        dropdown_expanded = False

        # Rysowanie rozwijanej listy
        pygame.draw.rect(screen, BACKGROUND_COLOR, dropdown_rect)
        pygame.draw.rect(screen, FONT_COLOR, dropdown_rect, 2)
        draw_text(screen, selected_option or "Select an option", font, FONT_COLOR, dropdown_rect)

        # Rysowanie opcji rozwijanej listy
        if dropdown_expanded:
            for i, option in enumerate(OPTIONS):
                option_rect = dropdown_rect.copy()
                option_rect.y += (i + 1) * dropdown_rect.height
                pygame.draw.rect(screen, BACKGROUND_COLOR, option_rect)
                pygame.draw.rect(screen, FONT_COLOR, option_rect, 2)
                draw_text(screen, option, font, FONT_COLOR, option_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
