import pygame

class Enemy():
    image:pygame.surface.Surface
    def __init__(
            self,
            pos: tuple[float,float], 
            size_multiplyer:float,):
        self.alive = True
        self.screen = pygame.display.get_surface()

        self.screenSize = pygame.display.get_window_size()

        self.xpos = pos[0]
        self.ypos = pos[1]

        self.x_size = 64*size_multiplyer
        self.y_size = 64*size_multiplyer

        self.hitbox = pygame.Rect(self.xpos, self.ypos, self.x_size,self.y_size)
        self.distancebox = (80,80)

        self.list_of_enemies:list[Enemy] = []

        self.direction = 1

        self.size_multiplyer = size_multiplyer

        self.speed = 0
        
        self.check_y_move = False

    def get_list(self,list_of_enemies):
        self.list_of_enemies = list_of_enemies

    def draw(self):
        self.hitbox.x = int(self.xpos)
        self.hitbox.y = int(self.ypos)
        self.screen.blit(self.image,self.hitbox)

    def collide(self, projectile:pygame.Rect, enemyList, Listposition, position):
        if projectile.colliderect(self.hitbox):
            self.alive = False

    def edge_collide(self):
        if self.xpos >= self.screenSize[0] - 128*self.size_multiplyer:
            for enemy in self.list_of_enemies:
                enemy.direction = 1
                enemy.check_y_move = True
        elif self.xpos <= 64*self.size_multiplyer:
            for enemy in self.list_of_enemies:
                enemy.direction = -1
                enemy.check_y_move = True

    def move(self):
        if self.speed == 0:
            self.speed = 10
            self.xpos -= (8*self.size_multiplyer)*self.direction
            if self.check_y_move == True:
                self.ypos += 32*self.size_multiplyer
                self.check_y_move = False
        else:
            self.speed -= 1


    
    def update(self):
        #self.collide()
        self.move()
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