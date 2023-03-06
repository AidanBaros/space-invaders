from __future__ import annotations
import pygame
from barrier import Barrier
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from enemy import Enemy

class Projectile:
    image:pygame.surface.Surface
    def __init__(self, xpos, ypos, size_multiplyer, screen: pygame.surface.Surface,god_mode=False):
        self.screen = screen
        self.screensize = screen.get_size()
        self.xpos = xpos
        self.ypos = ypos
        self.size_multiplyer = size_multiplyer
        self.x_size = 8 * self.size_multiplyer
        self.y_size = 20 * self.size_multiplyer
        self.is_alive = True
        self.speed = 7
        self.hitbox = pygame.Rect(self.xpos,self.ypos,self.x_size,self.y_size)
        if god_mode:
            self.speed = 30


    def draw(self):
        #pygame.draw.rect(self.screen,"red",(self.hitbox))
        self.screen.blit(self.image,self.hitbox)

    def move(self):
        pass

    def collision(self):
        pass
        

    def update(self):
        pass



class Player_bullet(Projectile):
    def __init__(self, xpos, ypos, size_multiplyer, screen: pygame.surface.Surface, god_mode):
        super().__init__(xpos, ypos,size_multiplyer, screen, god_mode)
        self.image = pygame.transform.scale(pygame.image.load(f"invaders_imgs/player_shot.png"),(self.x_size,self.y_size))

    def collision(self, list_of_enemies:list[Enemy], list_of_barriers:list[Barrier]):
        score = 0
        if self.hitbox.centery <= 0:
            self.is_alive = False
            #print("edge")
        for i, bad_guy in enumerate(list_of_enemies):
            if self.hitbox.colliderect(bad_guy.hitbox):
                self.is_alive = False
                if bad_guy.type == 1:
                    score = 10
                elif bad_guy.type == 2:
                    score = 20
                elif bad_guy.type == 3:
                    score = 40
                list_of_enemies.pop(i)
                #print("bad_guy")
        for i, barrier in enumerate(list_of_barriers):
            if self.hitbox.colliderect(barrier.hitbox):
                self.is_alive = False
                if barrier.health != 1:
                    barrier.health -=1
                else:
                    list_of_barriers.pop(i)
                #print("wall")
        return score

    def move(self):
        if self.is_alive:
            self.ypos -= self.speed * self.size_multiplyer
            self.hitbox.centery = round(self.ypos)
        else:
            self.xpos = -1000
            self.ypos = -1000
    
    def update(self, list_of_enemies, list_of_barriers):
        score = self.collision(list_of_enemies, list_of_barriers)
        self.move()
        self.draw()
        return self.is_alive, score


class Enemy_bullet(Projectile):
    def __init__(self, xpos, ypos, size_multiplyer, screen: pygame.surface.Surface,):
        super().__init__(xpos, ypos, size_multiplyer, screen,)
        self.image = pygame.transform.scale(pygame.image.load(f"invaders_imgs/enemy_shot_1.png"),(self.x_size,self.y_size))
    
    def collision(self, player, list_of_barriers:list[Barrier]):
        if self.hitbox.centery >= self.screensize[1]:
            self.is_alive = False
            #print("edge")
        if self.hitbox.colliderect(player.hitbox):
            self.is_alive = False
            player.alive = False
            #print("player")
        for i, barrier in enumerate(list_of_barriers):
            if self.hitbox.colliderect(barrier.hitbox):
                self.is_alive = False
                if barrier.health != 1:
                    barrier.health -=1
                else:
                    list_of_barriers.pop(i)
                #print("wall")

    def move(self):
        if self.is_alive:
            self.ypos += self.speed * self.size_multiplyer
            self.hitbox.centery = round(self.ypos)
        else:
            self.xpos = -1000
            self.ypos = -1000

    def update(self, player_hitbox, list_of_barriers):
        self.collision(player_hitbox, list_of_barriers)
        self.move()
        self.draw()
        return self.is_alive
