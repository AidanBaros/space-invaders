import pygame
from enemy import *
from player import Player
from barrier import Barrier
from projectile import *


pygame.init()
pygame.display.set_caption("Space Invaders")
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screenSize = screen.get_size()
clock = pygame.time.Clock()
gameover = False
enemyList = []
projectileList = []

size_multiplyer = screenSize[0]/1920

list_of_barriers = []

player = Player(screen, screenSize, size_multiplyer)

bob = Crab((500,500),size_multiplyer)

def create_barriers():
    xpos = 281 * size_multiplyer
    ypos = screenSize[1] - 550
    for _ in range(4):
        for j in range(4):
            for i in range(4):
                if j == 0 and (i == 0 or i == 3):
                    pass
                elif j == 3 and (i == 1 or i == 2):
                    pass
                else:
                    list_of_barriers.append(Barrier(screen,(xpos + ((32*size_multiplyer)*i),ypos+((32*size_multiplyer)*j)),size_multiplyer))
        xpos += (281 * size_multiplyer) + (128*size_multiplyer)
            

create_barriers()
while not gameover: 
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LCTRL]:
            gameover = True


    screen.fill("black")
    player.update(size_multiplyer)
    for blocks in list_of_barriers:
        blocks.update()


    bob.draw()

    
    pygame.display.flip()

pygame.quit()





"""for enemy in enemyList:
    enemy.draw()
for projectile in projectileList:
    projectile.draw()"""
