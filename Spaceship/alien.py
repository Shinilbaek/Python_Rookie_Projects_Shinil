import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """class of an alien"""

    def __init__(self,ai_settings,screen):
        """initialize an alien"""
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_setttings = ai_settings

        #load alien's image and set its rect prop
        self.image = pygame.image.load('Spaceship/images/alien.bmp')
        self.rect = self.image.get_rect()

        #initialize alien's position near (0,0)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store alien's accurate position
        self.x = float(self.rect.x)

    def blitme(self):
        """draw an aliena at given position"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """move aliens to the right"""
        self.x += self.ai_setttings.alien_speed_factor
        self.rect.x = self.x


    def check_edges(self):
        """if an alien touches the edge, then return True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True 
    

    def update(self):
        """move an alien to the left or right"""
        self.x += (self.ai_setttings.alien_speed_factor *
                    self.ai_setttings.fleet_direction)
        self.rect.x = self.x

    