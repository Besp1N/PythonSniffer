import pygame
import sys
from scapy.all import get_if_list

# Inicjalizacja Pygame
pygame.init()

# Ustawienia kolorów
BACKGROUND_COLOR = (72, 80, 185)
BUTTON_COLOR = (85, 224, 163)
TEXT_COLOR = (255, 255, 255)

# Ustawienia okna
WIDTH, HEIGHT = 1200, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Przyciski w Pygame")


# Funkcja rysująca przycisk
def draw_button(x, y, width, height, color, text):
    pygame.draw.rect(screen, color, (x, y, width, height), border_radius=10)

    font = pygame.font.SysFont(None, 25)
    text_surface = font.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(text_surface, text_rect)


# Funkcja pobierająca interfejsy
def get_interfaces():
    return get_if_list()


# Główna pętla gry
def main():
    # Pobranie interfejsów
    interfaces = get_interfaces()

    # Szerokość przycisku
    button_width = (WIDTH - 20) // len(interfaces)  # Uwzględniamy odstępy

    # Stworzenie listy przycisków na podstawie liczby interfejsów
    buttons = []
    x, y = 10, HEIGHT // 4
    for interface in interfaces:
        button_rect = pygame.Rect(x, y, button_width, 50)
        buttons.append(button_rect)
        x += button_width + 10  # Dodajemy odstęp między przyciskami
        if x + button_width > WIDTH:  # Jeśli przycisk wyjdzie poza ekran, przechodzimy do następnej linii
            x = 10
            y += 60  # Dodajemy odstęp między liniami przycisków

    while True:
        screen.fill(BACKGROUND_COLOR)

        # Napis "Wybierz interfejs"
        font = pygame.font.SysFont(None, 30)
        text_surface = font.render("Wybierz interfejs", True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4 - 25))  # Mniejszy odstęp
        screen.blit(text_surface, text_rect)

        # Rysowanie przycisków
        for i, button in enumerate(buttons):
            draw_button(button.x, button.y, button.width, button.height, BUTTON_COLOR, interfaces[i].upper())

        # Obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Sprawdzamy, czy kliknięto lewym przyciskiem myszy
                    for i, button in enumerate(buttons):
                        if button.collidepoint(event.pos):
                            print(f"Kliknięto przycisk dla interfejsu: {interfaces[i]}")

        pygame.display.flip()


if __name__ == "__main__":
    main()
