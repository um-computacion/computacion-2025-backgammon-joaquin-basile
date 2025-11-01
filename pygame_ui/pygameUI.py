import pygame

class PygameUI:
    '''
    Interfaz grafica para el juego
    '''
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1500, 1300))
        self.bg_image = pygame.image.load('./assets/board.png')
        self.bg_image = pygame.transform.scale(self.bg_image, self.screen.get_size()).convert()
        self.clock = pygame.time.Clock()
        self.running = True
        self.points = []

        self.checker_radius = 30  
        self.w_checker = self.create_checker((255, 255, 255))  
        self.b_checker = self.create_checker((50, 50, 50))
    
    def create_checker(self, color):
        size = self.checker_radius * 2
        surface = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(surface, color, (self.checker_radius, self.checker_radius), self.checker_radius)
        pygame.draw.circle(surface, (0, 0, 0), (self.checker_radius, self.checker_radius), self.checker_radius, 2)
        return surface

    def detect_point(self, mouse_pos, board_width, board_height):
        x, y = mouse_pos
        margin_h_percentage = 0.05
        margin_v_percentage = 0.05   
        horizontal_margin = board_width * margin_h_percentage
        vertical_margin = board_height * margin_v_percentage
        
        adjusted_x = x - horizontal_margin
        adjusted_y = y - vertical_margin
        
        play_width = board_width - (2 * horizontal_margin)
        play_height = board_height - (2 * vertical_margin)
        
        if adjusted_x < 0 or adjusted_x > play_width or adjusted_y < 0 or adjusted_y > play_height:
            return None
        
        bar_width = play_width * 0.06  # For example, 6% of width
        
        points_width = play_width - bar_width
        point_width = points_width / 12
        
        left_half = points_width / 2
        
        if adjusted_x < left_half:
            column = int(adjusted_x / point_width)
        elif adjusted_x < left_half + bar_width:
            return "bar"
        else:
            right_x = adjusted_x - left_half - bar_width
            column = 6 + int(right_x / point_width)
        
        if column < 0 or column > 11:
            return None
        
        if adjusted_y < play_height / 2:
            return 13 + column
        else:
            return 12 - column

    def run(self):
        while self.running:
            self.handle_events()

            # Do logical updates here.
            # ...

            self.screen.blit(self.bg_image, (0, 0))

            # Render the graphics here.
            # ...

            pygame.display.update()  # Refresh on-screen display
            self.clock.tick(60)     # wait until next frame (at 60 FPS)

    def print_points(self):
            size = self.screen.get_size()
            mouse = pygame.mouse.get_pos()
            casilla = self.detect_point(mouse, size[0], size[1])
            print(casilla)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONUP:
                self.print_points()
