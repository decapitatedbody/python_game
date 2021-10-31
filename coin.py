from objectinspace import ObjectInSpace
import random

class Coin(ObjectInSpace):
    def __init__(self, image, X, Y, change_X, change_Y, healing, value):
        super().__init__(image, X, Y, change_X, change_Y)
        self.healing = healing
        self.value = value

    def heal(self, target):
        first_hp = target.hp
        target.hp = min(target.max_hp, target.hp + self.healing)
        target.hp_healed += target.hp - first_hp

    def set_coin(self, X=(0, 430), Y=(-250,-70), changeY=(3, 5)):
        self.X = random.randint(*X)
        self.Y = random.randint(*Y)
        self.change_Y = random.randint(*changeY)
        self.healing = random.randint(1, 2)
        self.value = random.randint(1, 3)
