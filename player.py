class Player:

    def __init__(self, **kwargs):
        self.name = None
        self.screen = None
        self.img = None
        self.p_x = None
        self.p_y = None
        self.achievement = []
        self.death = 0

        for key, value in kwargs.items():
            setattr(self, key, value)

    def render(self):
        import pygame
        return self.screen.blit(pygame.image.load(self.img), (self.p_x, self.p_y))

    def move(self):
        import pygame
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.p_x -= 3
            return self.p_x
        elif pressed[pygame.K_RIGHT]:
            self.p_x += 3
            return self.p_x
