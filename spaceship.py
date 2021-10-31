from objectinspace import ObjectInSpace
from stack import Stack

class Spaceship(ObjectInSpace):

    def __init__(self, image, X, Y, change_X, change_Y, hp, max_hp, score, gold, hp_healed, num_bullets):
        super().__init__(image, X, Y, change_X, change_Y)
        self.hp = hp
        self.max_hp = max_hp
        self.score = score
        self.gold = gold
        self.hp_healed = hp_healed
        self.nb = num_bullets
        self.gun = Stack()
        self.bullets = []
        for _ in range(self.nb):
            self.gun.push(ObjectInSpace("weapons.png", 220, 600, 0, -9))
            self.bullets.append(0)

    def fire(self):
        if self.gun.is_empty(): return None
        else:
            shot = self.gun.pop()
            shot.X = self.X + 17
            shot.Y = self.Y + 10
            for i in range(self.nb):
                if isinstance(self.bullets[i], int):
                    self.bullets[i] = shot
                    break

    def reload(self):
        self.gun.push(ObjectInSpace("weapons.png", 220, 600, 0, -9))

    def flying_bullets(self, target, screen):
        for i in range(self.nb):
            if isinstance(self.bullets[i], ObjectInSpace):
                screen.show_object(screen.load_image(self.bullets[i].image), self.bullets[i].X, self.bullets[i].Y)
                self.bullets[i].move()
                if screen.isCollision(self.bullets[i], target):
                    self.bullets[i] = 0
                    self.reload()
                    target.hits_taken += 1
            if isinstance(self.bullets[i], ObjectInSpace):
                if self.bullets[i].Y < -32:
                    self.bullets[i] = 0
                    self.reload()
