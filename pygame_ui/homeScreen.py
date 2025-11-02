import pygame
from pygame_ui.exceptions import ExitGame

class HomeScreen():
    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height
        self.__running = True
        self.__backgorun_color = (255, 255, 255)

    def render(self):
        while self.__running:
            for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise ExitGame()
            screen = pygame.display.set_mode((self.__width, self.__height))
            screen.fill(self.__backgorun_color)
            pygame.display.flip()

