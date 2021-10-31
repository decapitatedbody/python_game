class ObjectInSpace:
    def __init__(self, image, X, Y, change_X, change_Y):
        self.image = image
        self.X = X
        self.Y = Y
        self.change_X = change_X
        self.change_Y = change_Y

    def move(self):
        self.X += self.change_X
        self.Y += self.change_Y

    def set_changes(self, X, Y):
        self.change_X = X
        self.change_Y = Y
