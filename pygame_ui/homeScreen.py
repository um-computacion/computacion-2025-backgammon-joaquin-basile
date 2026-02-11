import pygame
from pygame_ui.textField import TextField
from pygame_ui.text import Text
from core.backgammon import Backgammon

class HomeScreen:
    def __init__(self, backgammon: Backgammon, screen: pygame.Surface):
        self.__backgammon = backgammon
        self.__screen = screen
        self.__running = True
        self.__background_color = (45, 52, 54)
        
        # Crear campos de texto para los nombres
        width = screen.get_width()
        height = screen.get_height()
        center_x = width // 2
        self.__player1_field = TextField(
            center_x - 200, 
            height // 2 - 80, 
            400, 
            50, 
            "Jugador 1 (Negro)"
        )
        self.__player2_field = TextField(
            center_x - 200, 
            height // 2 + 20, 
            400, 
            50, 
            "Jugador 2 (Blanco)"
        )
        
        # Textos
        self.__title = Text(
            center_x, 
            100, 
            "BACKGAMMON", 
            font_size=100, 
            color=(236, 240, 241)
        )
        self.__instruction = Text(
            center_x,
            height // 2 - 150,
            "Ingresa los nombres de los jugadores",
            font_size=40,
            color=(189, 195, 199)
        )
        self.__start_button_text = Text(
            center_x,
            height // 2 + 120,
            "PRESIONA ENTER PARA COMENZAR",
            font_size=35,
            color=(46, 204, 113)
        )

    def render(self):
        """Renderiza la pantalla de inicio y retorna los nombres"""
        while self.__running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
                    return None, None  # Salir del juego
                
                # Manejar eventos en los campos de texto
                self.__player1_field.handle_event(event)
                self.__player2_field.handle_event(event)
                
                # Detectar ENTER para comenzar
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    p1_name = self.__player1_field.get_text().strip()
                    p2_name = self.__player2_field.get_text().strip()
                    print(p1_name, p2_name)
                    self.__backgammon.with_players(p1_name, p2_name)
                    self.__running = False
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    rect = self.__start_button_text.get_surface().get_rect()
                    if rect.collidepoint(pygame.mouse.get_pos()):
                        p1_name = self.__player1_field.get_text().strip()
                        p2_name = self.__player2_field.get_text().strip()
                        print(p1_name, p2_name)
                        self.__backgammon.with_players(p1_name, p2_name)
                        self.__running = False
                        return


            
            # Dibujar la pantalla
            self.__screen.fill(self.__background_color)
            self.__title.render(self.__screen)
            self.__instruction.render(self.__screen)
            self.__player1_field.render(self.__screen)
            self.__player2_field.render(self.__screen)
            self.__start_button_text.render(self.__screen)
            
            pygame.display.flip()
            pygame.time.Clock().tick(60)

