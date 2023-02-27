import pygame


class Player:
    def __init__(
        self,
        screen: pygame.surface.Surface,
        screenSize: tuple[int, int],
        size_multiplyer,
    ):
        self.screen = screen

        self.screenSize = screenSize

        self.player_x = 64*size_multiplyer
        self.player_y = 64*size_multiplyer

        self.rect = pygame.Rect(
            self.screenSize[0] // 2 - (self.player_x/2), self.screenSize[1] - (100*size_multiplyer + self.player_x), self.player_x, self.player_y
        )
        self.hitbox = self.rect.copy()
        self.image = pygame.transform.scale(pygame.image.load(f"invaders_imgs/player.png"),(self.player_x,self.player_y))

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 10

        self.lives = 3

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

        if keys[pygame.K_SPACE]:
            self.attack()

    def move(self,size_multiplyer):
        self.pos.x += self.direction.x * self.speed * size_multiplyer
        self.hitbox.centerx = round(self.pos.x)
        self.rect.centerx = self.hitbox.centerx

    def draw(self):
        #pygame.draw.rect(self.screen, (255, 0, 0), self.rect)
        self.screen.blit(self.image,self.rect)

    def attack(self):
        
        pass

    def update(self,size_multiplyer):
        self.input()
        self.move(size_multiplyer)
        self.draw()
