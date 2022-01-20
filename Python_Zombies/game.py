#Micah Perez - Python Zombies - Created October 1st 2020
import pygame as pg
import config as cg
import pygame.freetype
import sys
import os
from player import Player, Bullet, Enemy
from game_state import GameState
import random


bullets = [] #bullets array
enemies = [] #enemies array

#Set up path for font using os
font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"fonts","QuirkyRobot.ttf")
font_size = cg.FONT_SIZE
pygame.freetype.init()
#set font 
robot_font = pygame.freetype.Font(font_path, font_size)

#Game Class
class Game:
    #Init function for game state
    def __init__(self, screen):
        self.screen = screen
        self.objects= []
        self.game_state = GameState.NONE
        self.enemies_killed = 0
        self.health = 0
        #Used to calculate accuracy
        self.shots = 0

    #Create player and give them starting parameters
    def setUp(self):
        player = Player(40,30,'E',10)
        self.player = player
        self.objects.append(player)
        print("do set up")
        self.game_state = GameState.RUNNING

    #Function created to display game stats
    def stats(self):
        robot_font.render_to(self.screen, (100, 35), "Health:"+str(self.enemies_killed), cg.WHITE, None, size=30)
        robot_font.render_to(self.screen, (300, 35), "Enemys Killed:"+str(self.enemies_killed), cg.WHITE, None, size=30)
        try:
            robot_font.render_to(self.screen, (500, 35), "Accuracy:"+str(round(self.enemies_killed/self.shots*100, 2)) + "%", cg.WHITE, None, size=30)
        except:
            robot_font.render_to(self.screen, (500, 35), "Accuracy:"+str(0), cg.WHITE, None, size=30)


    #Update Function - Screen, Player, and Enemy Update
    def update(self):
        self.screen.fill(cg.BLACK)
        print("update")
        self.handle_events()
        self.stats() # draw text

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
                    self.enemies_killed += 1
            e.render(self.screen)


    #In game is out of events then quit game, also notice if a bullet has been shot
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
                self.shots += 1
            #Random Chance to Create Enemy Somewhere on Map
            if random.randint(0,50) == 15:
                x = random.randint(0,(cg.SCREEN_WIDTH/10))
                y = random.randint(0,(cg.SCREEN_HEIGHT/10))
                x_player = self.player.get_x()
                y_player = self.player.get_y()
                e = Enemy(x, y, x_player, y_player, 2)
                enemies.append(e)
        self.player.move()
