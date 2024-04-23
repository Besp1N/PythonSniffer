import pygame
import sys

# Inicjalizacja Pygame
pygame.init()

# Ustawienia kolorów
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Ustawienia okna
WIDTH, HEIGHT = 400, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Przyciski w Pygame")


# Funkcja rysująca przycisk
def draw_button(x, y, width, height, color, text):
    pygame.draw.rect(screen, color, (x, y, width, height))

    font = pygame.font.SysFont(None, 30)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(text_surface, text_rect)


# Główna pętla gry
def main():
    button1 = pygame.Rect(50, 50, 100, 50)
    button2 = pygame.Rect(250, 50, 100, 50)

    while True:
        screen.fill(WHITE)

        # Rysowanie przycisków
        draw_button(button1.x, button1.y, button1.width, button1.height, RED, "Przycisk 1")
        draw_button(button2.x, button2.y, button2.width, button2.height, GREEN, "Przycisk 2")

        # Obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Sprawdzamy, czy kliknięto lewym przyciskiem myszy
                    if button1.collidepoint(event.pos):
                        print("Kliknięto przycisk jeden")
                    elif button2.collidepoint(event.pos):
                        print("Kliknięto przycisk dwa")

        pygame.display.flip()


if __name__ == "__main__":
    main()
