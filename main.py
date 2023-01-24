import pygame
from enemy import *
from player import Player
from projectile import *


pygame.init()
pygame.display.set_caption("Space Invaders")
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screenSize = screen.get_size()
clock = pygame.time.Clock()
gameover = False
enemyList = []
projectileList = []

Xmultiplyer = 1920/screenSize[0]
Ymultiplyer = 1080/screenSize[1]



while not gameover: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LCTRL]:
            gameover = True





"""for enemy in enemyList:
    enemy.draw()
for projectile in projectileList:
    projectile.draw()"""
