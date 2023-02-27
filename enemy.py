import pygame

class Enemy():
    image:pygame.surface.Surface
    def __init__(
            self,
            pos: tuple[float,float], 
            size_multiplyer,):
        self.alive = True
        self.screen = pygame.display.get_surface()

        self.screenSize = pygame.display.get_window_size()

        self.pos:tuple[float,float] = pos

        self.x_size = 64*size_multiplyer
        self.y_size = 64*size_multiplyer

        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], self.x_size,self.y_size)
        self.distancebox = (80,80)

        self.list_of_enemies:list[list[Enemy]] = []

        self.direction = 1

    def get_list(self,list_of_enemies):
        self.list_of_enemies = list_of_enemies

    def draw(self):
        self.screen.blit(self.image,self.hitbox)

    def collide(self, projectile:pygame.Rect, enemyList, Listposition, position):
        if projectile.colliderect(self.hitbox):
            self.alive = False

    def move(self):
        can_move = True
        if self.direction == 1:
            row_num = 0
            for j in range(10,-1,-1):
                for i in range(5):
                    if self.list_of_enemies[i][-1].alive == True:
                        row_num = j
                        break# just delete the enemies adn make it one list
                pass
    
    def update(self):
        #self.collide()
        self.draw()

class Skull(Enemy):
    def __init__(self,
            pos: tuple[float,float], 
            size_multiplyer,):
        super().__init__(pos, size_multiplyer)
        self.image = pygame.transform.scale(pygame.image.load(f"invaders_imgs/yellow_1.png"),(self.x_size,self.y_size))

class Crab(Enemy):
    def __init__(self,
            pos: tuple[float,float], 
            size_multiplyer,):
        super().__init__(pos, size_multiplyer)
        self.image = pygame.transform.scale(pygame.image.load(f"invaders_imgs/orange_1.png"),(self.x_size,self.y_size))

class Octo(Enemy):
    def __init__(self,
            pos: tuple[float,float], 
            size_multiplyer,):
        super().__init__(pos, size_multiplyer)
        self.image = pygame.transform.scale(pygame.image.load(f"invaders_imgs/red_1.png"),(self.x_size,self.y_size))

"""class UFO(Enemy):
    def __init__(self):
        super().__init__()"""