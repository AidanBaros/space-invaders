import pygame

class Enemy():
    def __init__(self,):
        self.alive = True
        self.screen = pygame.display.get_surface()

        self.screenSize = pygame.display.get_window_size()

        self.pos = ()

        self.hitbox = (64,64)
        self.distancebox = (80,80)


    def draw(self):
        pass

    def collide(self, projectile:pygame.Rect, enemyList, Listposition, position):
        if projectile.colliderect(self.hitbox):
            self.alive = False
        
        

class skull(Enemy):
    def __init__(self):
        super().__init__()

class crab(Enemy):
    def __init__(self):
        super().__init__()

class octo(Enemy):
    def __init__(self):
        super().__init__()

class sauser(Enemy):
    def __init__(self):
        super().__init__()