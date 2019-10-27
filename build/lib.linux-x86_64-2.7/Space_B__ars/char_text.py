import pygame
import variables
class char_text:
    r=None
    textrect=None
    text=None
    def __init__(self, rep):
        self.r = '_' if rep==' ' else rep
        basicfont = pygame.font.SysFont(None, (variables.screen_max_y)//10)
        self.text = basicfont.render(self.r, True, (0, 255, 250))
        self.textrect = self.text.get_rect()
        self.textrect.centerx = -50 if variables.dirn else (variables.screen_max_x+50)
        self.textrect.centery = variables.screen_max_y//4 + variables.screen_max_y//8
    
    def update_screen(self, screen):
        screen.blit(self.text, self.textrect)
        
    def update_pos(self):
        self.textrect.centerx=self.textrect.centerx+7 if variables.dirn else (self.textrect.centerx-7)

    def __del__(self):
        self.textrect=None
        self.r=None
        self.text=None
