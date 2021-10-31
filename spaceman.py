import pygame, sys, random
from pygame.locals import *
from objectinspace import ObjectInSpace
from spaceship import Spaceship
from alien import Alien
from background import Background
from coin import Coin
from button import Button

class Game():
    pygame.init()
    screen = Background(500, 700, True)
    clock = pygame.time.Clock()

    def set_meteor(self, meteor, Y=(-250,-70), changeY = (5, 8)):
        meteor.X = random.choice(range(-2, 440, 63))
        meteor.Y = random.randint(*Y)
        meteor.change_Y = random.randint(*changeY)

    def check_position(self, object, XLeft, XRight):
        if object.X <= XLeft:
            object.X = XLeft
        elif object.X >= XRight:
            object.X = XRight

    def launch_game(self):
        button1 = Button("START", (200,200,200), 130, 270, 230, 40)
        button2 = Button("HOW TO PLAY", (200,200,200), 130, 320, 230, 40)
        button3 = Button("EXIT", (200,200,200), 130, 370, 230, 40)
        while True:
            self.screen.screen.fill((49, 64, 78))
            self.screen.write("SPACE TRAVEL", (221, 244, 100), 100, 170, 45, "Wolland.ttf")

            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pos = pygame.mouse.get_pos()
            button1.draw(self.screen.screen, (221, 244, 100))
            if button1.field.collidepoint(pos):
                if click:
                    self.play_game()
            button2.draw(self.screen.screen, (221, 244, 100))
            if button2.field.collidepoint(pos):
                if click:
                    self.how_to_play()
            button3.draw(self.screen.screen, (221, 244, 100))
            if button3.field.collidepoint(pos):
                if click:
                    pygame.quit()
                    sys.exit()
            self.clock.tick(30)
            pygame.display.update()

    def how_to_play(self):
        running = True
        while running:
            self.screen.screen.fill((49, 64, 78))
            self.screen.screen.blit(self.screen.load_image("back.png"), (100, 80))
            self.screen.write("move left", (221, 244, 100), 270, 95, 35, "EXTRASerif-Regular.ttf")
            self.screen.screen.blit(self.screen.load_image("arrow.png"), (100, 150))
            self.screen.write("move right", (221, 244, 100), 270, 165, 35, "EXTRASerif-Regular.ttf")
            self.screen.screen.blit(self.screen.load_image("down-arrow12.png"), (100, 230))
            self.screen.write("do not move", (221, 244, 100), 270, 245, 35, "EXTRASerif-Regular.ttf")
            self.screen.write("Space Bar", (0, 0, 0), 60, 320, 25, "CorbertWide-Regular.ttf")
            self.screen.write("shoot", (221, 244, 100), 270, 323, 35, "EXTRASerif-Regular.ttf")
            self.screen.write("Decription:", (0, 0, 0), 40, 450, 35, "EXTRASerif-Regular.ttf")
            self.screen.write("The aim is to survive as long as possible.", (221, 244, 100), 40, 490, 30, "EXTRASerif-Regular.ttf")
            self.screen.write("Avoid meteors and comets.", (221, 244, 100), 40, 530, 30, "EXTRASerif-Regular.ttf")
            self.screen.write("If there is an alien, try to shoot it,", (221, 244, 100), 40, 570, 30, "EXTRASerif-Regular.ttf")
            self.screen.write("you will get additional points by hitting it.", (221, 244, 100), 40, 610, 30, "EXTRASerif-Regular.ttf")
            self.screen.write("press esc to back to menu", (221, 244, 100), 155, 660, 15, "freesansbold.ttf")

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            self.clock.tick(30)
            pygame.display.update()

    def game_over(self, pl_score, pl_hp_healed, pl_gold, al_comet_missed, al_hits_taken, met_avoided):
        running = True
        game_over_time = pygame.time.get_ticks()
        while running:
            self.screen.screen.blit(self.screen.load_image("space11.png"), (0, 0))
            self.screen.write("GAME OVER", (221, 244, 100), 65, 100, 60, "freesansbold.ttf")
            self.screen.write("check your results", (221, 244, 100), 160, 180, 20, "freesansbold.ttf")
            self.screen.write("Score: {}".format(pl_score), (221, 244, 100), 60, 250, 35, "freesansbold.ttf")
            self.screen.write("including {} meteors, {} comets".format(met_avoided, al_comet_missed),\
                              (221, 244, 100), 60, 300, 20, "freesansbold.ttf")
            self.screen.write("and {} hits to the alien".format(al_hits_taken), (221, 244, 100), 60, 325, 20, "freesansbold.ttf")
            self.screen.write("Lives healed: {}".format(pl_hp_healed), (221, 244, 100), 60, 360, 35, "freesansbold.ttf")
            self.screen.write("Gold: {}".format(pl_gold), (221, 244, 100), 60, 410, 35, "freesansbold.ttf")
            self.screen.write("press esc to back to menu", (221, 244, 100), 155, 660, 15, "freesansbold.ttf")

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            self.clock.tick(30)
            pygame.display.update()

    def play_game(self):
        alien = Alien("transportation.png", 220, -70, random.choice([8, -8]), 1, 0, 0, 5)
        player = Spaceship("spaceship.png", 220, 600, 0, 0, 10, 10, 0, 0, 0, 4)
        running, alien_out = True, True
        last_meteor_time = pygame.time.get_ticks()
        fire_time = pygame.time.get_ticks()
        meteor, coin = [], []
        num_meteors, num_coins, count, bounce, met_avoided = 5, 2, 0, 0, 0
        for _ in range(num_meteors):
            meteor.append(ObjectInSpace("meteor.png", random.choice(range(-2, 440, 63)),\
                          random.randint(-250, -70), 0, random.randint(5, 8)))
        for _ in range(num_coins):
            coin.append(Coin("coin1.png", random.randint(0, 430), random.randint(-250, -70), 0, random.randint(3,5),\
                                          random.randint(1, 2), random.randint(1, 3)))
        while running:
            self.screen.screen.blit(self.screen.load_image("space11.png"), (0, 0))
            now = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.key == K_LEFT: player.set_changes(-11, player.change_Y)
                    elif event.key == K_RIGHT: player.set_changes(11, player.change_Y)
                    elif event.key == K_DOWN: player.set_changes(0, 0)
                    elif event.key == K_SPACE:
                        if now - fire_time >= 200:
                            player.fire()
                            fire_time = pygame.time.get_ticks()

            # wyswietlanie meteorow
            for i in range(num_meteors):
                self.screen.show_object(self.screen.load_image(meteor[i].image), meteor[i].X, meteor[i].Y)
                meteor[i].move()
                if meteor[i].Y > 700:
                    if count < 5 * num_meteors:
                        self.set_meteor(meteor[i])
                        count += 1
                        bounce = 0
                        last_meteor_time = pygame.time.get_ticks()
                    else: self.set_meteor(meteor[i], Y=(-500,-500), changeY=(0,0))
                    met_avoided += 1
                elif count < 5 * num_meteors and meteor[i].Y == -500:
                    self.set_meteor(meteor[i])

                if self.screen.isCollision(meteor[i], player):
                    if count < 5 * num_meteors:
                        self.set_meteor(meteor[i])
                        count += 1
                        bounce = 0
                        last_meteor_time = pygame.time.get_ticks()
                    else: self.set_meteor(meteor[i], Y=(-500,-500), changeY=(0,0))
                    player.hp -= 1

            # wyswietlanie coinow
            for i in range(num_coins):
                self.screen.show_object(self.screen.load_image(coin[i].image), coin[i].X, coin[i].Y)
                coin[i].move()
                if coin[i].Y > 700:
                    if count < 4 * num_meteors:
                        coin[i].set_coin()
                    else: coin[i].set_coin(Y=(-500,-500), changeY=(0,0))
                elif count < 5 * num_meteors and coin[i].Y == -500:
                    coin[i].set_coin()
                if self.screen.isCollision(coin[i], player):
                    if count < 4 * num_meteors:
                        coin[i].set_coin()
                    else: coin[i].set_coin(Y=(-500,-500), changeY=(0,0))
                    coin[i].heal(player)
                    player.gold += coin[i].value

            if count == 5 * num_meteors:
                cooldown = 5000
                real_time = now - last_meteor_time
                if real_time >= cooldown and real_time <= 1.8 * cooldown:
                    if real_time < 1.2 * cooldown or (real_time < 1.6 * cooldown and real_time > 1.4 * cooldown):
                        self.screen.write("WATCH OUT", (200,200,200), 70, 250, 60, "freesansbold.ttf")
                elif real_time > 1.8 * cooldown:
                    self.screen.show_object(self.screen.load_image(alien.image), alien.X, alien.Y)
                    if alien_out:
                        alien.set_changes(alien.change_X, 1)
                        alien_out = False
                    alien.Y += alien.change_Y
                    if alien.Y >= 0: alien.attack(player, self.screen, bounce)
                    if alien.Y >= 36:
                        if bounce <= 22:
                            alien.set_changes(alien.change_X, 0)
                            if alien.X <= 0:
                                alien.set_changes(8, 0)
                                bounce += 1
                            elif alien.X >= 436:
                                alien.set_changes(-8, 0)
                                bounce += 1
                            alien.move()
                        else:
                            if alien.X == 220:
                                alien.X = 220
                                alien.set_changes(alien.change_X, -1)
                            alien.move()
                    elif alien.Y < -64 and bounce > 0:
                        alien_out = True
                        count = 0

            # "obslugiwanie" gracza
            player.score = met_avoided + alien.comet_missed + alien.hits_taken
            player.move()
            player.flying_bullets(alien, self.screen)
            self.screen.show_object(self.screen.load_image(player.image), player.X, player.Y)
            self.screen.write("Lives: {}".format(player.hp), (255, 255, 255), 10, 670, 25, "freesansbold.ttf")
            self.check_position(player, 5, 431)

            if not player.hp:
                running = False
                self.game_over(player.score, player.hp_healed, player.gold, alien.comet_missed, alien.hits_taken, met_avoided)
            self.clock.tick(60)
            pygame.display.update()

if __name__ == "__main__":
    new_game = Game()
    new_game.launch_game()
    # new_game.play_game()
    # new_game.game_over()
