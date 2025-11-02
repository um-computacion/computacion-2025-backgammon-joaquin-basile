import pygame
from core.backgammon import Backgammon
from pygame_ui.pointManager import PointManager
from pygame_ui.text import Text
from pygame_ui.dice import Dice
from core.const import black, white

class PygameUI:
    '''
    Interfaz grafica para el juego
    '''
    def __init__(self, backgammon: Backgammon = Backgammon(), scale: float = 1.0):
        pygame.init()
        pygame.font.init()
        self.__backgammon = backgammon
        self.__running = True
        self.__scale = scale

        self.__bg_image = pygame.image.load('./assets/board.png')
        self.__bg_image = pygame.transform.scale(
                self.__bg_image,
                (
                    int(self.__bg_image.get_width() * self.__scale), 
                    int(self.__bg_image.get_height() * self.__scale)
                )
        )
        self.__screen = pygame.display.set_mode((self.__bg_image.get_width() + 700, self.__bg_image.get_height()))
        self.__screen_w, self.__screen_h = self.__screen.get_size()

        # Inicializar el PointManager
        self.__point_manager = PointManager(
            self.__screen,
            self.__bg_image.get_width(),
            self.__bg_image.get_height(),
            self.__scale
        )
        self.__dice = Dice(self.__screen, (self.__screen_w - 65, self.__screen_h/2))

        aling_x = self.__screen_w * 0.85
        align_y = self.__screen_h / 2

        self.__title = Text(aling_x, align_y - 0.80*align_y, "Backgammon", font_size=80, color=(0, 0, 0))
        self.__turn_msg = Text(aling_x-20, align_y, "Estado del juego", font_size=50, color=(0, 0, 0))
        self.__bar_msg = Text(aling_x-20, align_y + 40, "Fichas en el bar", font_size=50, color=(0, 0, 0))
        self.__won_checkers_msg = Text(aling_x-20, align_y + 80, "", font_size=40, color=(0, 150, 0))
        self.__error_msg = Text(aling_x-30, align_y + 0.90*align_y, "Un error cualquier de pruebita", font_size=30, color=(255, 50, 50))

        self.__clock = pygame.time.Clock()
        self.__debug_mode = False

    def start(self):
        # name1 = input("Ingrese el nombre del jugador 1 (fichas negras): ")
        # name2 = input("Ingrese el nombre del jugador 2 (fichas blancas): ")
        self.__backgammon.with_players("joaco", "jero")
        result = self.__backgammon.start_game()
        self.run()

    def set_msg_state(self):
        actual_player = self.__backgammon.actual_player()
        bar = self.__backgammon.get_bar_state()
        won_checkers = self.__backgammon.get_won_checkers()
        p1, p2 = self.__backgammon.get_players()

        msj = f"Turno de: {actual_player.get_name()}, {actual_player.get_color()}"
        self.__turn_msg.set_content(msj)

        msj = f"Bar: {black} {bar[black]}, {white} {bar[white]}"
        self.__bar_msg.set_content(msj)

        msj = f"Puntos: {p1.get_name()} {won_checkers[p1]}, {p2.get_name()} {won_checkers[p2]}"
        self.__won_checkers_msg.set_content(msj)


    def run(self):
        while self.__running and self.__backgammon.get_winner() is None:
            try:
                self.handle_events()
            except Exception as e:
                self.__error_msg.set_content(str(e))

            # Limpia la pantalla
            self.__screen.fill((255, 255, 255))
            self.__screen.blit(self.__bg_image, (0, 0))

            # Renderiza las fichas en los points
            self.__point_manager.render_all_points(self.__backgammon.get_board_state())
            self.__point_manager.render_selection_highlight()
            if self.__debug_mode:
                self.__point_manager.debug_render()
            # Renderiza las fichas en el bar


            # Muestra los dados
            self.__dice.render(self.__backgammon.get_dice_values(), self.__backgammon.get_used_dice())
            #Renderizar textos
            self.set_msg_state()
            self.__title.render(self.__screen)
            self.__turn_msg.render(self.__screen)
            self.__bar_msg.render(self.__screen)
            self.__won_checkers_msg.render(self.__screen)
            self.__error_msg.render(self.__screen)

            # Actualiza la pantalla
            pygame.display.update()
            self.__clock.tick(60)

        if self.__backgammon.get_winner() is None:
            print("Adios!!")
        else:
            self.show_winner()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.handle_points(mouse_pos)
                self.handle_dice(mouse_pos)

            if event.type == pygame.KEYDOWN:
                self.handle_key_event(event)
        self.handle_turn()

    def handle_turn(self):
        if self.__backgammon.is_checker_on_bar():
            self.__point_manager.lock_selection()
            self.turn_from_bar()
        else:
            self.__point_manager.unlock_selection()
            self.turn()

        if self.__backgammon.is_all_dice_used():
            self.__backgammon.next_turn()
            self.__backgammon.trow_dice()

    def turn_from_bar(self):
        if not self.__dice.is_dice_selected():
            return
        self.__backgammon.move_from_bar(self.__dice.get_selected_dice())
        self.__dice.clear_selection()

    def turn(self):
        if not self.__point_manager.is_point_selected():
            return
        if not self.__dice.is_dice_selected():
            return
        self.__backgammon.move(self.__point_manager.get_selected_point(), self.__dice.get_selected_dice())
        self.__dice.clear_selection()
        self.__point_manager.clear_selection()

    def handle_points(self, mouse_pos: tuple[int, int]):
        point_clicked = self.__point_manager.detect_clicked_point(mouse_pos)
        if point_clicked is not None:
            point = self.__backgammon.get_board_state()[point_clicked-1]
            player_color = self.__backgammon.actual_player().get_color()
            if point.get_color() != player_color:
                raise Exception("No puedes seleccionar un punto que no tiene tus fichas")
            self.__point_manager.select_point(point_clicked)

    def handle_dice(self, mouse_pos: tuple[int, int]):
        dice_clicked = self.__dice.detect_click_dice(mouse_pos)
        if dice_clicked is not None:
            print(f"Dice clicked: {dice_clicked}")

    def handle_key_event(self, event: pygame.event):
        if event.key == pygame.K_d:
            self.__debug_mode = not self.__debug_mode
            print(f"Debug mode: {self.__debug_mode}")
        if event.key == pygame.K_o:
            print("Pasando turno...")
            self.__backgammon.next_turn()
            self.__backgammon.trow_dice()

    def show_winner(self):
        print("El ganador es ...")
