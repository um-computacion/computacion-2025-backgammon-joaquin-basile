import pygame

class Dice():
    def __init__(self, screen: pygame.Surface, pos_dice: tuple[int, int]):
        self.__screen = screen
        self.__dice1_img = pygame.transform.scale(pygame.image.load('./assets/dice/1.png'), (60, 60)).convert()
        self.__dice2_img = pygame.transform.scale(pygame.image.load('./assets/dice/2.png'), (60, 60)).convert()
        self.__dice3_img = pygame.transform.scale(pygame.image.load('./assets/dice/3.png'), (60, 60)).convert()
        self.__dice4_img = pygame.transform.scale(pygame.image.load('./assets/dice/4.png'), (60, 60)).convert()
        self.__dice5_img = pygame.transform.scale(pygame.image.load('./assets/dice/5.png'), (60, 60)).convert()
        self.__dice6_img = pygame.transform.scale(pygame.image.load('./assets/dice/6.png'), (60, 60)).convert()

        self.__dice1_pos = (pos_dice[0], pos_dice[1] + 65)
        self.__dice2_pos = (pos_dice[0], pos_dice[1])

        self.__dice_surface: list[pygame.Surface] = [None, None]
        self.__selected_dice: int = None 
        
    def set_pos(self, pos_dice: tuple[int, int]):
        self.__dice1_pos = (pos_dice[0], pos_dice[1] + 65)
        self.__dice2_pos = (pos_dice[0], pos_dice[1])

    def highlight_surface(self, surface, color=(255, 255, 0), alpha=50):
        """Añade un efecto de brillo a una surface"""
        highlighted = surface.copy()
        overlay = pygame.Surface(surface.get_size())
        overlay.fill(color)
        overlay.set_alpha(alpha)
        highlighted.blit(overlay, (0, 0))
        return highlighted

    def set_dice_values(self, dice: list[int]):
        for k, d in enumerate(dice):
            if d == 1:
                self.__dice_surface[k] = self.__dice1_img
            elif d == 2:
                self.__dice_surface[k] = self.__dice2_img
            elif d == 3:
                self.__dice_surface[k] = self.__dice3_img
            elif d == 4:
                self.__dice_surface[k] = self.__dice4_img
            elif d == 5:
                self.__dice_surface[k] = self.__dice5_img
            else:
                self.__dice_surface[k] = self.__dice6_img

    def get_dice_pos(self, dice_number: int) -> tuple[int, int]:
        return self.__dice1_pos if dice_number == 1 else self.__dice2_pos

    def render(self, dice: list[int], used: tuple[bool, bool]):
        if dice is not None:
            self.set_dice_values(dice)

        if not used[0]:
            if self.__selected_dice == 1:
                self.__screen.blit(self.highlight_surface(self.__dice_surface[0]), self.__dice1_pos)
            else:
                self.__screen.blit(self.__dice_surface[0], self.__dice1_pos)

        if not used[1]:
            if self.__selected_dice == 2:
                self.__screen.blit(self.highlight_surface(self.__dice_surface[1]), self.__dice2_pos)
            else:
                self.__screen.blit(self.__dice_surface[1], self.__dice2_pos)

    def detect_click_dice(self, mouse_pos):
        """
        Detecta sobre que dado se hizo click y devuelve el numero de dado o None
        """
        t1, l1 = self.get_dice_pos(1)
        t2, l2 = self.get_dice_pos(2)
        dice1_rect = pygame.Rect(t1, l1, 60, 60)
        dice2_rect = pygame.Rect(t2, l2, 60, 60)
        
        if dice1_rect.collidepoint(mouse_pos):
            self.toggle_selected_dice(1)
        elif dice2_rect.collidepoint(mouse_pos):
            self.toggle_selected_dice(2)

    def toggle_selected_dice(self, dice_number: int):
        if self.__selected_dice == dice_number:
            self.__selected_dice = None
        else:
            self.__selected_dice = dice_number

    def get_selected_dice(self):
        return self.__selected_dice

    def is_dice_selected(self):
        return self.__selected_dice is not None 

    def clear_selection(self):
        """Deselecciona cualquier punto seleccionado."""
        self.__selected_dice = None
    




