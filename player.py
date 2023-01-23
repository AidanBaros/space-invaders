import pygame
#o,[prt]

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.Surface((32,64))
        self.image.fill((18,122,89))
        self.rect = self.image.get_rect(center = pos)

        self.lives = 3
        self.pos = pygame.math.Vector2(self.rect.center)

        self.display_surface = pygame.display.get_surface()

    def update(self):
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
    def draw(self):
        pygame.draw(self.display_surface, self.rect)