class Object:
    def __init__(self, **kwargs):
        self.screen = None
        self.color = None
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

        for key, value in kwargs.items():
            setattr(self, key, value)

    def render_gate(self):
        import pygame
        return pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
