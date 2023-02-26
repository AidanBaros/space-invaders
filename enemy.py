import pygame

class Enemy():
    def __init__(
            self,
            pos: tuple[int,int], 
            size_multiplyer,):
        self.alive = True
        self.screen = pygame.display.get_surface()

        self.screenSize = pygame.display.get_window_size()

        self.pos:tuple[int,int] = pos

        self.x_size = 64*size_multiplyer
        self.y_size = 64*size_multiplyer

        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], self.x_size,self.y_size)
        self.distancebox = (80,80)

        self.image:pygame.image = None


    def draw(self):
        self.screen.blit(self.image,self.hitbox)

    def collide(self, projectile:pygame.Rect, enemyList, Listposition, position):
        if projectile.colliderect(self.hitbox):
            self.alive = False

    def move(self):
        pass
    
    def update(self):
        pass

class Skull(Enemy):
    def __init__(self,
            pos: tuple[int,int], 
            size_multiplyer,):
        super().__init__(pos: tuple[int,int], size_multiplyer)
        self.image = pygame.transform.scale(pygame.image.load(f"invaders_imgs/yellow_1.png"),(self.x_size,self.y_size))

class Crab(Enemy):
    def __init__(self,
            pos: tuple[int,int], 
            size_multiplyer,):
        super().__init__(pos: tuple[int,int], size_multiplyer)
        self.image = pygame.transform.scale(pygame.image.load(f"invaders_imgs/orange_1.png"),(self.x_size,self.y_size))

class Octo(Enemy):
    def __init__(self,
            pos: tuple[int,int], 
            size_multiplyer,):
        super().__init__(pos: tuple[int,int], size_multiplyer)
        self.image = pygame.transform.scale(pygame.image.load(f"invaders_imgs/red_1.png"),(self.x_size,self.y_size))

"""class UFO(Enemy):
    def __init__(self):
        super().__init__()"""