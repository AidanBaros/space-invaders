import pygame
from projectile import *


class Player:
    def __init__(
        self,
        screen: pygame.surface.Surface,
        screenSize: tuple[int, int],
        size_multiplyer,
        god_mode:bool,
    ):
        self.screen = screen
        self.screenSize = screenSize
        self.size_multiplyer = size_multiplyer
        self.player_x = 64*self.size_multiplyer
        self.player_y = 64*self.size_multiplyer
        self.rect = pygame.Rect(self.screenSize[0] // 2 - (self.player_x/2), self.screenSize[1] - (100*self.size_multiplyer + self.player_x), self.player_x, self.player_y)
        self.hitbox = self.rect.copy()
        self.image = pygame.transform.scale(pygame.image.load(f"invaders_imgs/player.png"),(self.player_x,self.player_y))
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 5
        self.alive = True
        self.lives = 3
        self.did_shoot = False
        self.shot_alive = True
        self.god_mode = god_mode

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.hitbox.left >= 0:
            self.direction.x = -1
            # self.status = "left"
        elif keys[pygame.K_d] and self.hitbox.right <= self.screenSize[0]:
            self.direction.x = 1
            # self.status = "right"
        else:
            self.direction.x = 0

        if keys[pygame.K_w]:
            self.shoot()

    def move(self):
        self.pos.x += self.direction.x * self.speed * self.size_multiplyer
        self.hitbox.centerx = round(self.pos.x)
        self.rect.centerx = self.hitbox.centerx

    def draw(self):
        #pygame.draw.rect(self.screen, (255, 0, 0), self.rect)
        self.screen.blit(self.image,self.rect)

    def shoot(self):
        if self.did_shoot == False:
            self.did_shoot = True
            self.shot = Player_bullet(self.pos[0],self.pos[1],self.size_multiplyer,self.screen, self.god_mode)

    def update(self, list_of_enemies, list_of_barriers):
        score = 0
        if self.did_shoot:
            self.shot_alive, score = self.shot.update(list_of_enemies,list_of_barriers)
            if self.shot_alive == False:
                self.did_shoot = False
        self.input()
        self.move()
        self.draw()
        return score
