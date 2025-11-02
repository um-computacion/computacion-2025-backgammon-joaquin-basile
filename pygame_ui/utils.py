import pygame
def highlight_surface(surface, color=(255, 255, 0), alpha=50):
    """Añade un efecto de brillo a una surface"""
    highlighted = surface.copy()
    overlay = pygame.Surface(surface.get_size())
    overlay.fill(color)
    overlay.set_alpha(alpha)
    highlighted.blit(overlay, (0, 0))
    return highlighted

