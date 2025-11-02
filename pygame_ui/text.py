import pygame
class Text():
    def __init__(
        self, 
        x: int,
        y: int,
        content: str, 
        font_size: int = 20, 
        color: tuple[int, int, int] = (100, 100, 100)
    ):
        self.__font = pygame.font.Font(None, font_size)
        self.__content = content
        self.__color = color
        self.__x = x 
        self.__y = y 
        self.__text_surface = self.__font.render(self.__content, True, self.__color)

    def set_content(self, new_content: str):
        self.__content = new_content
        self.set_surface()

    def set_font_size(self, new_size):
        self.__font_size = new_size
        self.set_surface()

    def set_color(self, new_color):
        self.__color = new_color
        self.set_surface()

    def set_surface(self):
        self.__text_surface = self.__font.render(self.__content, True, self.__color)

    def get_content(self):
        return self.content
    def get_font_size(self):
        return self.font_size
    def get_color(self):
        return self.color

    def render(self, screen: pygame.Surface) -> pygame.Surface:
        text_rect = self.__text_surface.get_rect()
        text_rect.center = (self.__x, self.__y)
        screen.blit(self.__text_surface, text_rect)
