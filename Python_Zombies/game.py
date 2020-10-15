import pygame as pg
import config as cg
from player import Player, Bullet, Enemy
from game_state import GameState
import random


bullets = [] #bullets array
enemies = [] #enemies array

#Game Class
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.objects= []
        self.game_state = GameState.NONE

    def setUp(self):
        player = Player(40,30,'E',10)
        self.player = player
        self.objects.append(player)
        print("do set up")
        self.game_state = GameState.RUNNING

    def update(self):
        self.screen.fill(cg.BLACK)
        print("update")
        self.handle_events()

        for i,b in enumerate(bullets):
            b.move()
            if ((b.position_bullet[0] <= 0) | (b.position_bullet[0] >= 80) | (b.position_bullet[1] <= 0) | (b.position_bullet[1] >= 60)):
                del bullets[i]
            else:
                b.render(self.screen)

        for object in self.objects:
            object.render(self.screen)

        for i,e in enumerate(enemies):
            e.move()
            for b in bullets:
                if (((b.position_bullet[0] <= e.position_enemy[0] + 2) and (b.position_bullet[0] >= e.position_enemy[0]-2)) and ((b.position_bullet[1] <= e.position_enemy[1] + 2) and (b.position_bullet[1] >= e.position_enemy[1] - 2))):
                    del enemies[i]
            e.render(self.screen)


    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game_state = GameState.ENDED
            #Shoots a Bullet in Direction of Mouse Click
            if event.type == pg.MOUSEBUTTONDOWN:
                x,y = pg.mouse.get_pos()
                x = (x/10)
                y = (y/10)
                x_player = self.player.get_x()
                y_player = self.player.get_y()
                b = Bullet(x,y,x_player, y_player,cg.SPEED)
                bullets.append(b)
            #Random Chance to Create Enemy Somewhere on Map
            if random.randint(0,50) == 15:
                x = random.randint(0,(cg.SCREEN_WIDTH/10))
                y = random.randint(0,(cg.SCREEN_HEIGHT/10))
                x_player = self.player.get_x()
                y_player = self.player.get_y()
                e = Enemy(x, y, x_player, y_player, 2)
                enemies.append(e)
        self.player.move()
