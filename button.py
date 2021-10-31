import pygame

class Button:
    def __init__(self, text, color, X, Y, width, height):
        self.txt = text
        self.color = color
        self.X = X
        self.Y = Y
        self.width = width
        self.height = height
        self.field = pygame.Rect(X, Y, width, height)

    def draw(self, surface, color, outln=(0, 0, 0)):
        pygame.draw.rect(surface, outln, (self.X-3, self.Y-3, self.width+4, self.height+4))
        font = pygame.font.Font("freesansbold.ttf", 32)
        text = font.render(self.txt, True, color)
        surface.blit(text, (self.X + (self.width/2 - text.get_width()/2),\
                            self.Y + (self.height/2 - text.get_height()/2)))  # ustawianie napisu jak
                                                                              # najbardziej na środku przycisku
