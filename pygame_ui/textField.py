import pygame

class TextField:
    def __init__(self, x: int, y: int, width: int, height: int, placeholder_text: str):
        self.__rect = pygame.Rect(x, y, width, height)
        self.__text = ""
        self.__placeholder = placeholder_text
        self.__active = False
        self.__color = GRAY
        
    def handle_event(self, event: pygame.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.__active = self.rect.collidepoint(event.pos)
            self.__color = BLUE if self.__active else GRAY
            
        if event.type == pygame.KEYDOWN and self.__active:
            if event.key == pygame.K_RETURN:
                self.__active = False
                self.__color = GRAY
            elif event.key == pygame.K_BACKSPACE:
                self.__text = self.__text[:-1]
            else:
                if len(self.__text) < 15:
                    self.__text += event.unicode

    def draw(self, screen):
        # Draw field rectangle
        pygame.draw.rect(screen, self.color, self.rect, 3)
        pygame.draw.rect(screen, WHITE, self.rect)
        pygame.draw.rect(screen, self.color, self.rect, 3)
        
        # Show text or placeholder
        display_text = self.text if self.text else self.placeholder
        text_color = BLACK if self.text else DARK_GRAY
        text_surface = text_font.render(display_text, True, text_color)
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))

    def get_text(self) -> str:
        return self.__text
