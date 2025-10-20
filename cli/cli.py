from core.backgammon import Backgammon
from core.const import black, white

class CLI:
    '''
    Interfaz del juego por linea de comandos
    '''
    def __init__(self):
        self.__backgammon = Backgammon()

    def start_cli(self):
        try:
            print("Iniciando el juego de Backgammon...")
            name1 = input("Elegir el nombre jugador negro: ")
            name2 = input("Elegir el nombre jugador blanco: ")
            self.__backgammon.with_players(name1, name2)
            print("Se estan girando los dados para decidir quien comienza...")
            result, starter = self.__backgammon.start_game()
            print("Los resultados fueron: ", result)
            print("El jugador ", starter.get_name(), " comienza!!")

            while not self.__backgammon.end_game():
                print("Se estan tirando los dados...")
                dados = self.__backgammon.trow_dice()
                print("Primer dado: ", dados[0])
                print("Segundo dado: ", dados[1])
                for i in range(2):
                    self.display_board()
                    pos = int(input("Que ficha mover: ")) - 1
                    dado = int(input("Que dado usar: "))
                    self.__backgammon.move(pos, dado)


        except KeyboardInterrupt:
            print("\nSe termino el juego!")

    def display_board(self):
        points = self.__backgammon.get_board_state()
        bar = self.__backgammon.get_bar_state()

        # Símbolos para las fichas
        symbols = {black: '●', white: '○'}

        print("\n" + "="*70)
        print("                      TABLERO DE BACKGAMMON")
        print("="*70)

        # Parte superior del tablero (puntos 12-23)
        print("\n  13  14  15  16  17  18        19  20  21  22  23  24")
        print("┌───┬───┬───┬───┬───┬───┐ BAR ┌───┬───┬───┬───┬───┬───┐")

        # Mostrar fichas en la parte superior (máximo 5 filas visibles)
        for row in range(10):
            line = "│"
            for i in range(12, 18):
                point = points[i]
                if point.get_quantity() > row:
                    symbol = symbols.get(point.get_color(), ' ')
                    line += f" {symbol} │"
                else:
                    line += "   │"

            # Barra
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

        # Mostrar fichas en la parte inferior (máximo 5 filas visibles)
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
        print("  12  11  10   9   8   7        6   5   4   3   2   1")

        # Leyenda
        print("\n" + "-"*70)
        print(f"Leyenda: {symbols[black]} = Negro (bk)  |  {symbols[white]} = Blanco (wh)")
        print(f"BAR: Negro {symbols[black]} = {bar[black]}  |  Blanco {symbols[white]} = {bar[white]}")
        print("="*70 + "\n")
