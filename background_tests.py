import unittest
from background import Background
from spaceship import Spaceship

class TestBackground(unittest.TestCase):

    def setUp(self):
        self.bg = Background(500, 700, False)
        self.player1 = Spaceship("spaceship.png", 220, 600, 0, 0, 10, 10, 0, 0, 0, 4)
        self.player2 = Spaceship("spaceship.png", 270, 600, 0, 0, 10, 10, 0, 0, 0, 4)
        self.player3 = Spaceship("spaceship.png", 270, 650, 0, 0, 10, 10, 0, 0, 0, 4)
        self.player4 = Spaceship("spaceship.png", 270, 650, 0, 0, 10, 10, 0, 0, 0, 4)


    def test_isCollision(self):
        self.assertTrue(self.bg.isCollision(self.player1, self.player2))
        self.assertTrue(self.bg.isCollision(self.player2, self.player3))
        self.assertFalse(self.bg.isCollision(self.player1, self.player3))



if __name__ == "__main__":
    unittest.main()
