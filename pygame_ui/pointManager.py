import pygame
from pygame_ui.point import Point
from core.point import Point as CorePoint

class PointManager:
    """
    Manages all 24 points on the backgammon board.
    """
    def __init__(self, screen: pygame.Surface, board_width: int, board_height: int, scale: float = 1.0):
        self.__screen = screen
        self.__board_width = board_width
        self.__board_height = board_height
        self.__points: list[Point] = []
        self.__selected_point: int | None = None  # Punto seleccionado (1-24)
        self.__block_pressed: bool = False 
        self.__scale = scale
        self.__initialize_points()
    
    def __initialize_points(self):
        """
        Create all 24 points with their positions on the board.
        
        Board layout (based on your image):
        Top:    13 14 15 16 17 18 | BAR | 19 20 21 22 23 24
        Bottom: 12 11 10  9  8  7 | BAR |  6  5  4  3  2  1
        """

        # Configuración del tablero - AJUSTA ESTOS VALORES según tu imagen
        margin_left = 37.5 * self.__scale        # Margen izquierdo (zona beige)
        margin_right = 37.5 * self.__scale       # Margen derecho
        margin_top = 37.5 * self.__scale       # Margen superior
        margin_bottom = 35 * self.__scale      # Margen inferior
        bar_width = 31.5 * self.__scale          # Ancho de la barra central (zona roja oscura)
        point_width_reduction = 0 * self.__scale # Reducir el ancho de cada point
        
        # Calcular el ancho disponible para cada mitad del tablero
        total_width = self.__board_width - margin_left - margin_right - bar_width
        half_width = total_width // 2  # Ancho de cada mitad (izquierda y derecha)
        
        # Cada mitad tiene 6 points
        point_width = (half_width // 6) - point_width_reduction
        
        # Altura de las agujas (triángulos)
        total_height = self.__board_height - margin_top - margin_bottom
        point_height = total_height // 2  # Mitad superior y mitad inferior
        
        # Calcular posición de inicio de cada sección
        left_section_start = margin_left
        right_section_start = margin_left + half_width + bar_width
        
        # LADO DERECHO INFERIOR: Points 1-5 (de derecha a izquierda)
        for i in range(6):
            left = right_section_start + (5 - i) * point_width + point_width_reduction * (5 - i)
            top = self.__board_height - margin_bottom - point_height
            point = Point(
                self.__screen,
                top=top,
                left=left,
                width=point_width,
                heigth=point_height,
                orientacion='bot',
                scale=self.__scale
            )
            self.__points.append(point)
        
        # LADO IZQUIERDO INFERIOR: Points 6-11 (de derecha a izquierda)
        for i in range(6):
            left = left_section_start + (5 - i) * point_width + point_width_reduction * (5 - i)
            top = self.__board_height - margin_bottom - point_height
            point = Point(
                self.__screen,
                top=top,
                left=left,
                width=point_width,
                heigth=point_height,
                orientacion='bot',
                scale=self.__scale
            )
            self.__points.append(point)
        
        # LADO IZQUIERDO SUPERIOR: Points 12-17 (de izquierda a derecha)
        for i in range(6):
            left = left_section_start + i * point_width + point_width_reduction * i
            top = margin_top
            point = Point(
                self.__screen,
                top=top,
                left=left,
                width=point_width,
                heigth=point_height,
                orientacion='top',
                scale=self.__scale
            )
            self.__points.append(point)
        
        # LADO DERECHO SUPERIOR: Points 18-23 (de izquierda a derecha)
        for i in range(6):
            left = right_section_start + i * point_width + point_width_reduction * i
            top = margin_top
            point = Point(
                self.__screen,
                top=top,
                left=left,
                width=point_width,
                heigth=point_height,
                orientacion='top',
                scale=self.__scale
            )
            self.__points.append(point)
    
    def get_point(self, index: int) -> Point:
        """Get a point by its number (1-24)"""
        if 0 <= index <= 23:
            return self.__points[index]
        return None
    
    def detect_clicked_point(self, mouse_pos: tuple[int, int]) -> int | None:
        """
        Detect which point was clicked.
        
        Args:
            mouse_pos: (x, y) position of mouse click
            
        Returns:
            Point number (1-24) or None if no point was clicked
        """
        if self.__block_pressed:
            return
        for i, point in enumerate(self.__points):
            if point.get_rect().collidepoint(mouse_pos):
                return i + 1  # Return 1-indexed point number
        return None
    
    def select_point(self, point_number: int | None):
        """
        Selecciona un punto específico.
        
        Args:
            point_number: Número del punto (1-24) o None para deseleccionar
        """
        if point_number is None:
            self.__selected_point = None
        elif 1 <= point_number <= 24:
            self.__selected_point = point_number
    
    def toggle_point_selection(self, point_number: int):
        """
        Alterna la selección de un punto. Si está seleccionado, lo deselecciona.
        Si no está seleccionado, lo selecciona.
        
        Args:
            point_number: Número del punto (1-24)
        """
        if self.__block_pressed:
            return
        if self.__selected_point == point_number:
            self.__selected_point = None
        else:
            self.__selected_point = point_number
    
    def get_selected_point(self) -> int | None:
        """
        Retorna el número del punto seleccionado actualmente.
        
        Returns:
            Número del punto (1-24) o None si no hay ninguno seleccionado
        """
        if self.__block_pressed:
            return None
        return self.__selected_point
    
    def is_point_selected(self,) -> bool:
        """
        Verifica si un punto específico está seleccionado.
        
        Args:
            point_number: Número del punto (1-24)
            
        Returns:
            True si el punto está seleccionado, False en caso contrario
        """
        return self.__selected_point is not None
    
    def clear_selection(self):
        """Deselecciona cualquier punto seleccionado."""
        self.__selected_point = None

    def lock_selection(self):
        self.__block_pressed = True 

    def unlock_selection(self):
        self.__block_pressed = False
    
    def render_point(self, point_number: int, quantity: int, color: str):
        """
        Render checkers on a specific point.
        
        Args:
            point_number: Point number (1-24)
            quantity: Number of checkers to render
            color: Color of checkers ('black' or 'white')
        """
        if 0 <= point_number <= 23:
            point = self.__points[point_number]
            point.render(quantity, color)
    
    def render_all_points(self, board_state: list[CorePoint]):
        """
        Render all points based on the board state.
        
        Args:
            board_state: Dictionary mapping point numbers to (quantity, color)
                        Example: {1: (2, 'white'), 6: (5, 'black'), ...}
        """
        for point_num, point in enumerate(board_state):
            if point.get_quantity() > 0:
                self.render_point(point_num, point.get_quantity(), point.get_color())
    
    def render_selection_highlight(self):
        """
        Renderiza un resaltado visual sobre el punto seleccionado.
        Debe llamarse después de render_all_points para que se vea sobre las fichas.
        """
        if self.__selected_point is None:
            return
        
        point = self.__points[self.__selected_point - 1]
        rect = point.get_rect()
        
        # Crear un borde brillante alrededor del punto seleccionado
        pygame.draw.rect(self.__screen, (255, 255, 0), rect, 4)  # Borde amarillo
        
        # Opcional: agregar un efecto de resplandor con transparencia
        highlight_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        highlight_surface.fill((255, 255, 0, 50))  # Amarillo semi-transparente
        self.__screen.blit(highlight_surface, (rect.left, rect.top))
    
    def debug_render(self):
        """
        Render semi-transparent rectangles over all points for debugging.
        Useful to visualize if points are positioned correctly.
        """
        for i, point in enumerate(self.__points):
            rect = point.get_rect()
            # Alternate colors for visibility
            color = (255, 0, 0, 100) if i % 2 == 0 else (0, 0, 255, 100)
            s = pygame.Surface((rect.width, rect.height))
            s.set_alpha(100)
            s.fill(color[:3])
            self.__screen.blit(s, (rect.left, rect.top))
            
            # Draw point number
            font = pygame.font.Font(None, 24)
            text = font.render(str(i + 1), True, (255, 255, 255))
            text_rect = text.get_rect(center=rect.center)
            self.__screen.blit(text, text_rect)

# import pygame
# from pygame_ui.point import Point
# from core.point import Point as CorePoint
#
# class PointManager:
#     """
#     Manages all 24 points on the backgammon board.
#     """
#     def __init__(self, screen: pygame.Surface, board_width: int, board_height: int):
#         self.__screen = screen
#         self.__board_width = board_width
#         self.__board_height = board_height
#         self.__points: list[Point] = []
#         self.__initialize_points()
#     
#     def __initialize_points(self):
#         """
#         Create all 24 points with their positions on the board.
#         
#         Board layout (based on your image):
#         Top:    13 14 15 16 17 18 | BAR | 19 20 21 22 23 24
#         Bottom: 12 11 10  9  8  7 | BAR |  6  5  4  3  2  1
#         """
#
#         # Configuración del tablero - AJUSTA ESTOS VALORES según tu imagen
#         margin_left = 75        # Margen izquierdo (zona beige)
#         margin_right = 70       # Margen derecho
#         margin_top = 75        # Margen superior
#         margin_bottom = 70      # Margen inferior
#         bar_width = 63          # Ancho de la barra central (zona roja oscura)
#         point_width_reduction = 0  # Reducir el ancho de cada point
#         
#         # Calcular el ancho disponible para cada mitad del tablero
#         total_width = self.__board_width - margin_left - margin_right - bar_width
#         half_width = total_width // 2  # Ancho de cada mitad (izquierda y derecha)
#         
#         # Cada mitad tiene 6 points
#         point_width = (half_width // 6) - point_width_reduction
#         
#         # Altura de las agujas (triángulos)
#         total_height = self.__board_height - margin_top - margin_bottom
#         point_height = total_height // 2  # Mitad superior y mitad inferior
#         
#         # Calcular posición de inicio de cada sección
#         left_section_start = margin_left
#         right_section_start = margin_left + half_width + bar_width
#         
#         # LADO DERECHO INFERIOR: Points 1-6 (de derecha a izquierda)
#         # Point 1 está en la esquina inferior derecha
#         for i in range(6):
#             left = right_section_start + (5 - i) * point_width + point_width_reduction * (5 - i)
#             top = self.__board_height - margin_bottom - point_height
#             point = Point(
#                 self.__screen,
#                 top=top,
#                 left=left,
#                 width=point_width,
#                 heigth=point_height,
#                 orientacion='bot'
#             )
#             self.__points.append(point)
#         
#         # LADO IZQUIERDO INFERIOR: Points 7-12 (de derecha a izquierda)
#         # Point 7 es el primero a la derecha de la barra, Point 12 el último a la izquierda
#         for i in range(6):
#             left = left_section_start + (5 - i) * point_width + point_width_reduction * (5 - i)
#             top = self.__board_height - margin_bottom - point_height
#             point = Point(
#                 self.__screen,
#                 top=top,
#                 left=left,
#                 width=point_width,
#                 heigth=point_height,
#                 orientacion='bot'
#             )
#             self.__points.append(point)
#         
#         # LADO IZQUIERDO SUPERIOR: Points 13-18 (de izquierda a derecha)
#         for i in range(6):
#             left = left_section_start + i * point_width + point_width_reduction * i
#             top = margin_top
#             point = Point(
#                 self.__screen,
#                 top=top,
#                 left=left,
#                 width=point_width,
#                 heigth=point_height,
#                 orientacion='top'
#             )
#             self.__points.append(point)
#         
#         # LADO DERECHO SUPERIOR: Points 19-24 (de izquierda a derecha)
#         for i in range(6):
#             left = right_section_start + i * point_width + point_width_reduction * i
#             top = margin_top
#             point = Point(
#                 self.__screen,
#                 top=top,
#                 left=left,
#                 width=point_width,
#                 heigth=point_height,
#                 orientacion='top'
#             )
#             self.__points.append(point)
#     
#     def get_point(self, index: int) -> Point:
#         """Get a point by its number (1-24)"""
#         if 1 <= index <= 24:
#             return self.__points[index - 1]
#         return None
#     
#     def detect_clicked_point(self, mouse_pos: tuple[int, int]) -> int | None:
#         """
#         Detect which point was clicked.
#         
#         Args:
#             mouse_pos: (x, y) position of mouse click
#             
#         Returns:
#             Point number (1-24) or None if no point was clicked
#         """
#         for i, point in enumerate(self.__points):
#             if point.get_rect().collidepoint(mouse_pos):
#                 return i + 1  # Return 1-indexed point number
#         return None
#     
#     def render_point(self, point_number: int, quantity: int, color: str):
#         """
#         Render checkers on a specific point.
#         
#         Args:
#             point_number: Point number (1-24)
#             quantity: Number of checkers to render
#             color: Color of checkers ('black' or 'white')
#         """
#         if 0 <= point_number <= 23:
#             point = self.__points[point_number]
#             point.render(quantity, color)
#     
#     def render_all_points(self, board_state: list[CorePoint]):
#         """
#         Render all points based on the board state.
#         
#         Args:
#             board_state: Dictionary mapping point numbers to (quantity, color)
#                         Example: {1: (2, 'white'), 6: (5, 'black'), ...}
#         """
#         for point_num, point in enumerate(board_state):
#             if point.get_quantity() > 0:
#                 self.render_point(point_num, point.get_quantity(), point.get_color())
#     
#     def debug_render(self):
#         """
#         Render semi-transparent rectangles over all points for debugging.
#         Useful to visualize if points are positioned correctly.
#         """
#         for i, point in enumerate(self.__points):
#             rect = point.get_rect()
#             # Alternate colors for visibility
#             color = (255, 0, 0, 100) if i % 2 == 0 else (0, 0, 255, 100)
#             s = pygame.Surface((rect.width, rect.height))
#             s.set_alpha(100)
#             s.fill(color[:3])
#             self.__screen.blit(s, (rect.left, rect.top))
#             
#             # Draw point number
#             font = pygame.font.Font(None, 24)
#             text = font.render(str(i + 1), True, (255, 255, 255))
#             text_rect = text.get_rect(center=rect.center)
#             self.__screen.blit(text, text_rect)
