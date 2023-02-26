import pygame

class Barrier():
    def __init__(self,screen:pygame.Surface,pos,size_multiplyer:float):
        self.screen = screen
        self.image_states = []
        self.health = 4
        self.pos = pos
        self.alive = True
        self.size = 32*size_multiplyer

        for i in range(3,-1,-1):
            self.image_states.append(pygame.transform.scale(pygame.image.load(f"images/barrier_{i}.png"),(self.size,self.size)))


    def damage(self):
        pass


    def draw(self):
        if self.alive:
            self.screen.blit(self.image_states[self.health-1], self.pos)


    def update(self):
        self.damage()
        self.draw()

