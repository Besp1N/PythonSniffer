import pygame
import sys
import threading
from scapy.all import get_if_list
from my_sniffer import sniff_packets, save_packets_to_file

# Inicjalizacja Pygame
pygame.init()

# Ustawienia kolorów
BACKGROUND_COLOR = (72, 80, 185)
BUTTON_COLOR = (85, 224, 163)
DISABLED_BUTTON_COLOR = (150, 150, 150)  # Kolor nieaktywnego przycisku
SELECTED_BUTTON_COLOR = (200, 100, 255)  # Kolor wybranego przycisku
TEXT_COLOR = (255, 255, 255)

# Ustawienia okna
WIDTH, HEIGHT = 1200, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Packet Sniffer with GUI")

font = pygame.font.SysFont(None, 20)


# Funkcja rysująca przycisk
def draw_button(x, y, width, height, color, text, selected=False, enabled=True):
    if selected:
        color = SELECTED_BUTTON_COLOR
    if not enabled:
        color = DISABLED_BUTTON_COLOR
    pygame.draw.rect(screen, color, (x, y, width, height), border_radius=10)

    text_surface = font.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(text_surface, text_rect)


# Funkcja pobierająca interfejsy
def get_interfaces():
    return get_if_list()


# Główna pętla gry
def main():
    interfaces = get_interfaces()

    button_width = (WIDTH - 20) // len(interfaces)
    buttons = []
    x, y = 10, HEIGHT // 4
    for interface in interfaces:
        button_rect = pygame.Rect(x, y, button_width, 50)
        buttons.append((button_rect, True))
        x += button_width + 10
        if x + button_width > WIDTH:
            x = 10
            y += 60

    start_button_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 80, 100, 50)
    start_button = (start_button_rect, False)

    selected_button = None
    stop_event = threading.Event()

    while True:
        screen.fill(BACKGROUND_COLOR)
        font_big = pygame.font.SysFont(None, 30)
        text_surface = font_big.render("Wybierz interfejs", True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4 - 25))
        screen.blit(text_surface, text_rect)

        for button_data in buttons:
            button, active = button_data
            draw_button(button.x, button.y, button.width, button.height, BUTTON_COLOR,
                        interfaces[buttons.index(button_data)].upper(), selected=not active)

        draw_button(start_button[0].x, start_button[0].y, start_button[0].width, start_button[0].height, BUTTON_COLOR,
                    "Start", selected=not start_button[1], enabled=selected_button is not None)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i, button_data in enumerate(buttons):
                        button, active = button_data
                        if button.collidepoint(event.pos) and active:
                            print(f"Kliknięto przycisk dla interfejsu: {interfaces[i]}")
                            selected_button = interfaces[i]
                            for j in range(len(buttons)):
                                if j != i:
                                    buttons[j] = (buttons[j][0], False)
                            break
                    if start_button[0].collidepoint(event.pos) and selected_button is not None and not start_button[1]:
                        print(f"Kliknięto przycisk Start and selected: {selected_button}")
                        start_button = (start_button[0], True)
                        stop_event.clear()
                        sniffer_thread = threading.Thread(target=sniff_packets, args=(selected_button,))
                        sniffer_thread.start()

        pygame.display.flip()


if __name__ == "__main__":
    main()
