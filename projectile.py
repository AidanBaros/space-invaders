import pygame

class Projectile:
    image:pygame.surface.Surface
    def __init__(self, xpos, ypos, size_multiplyer):
        self.xpos = xpos
        self.ypos = ypos
        self.size_multiplyer = size_multiplyer
        self.x_size = 8 * self.size_multiplyer
        self.y_size = 20 * self.size_multiplyer
        self.isAlive = False
        self.speed = 0



class Player_bullet(Projectile):
    def __init__(self, xpos, ypos, size_multiplyer):
        super().__init__(xpos, ypos,size_multiplyer)
        self.image = pygame.transform.scale(pygame.image.load(f"invaders_imgs/player_shot.png"),(self.x_size,self.y_size))


class Enemy_bullet(Projectile):
    def __init__(self, xpos, ypos, size_multiplyer):
        super().__init__(xpos, ypos, size_multiplyer)
        self.image = pygame.transform.scale(pygame.image.load(f"invaders_imgs/enemy_shot_1.png"),(self.x_size,self.y_size))
