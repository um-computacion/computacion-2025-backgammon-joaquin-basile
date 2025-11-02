import pygame
from core.const import black, white

class Point():
    def __init__(
        self, 
        screen: pygame.Surface, 
        top: int,
        left: int,
        width: int,
        heigth: int,
        orientacion: str,
        scale: float = 1.0
    ):
        self.__screen = screen
        self.__top = top
        self.__left = left
        self.__width = width
        self.__height = heigth
        self.__orientation = orientacion
        self.__rect = pygame.Rect(left, top, width, heigth)
        self.__scale = scale

        self.__checker_radius = 10 * self.__scale

    def render(self, quantity: int, color: str):
        """
        Render the checkers stacked within the point.

        Args:
            quantity (int): Number of checkers to render.
            color (str): Color of the checkers (e.g., 'black' or 'white').
        """
        spacing = 5  # Space between checkers

        # Posición X centrada en el point
        checker_position_x = self.__left + (self.__width - 2 * self.__checker_radius) // 2
        
        for i in range(quantity):
            if self.__orientation == 'top':
                # Stack checkers from top to bottom
                y_position = self.__top + i * (2 * self.__checker_radius + spacing)
            elif self.__orientation == 'bot':
                # Stack checkers from bottom to top
                y_position = self.__top + self.__height - (i + 1) * (2 * self.__checker_radius + spacing)
            else:
                raise ValueError("Invalid orientation. Use 'top' or 'bot'.")

            color_rgb = (0, 0, 0) if color == black else (255, 255, 255)
            checker = self.create_checker(color_rgb)
            # CORRECCIÓN: Las coordenadas estaban invertidas
            self.__screen.blit(checker, (checker_position_x, y_position))

    def create_checker(self, color) -> pygame.Surface:
        size = self.__checker_radius * 2
        surface = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(surface, color, (self.__checker_radius, self.__checker_radius), self.__checker_radius)
        pygame.draw.circle(surface, (0, 0, 0), (self.__checker_radius, self.__checker_radius), self.__checker_radius, 2)
        return surface
    
    def get_rect(self) -> pygame.Rect:
        return self.__rect
