import unittest
from coin import Coin
from spaceship import Spaceship
import random

class TestCoin(unittest.TestCase):

    def setUp(self):
        self.player = Spaceship("spaceship.png", 220, 600, 0, 0, 10, 10, 0, 0, 0, 4) # standardowy gracz, 10 żyć
        self.player_second = Spaceship("spaceship.png", 220, 600, 0, 0, 0, 10, 0, 0, 0, 4) # gracz o zerowej liczbie żyć
        # coin leczący tylko za 1
        self.c = Coin("coin1.png", random.randint(0, 430), random.randint(-250, -70), 0, random.randint(3,5), 1, random.randint(1, 3))
        self.c.heal(self.player)
        self.c.heal(self.player_second)
        self.c.set_coin(X=(0,5), Y=(100,200), changeY=(8,9))

    def test_set_coin(self):
        self.assertIn(self.c.X, range(0,6))
        self.assertIn(self.c.Y, range(100,201))
        self.assertIn(self.c.change_Y, range(8,10))

    def test_heal(self):
        self.assertEqual(self.player.hp, 10)
        self.assertNotEqual(self.player.hp, 11)
        self.assertEqual(self.player_second.hp, 1)
        self.assertNotEqual(self.player_second.hp, 0)
        self.assertNotEqual(self.player_second.hp, 2)


if __name__ == "__main__":
    unittest.main()
