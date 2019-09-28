import pygame.font

available_fonts = pygame.font.get_fonts()
for available_font in sorted(available_fonts):
    print(available_font)
