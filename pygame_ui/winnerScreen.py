class WinnerScreen():
    def __init__(self, screen, winner_text):
        self.screen = screen
        self.font = font
        self.winner_text = winner_text

    def display_winner(self):
        self.screen.fill((0, 0, 0))  # Clear screen with black
        text_surface = self.font.render(self.winner_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text_surface, text_rect)
        pygame.display.flip()  # Update the display

