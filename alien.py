from objectinspace import ObjectInSpace
import random

class Alien(ObjectInSpace):
    go = False
    comet = []

    def __init__(self, image, X, Y, change_X, change_Y, comet_missed, hits_taken, num_comets):
        super().__init__(image, X, Y, change_X, change_Y)
        self.comet_missed = comet_missed
        self.hits_taken = hits_taken
        self.num_comets = num_comets

    def set_comet(self, comet, X = (500,740), Y = (-100,400), chg = (4,5,7)):
        change = random.choice(chg)
        comet.X = random.randint(*X)
        comet.Y = random.randint(*Y)
        comet.change_X, comet.change_Y = -change, change

    def attack(self, target, screen, bounce):
        if self.Y == 1 and (not bounce):
            self.comet = []
            for _ in range(self.num_comets):
                self.comet.append(ObjectInSpace("nature.png", random.randint(500, 740), random.randint(-100, 400), -5, 5))
            self.go = True
        if self.go:
            for i in range(self.num_comets):
                screen.show_object(screen.load_image(self.comet[i].image), self.comet[i].X, self.comet[i].Y)
                self.comet[i].move()
                if self.comet[i].Y > 700:
                    if bounce < 20:
                        self.set_comet(self.comet[i])
                    else: self.set_comet(self.comet[i], Y=(-500,-500), chg=(0,0))
                    self.comet_missed += 1
                elif bounce < 20 and self.comet[i].Y == -500:
                    self.set_comet(self.comet[i])
                if screen.isCollision(self.comet[i], target):
                    if bounce < 20:
                        self.set_comet(self.comet[i])
                        target.hp -= 1
                    else:
                        self.set_comet(self.comet[i], X = (600,600), chg = (0,0,0))
                    self.hits_taken += 1
