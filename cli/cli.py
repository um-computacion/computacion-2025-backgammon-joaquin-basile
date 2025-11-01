from core.backgammon import Backgammon
from core.const import black, white
from time import sleep
from core.exceptions import OmitTurn

class CLI:
    '''
    Interfaz del juego por linea de comandos
    '''
    def __init__(
            self, 
            backgammon: Backgammon = Backgammon()
        ):
        self.__backgammon = backgammon

    def start_cli(self):
        try:
            print("Iniciando el juego de Backgammon...")
            name1 = input("Elegir el nombre jugador negro: ")
            name2 = input("Elegir el nombre jugador blanco: ")
            self.__backgammon.with_players(name1, name2)
            print("Se estan girando los dados para decidir quien comienza...")
            sleep(1.2)
            result, starter = self.__backgammon.start_game()
            for v in result:
                sleep(1)
                print(v , "saco ", result[v])

            while self.__backgammon.get_winner() is None:
                sleep(1)
                player = self.__backgammon.actual_player()
                self.__backgammon.trow_dice()
                self.turn()
                self.__backgammon.next_turn()

            print(f"Gano {self.__backgammon.get_winner().get_name()}")

        except KeyboardInterrupt:
            print("\nSe termino el juego!")

    def turn(self):
        self.display_board()
        try:
            if self.__backgammon.is_checker_on_bar():
                self.turn_whith_bar()
            else:
                self.turn_whithout_bar()
        except Exception as e:
            print(e)
            if input("Desea omitir el turno? (s/n): ").lower() == 's':
                return

        if not self.__backgammon.is_all_dice_used():
            self.turn()

    def turn_whithout_bar(self):
        pos = int(input("Que ficha mover (ingresar punto 1-24): "))
        dice_to_use = int(input("Que dado usar (1 o 2): "))
        self.__backgammon.move(pos, dice_to_use)
    
    def turn_whith_bar(self):   
        print("Tienes fichas en el bar!!")
        dice_to_use = int(input("Que dado usar (1 o 2): "))
        self.__backgammon.move_from_bar(dice_to_use)

    def display_board(self):
        points = self.__backgammon.get_board_state()
        bar = self.__backgammon.get_bar_state()

        # Símbolos para las fichas
        symbols = {black: '●', white: '○'}

        print("\n" + "="*70)
        print("                      TABLERO DE BACKGAMMON")
        print("="*70)

        print()
        print(" 13  14  15  16  17  18        19  20  21  22  23  24")
        print("┌───┬───┬───┬───┬───┬───┐ BAR ┌───┬───┬───┬───┬───┬───┐")

        for row in range(10):
            line = "│"
            for i in range(12, 18):
                point = points[i]
                if point.get_quantity() > row:
                    symbol = symbols.get(point.get_color(), ' ')
                    line += f" {symbol} │"
                else:
                    line += "   │"

            # Bar
            if row == 2:
                bar_display = f" {symbols[black]}{bar[black]}  "
            elif row == 3:
                bar_display = f" {symbols[white]}{bar[white]}  "
            else:
                bar_display = "     "
            line += bar_display

            line += "│"
            for i in range(18, 24):
                point = points[i]
                if point.get_quantity() > row:
                    symbol = symbols.get(point.get_color(), ' ')
                    line += f" {symbol} │"
                else:
                    line += "   │"
            print(line)

        print("│   │   │   │   │   │   │     │   │   │   │   │   │   │")
        print("├───┴───┴───┴───┴───┴───┤     ├───┴───┴───┴───┴───┴───┤")
        print("│   │   │   │   │   │   │     │   │   │   │   │   │   │")

        for row in range(9, -1, -1):
            line = "│"
            for i in range(11, 5, -1):
                point = points[i]
                if point.get_quantity() > row:
                    symbol = symbols.get(point.get_color(), ' ')
                    line += f" {symbol} │"
                else:
                    line += "   │"

            line += "     "

            line += "│"
            for i in range(5, -1, -1):
                point = points[i]
                if point.get_quantity() > row:
                    symbol = symbols.get(point.get_color(), ' ')
                    line += f" {symbol} │"
                else:
                    line += "   │"
            print(line)

        print("└───┴───┴───┴───┴───┴───┘     └───┴───┴───┴───┴───┴───┘")
        print(" 12  11  10   9   8   7         6   5   4   3   2   1")

        # Leyenda
        print("\n" + "-"*70)
        print(f"Leyenda: {symbols[black]} = Negro (bk) ->  |  {symbols[white]} = Blanco (wh) <-")
        print(f"BAR: Negro {symbols[black]} = {bar[black]}  |  Blanco {symbols[white]} = {bar[white]}")
        actual_player = self.__backgammon.actual_player()
        print(f"Turno de {actual_player.get_name()}, {actual_player.get_color()}")
        print(f"Dados disponibles: ")
        dices = self.__backgammon.get_dice_values()
        used = self.__backgammon.get_used_dice()
        if not used[0]:
            print(f"1: {dices[0]}")
        if not used[1]:
            print(f"2: {dices[1]}")

        print("="*70 + "\n")
