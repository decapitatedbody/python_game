import pygame

class Background:
    def __init__(self, X, Y, show):
        if show: self.screen = pygame.display.set_mode((X, Y))
        self.screenX = X
        self.screenY = Y

    def load_image(self, image):
        return pygame.image.load(image)

    def write(self, text, color, X, Y, font_size, font_style):
        font = pygame.font.Font(font_style, font_size)
        text_cont = font.render(text, True, color)
        text_form = text_cont.get_rect()
        text_form.topleft = (X, Y)
        self.screen.blit(text_cont, text_form)

    def show_object(self, object, X, Y):
        self.screen.blit(object, (X, Y))

    def isCollision(self, object1, object2):
        x1 = object1.X
        x2 = object2.X
        y1 = object1.Y
        y2 = object2.Y
        distance = ((x1-x2)**2+(y1-y2)**2)**0.5
        if distance <= 50:
            return True
        else: return False
