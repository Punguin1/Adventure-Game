import pygame
import pygame_gui as pgui

pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#055555'))

is_running = True
clock = pygame.time.Clock()
manager = pgui.UIManager((800, 600))

                                             text='Say Hello',
                                             manager=manager)
while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pgui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                print('Hello World!')
        manager.process_events(event)
    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    pygame.display.update()