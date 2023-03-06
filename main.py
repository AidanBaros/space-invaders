import pygame
from enemy import *
from player import Player
from barrier import Barrier
from projectile import *

def create_barriers(screen:pygame.Surface, screenSize:tuple[int,int], size_multiplyer:float, list_of_barriers:list[Barrier]):
    xpos = 281 * size_multiplyer
    ypos = screenSize[1] - 328 * size_multiplyer
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

def create_enemies(list_of_enemies:list[Enemy], size_multiplyer:float):
    xpos = 64 * size_multiplyer
    ypos = 32 * size_multiplyer
    for j in range(5):
        for i in range(11):
            if j == 0:
                list_of_enemies.append(Octo((xpos + ((64*size_multiplyer)*i),ypos + ((64*size_multiplyer)*j)),size_multiplyer))
            elif j <= 2:
                list_of_enemies.append(Crab((xpos + ((64*size_multiplyer)*i),ypos + ((64*size_multiplyer)*j)),size_multiplyer))
            else:
                list_of_enemies.append(Skull((xpos + ((64*size_multiplyer)*i),ypos + ((64*size_multiplyer)*j)),size_multiplyer))
    xpos += (281 * size_multiplyer) + (128*size_multiplyer)
            
def draw_lives(player_lives:int,screen:pygame.Surface,screenSize:tuple[int,int],size_multiplyer:float):
    for i in range(player_lives):
        image = pygame.transform.scale(pygame.image.load(f"invaders_imgs/player.png"),(64*size_multiplyer,64*size_multiplyer))
        screen.blit(image, (screenSize[0]-(64*size_multiplyer*(i+1)),10*size_multiplyer))

def main():
    pygame.init()
    pygame.display.set_caption("Space Invaders")
    screen:pygame.surface.Surface = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    screenSize = screen.get_size()
    clock = pygame.time.Clock()
    gameover = False

    size_multiplyer = screenSize[0]/1920

    score = 0
    dead = False

    god_mode = False

    list_of_barriers:list[Barrier] = []
    list_of_enemies:list[Enemy] = []
    font = pygame.font.Font('freesansbold.ttf', 128)
    font2 = pygame.font.Font('freesansbold.ttf', 32)

    player = Player(screen, screenSize, size_multiplyer, god_mode)
    create_barriers(screen,screenSize,size_multiplyer, list_of_barriers)
    create_enemies(list_of_enemies, size_multiplyer)
    while not gameover:
        if player.alive == False and player.lives != 0 and god_mode == False:
            player.alive = True
            player.lives -= 1
            list_of_barriers.clear()
            list_of_enemies.clear()
            create_barriers(screen,screenSize,size_multiplyer, list_of_barriers)
            create_enemies(list_of_enemies, size_multiplyer)
        elif player.lives == 0 or dead == True:
            loose_message = font.render(f"You Loose \n Score:{score}",True,"white")
            textRect = loose_message.get_rect()
            textRect.center = (screenSize[0]//2,screenSize[1]//2)
            screen.fill("black")
            for i in range(500):
                screen.fill("black")
                screen.blit(loose_message, textRect)
                pygame.display.flip()
            break
        if len(list_of_enemies) == 0:
            create_enemies(list_of_enemies, size_multiplyer)
            for enemy in list_of_enemies:
                if enemy.speed < 10:
                    enemy.speed += 0.25
                elif enemy.max_tick < 0:
                    enemy.max_tick -= 1
            score += 100
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LCTRL] or keys[pygame.K_ESCAPE]:
                gameover = True


        screen.fill("black")
        draw_lives(player.lives,screen,screenSize,size_multiplyer)
        score_message = font2.render(f"Score:{score}",True,"white")
        textRect = score_message.get_rect()
        textRect.topleft = (20,20)
        screen.blit(score_message, textRect)
        score += player.update(list_of_enemies, list_of_barriers)
        for blocks in list_of_barriers:
            blocks.update()

        for enemies in list_of_enemies:
            enemies.get_list(list_of_enemies)

        for enemies in list_of_enemies:
            dead = enemies.edge_collide()

        for enemies in list_of_enemies:
            enemies.update(player, list_of_barriers)

        
        pygame.display.flip()

    pygame.quit()


main()
