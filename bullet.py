import pygame
from pygame.sprite import Sprite

#a class to manange bullet fired from the ship
class Bullet(Sprite):

    def __init__(self,ai_settings,screen,ship):
        #create a bullet object at ships current position
        super().__init__()
        self.screen=screen

        #create a bullet rect at (0,0) and set its current position
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        #setting the bullets same position as that of ship
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top

        #storingbullets position as decimal so as to amke fine adjustments in speed
        self.y=float(self.rect.y)

        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor

    def update(self):
        #move the bullet up the screen
        #update the decimal position of ship
        self.y-=self.speed_factor
        #update the rect position
        self.rect.y=self.y

    def draw_bullet(self):
        #draw the bullet to the screen
        pygame.draw.rect(self.screen,self.color,self.rect)
        

