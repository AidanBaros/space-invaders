import pygame

class Player():
    def __init__(self,screen:pygame.surface):
        self.screen = screen
        self.lives = 3
        self.pos = ()

    def update(self):
        pass
    def draw(self):
        pass








"""
self.image = pygame.Surface((32,64))
        self.image.fill((18,122,89))
        #self.rect = self.image.get_rect(center = pos)
        self.rect = pygame.Rect(0,0,64,64)
        self.rect.center = pos

        self.lives = 3
        self.pos = pygame.math.Vector2(self.rect.center)

        self.display_surface = pygame.display.get_surface()

keys = pygame.key.get_pressed()
        self.draw()

        if keys[pygame.K_a]:
            self.pos.x -= 10
        if keys[pygame.K_SPACE]:#and condition for projectile cooldown
            pass
            #fire projectile here
        elif keys[pygame.K_d]:
            self.pos.x += 10
        else:
            pass
"""