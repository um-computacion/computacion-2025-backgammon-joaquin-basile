import pygame

class TextField:
    def __init__(self, x: int, y: int, width: int, height: int, placeholder_text: str):
        self.__rect = pygame.Rect(x, y, width, height)
        self.__text = ""
        self.__placeholder = placeholder_text
        self.__active = False
        self.__font = pygame.font.Font(None, 36)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.__active = self.__rect.collidepoint(event.pos)
            
        if event.type == pygame.KEYDOWN and self.__active:
            if event.key == pygame.K_RETURN:
                self.__active = False
            elif event.key == pygame.K_BACKSPACE:
                self.__text = self.__text[:-1]
            else:
                if len(self.__text) < 15:
                    self.__text += event.unicode

    def render(self, screen: pygame.Surface):
        # Color del borde según esté activo o no
        border_color = (0, 120, 215) if self.__active else (150, 150, 150)
        
        # Dibujar el campo
        pygame.draw.rect(screen, (255, 255, 255), self.__rect)
        pygame.draw.rect(screen, border_color, self.__rect, 3)
        
        # Mostrar texto o placeholder
        display_text = self.__text if self.__text else self.__placeholder
        text_color = (0, 0, 0) if self.__text else (150, 150, 150)
        text_surface = self.__font.render(display_text, True, text_color)
        screen.blit(text_surface, (self.__rect.x + 10, self.__rect.y + 10))

    def get_text(self) -> str:
        return self.__text
    
    def is_active(self) -> bool:
        return self.__active
