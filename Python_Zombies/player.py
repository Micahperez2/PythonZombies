import pygame as pg
import config as cg
from game_state import GameState
import math, random

#Player Class
class Player:
    def __init__(self, x_position, y_position, direction, health):
        print("player created")
        self.position = [x_position, y_position]
        self.direction = 'E'
        self.health = health

    def update(self):
        print("player updated")

    #Updates position relative to current position
    def update_position(self, x_change, y_change):
        self.position[0] += x_change
        self.position[1] += y_change

    #Updates position relative to screen
    def change_position(self, x_change, y_change):
        self.position[0] = x_change
        self.position[1] = y_change

    def get_x(self):
        return int(self.position[0])

    def get_y(self):
        return int(self.position[1])

    #Changes Direction of Object
    def update_direction(self, direction_change):
        self.direction = direction_change

    def render(self, screen):
        pg.draw.rect(screen, cg.WHITE, (self.position[0]*cg.SCALE, self.position[1]*cg.SCALE, cg.SCALE, cg.SCALE), 6)

    #Moves Character depending on Key Pressed
    def move(self):
        keys = pg.key.get_pressed()  #checking pressed keys
        if keys[pg.K_ESCAPE]:
            self.game_state = GameState.ENDED
        if keys[pg.K_w]:
            self.update_position(0, -1)
            self.update_direction('N')
        if keys[pg.K_s]:
            self.update_position(0, 1)
            self.update_direction('S')
        if keys[pg.K_a]:
            self.update_position(-1, 0)
            self.update_direction('W')
        if keys[pg.K_d]:
            self.update_position(1, 0)
            self.update_direction('E')
        #Bounce to Other Side if you Hit the Endge
        if (self.position[0] <= 0):
            self.position[0] += 80
        if (self.position[0] >= 80):
            self.position[0] -= 80
        if (self.position[1] <= 0):
            self.position[1] += 60
        if (self.position[1] >= 60):
            self.position[1] -= 60

#Bullet Class
class Bullet:
    def __init__(self, x_player, y_player, x_bullet, y_bullet, speed):
        print("bullet created")
        self.position_bullet = [x_bullet, y_bullet]
        angle = math.atan2(x_bullet - x_player, y_bullet - y_player)
        print('Angle in degrees:', int(angle*180/math.pi))
        self.dy = math.cos(angle)*speed
        self.dx = math.sin(angle)*speed
        self.x_bullet = x_bullet
        self.y_bullet = y_bullet

    #Override
    def move(self):
        #self.x and self.y are floats (decimals) so I get more accuracy
        #if I change self.x and y and then convert to an integer for
        #the rectangle.
        self.x_bullet = self.x_bullet + self.dx
        self.y_bullet = self.y_bullet + self.dy
        self.position_bullet[0] = self.x_bullet
        self.position_bullet[1] = self.y_bullet

    def render(self, screen):
        pg.draw.rect(screen, cg.RED, (self.position_bullet[0]*cg.SCALE, self.position_bullet[1]*cg.SCALE, cg.SCALE, cg.SCALE), 2)

class Enemy:
    def __init__(self, x_enemy, y_enemy, x_player, y_player, health):
        print("enemy created")
        self.position_enemy = [x_enemy, y_enemy]
        self.x_player = x_player
        self.y_player = y_player
        self.health = health
        self.x_direction = 1
        self.y_direction = 1
        self.speed = 1

    def change_x(self):
        self.x_direction = (self.x_direction * -1)

    def change_y(self):
        self.y_direction = (self.y_direction * -1)

    def move(self):
        if (self.position_enemy[0] <= 0):
            self.change_x()
        if (self.position_enemy[0] >= 80):
            self.change_x()
        if (self.position_enemy[1] <= 0):
            self.change_y()
        if (self.position_enemy[1] >= 60):
            self.change_y()
        dx = self.x_direction
        dy = self.y_direction
        self.position_enemy[0] = (self.speed * dx) + self.position_enemy[0]
        self.position_enemy[1] = (self.speed * dy) + self.position_enemy[1]

    def render(self, screen):
        pg.draw.rect(screen, cg.GREEN, (self.position_enemy[0]*cg.SCALE, self.position_enemy[1]*cg.SCALE, cg.SCALE, cg.SCALE), 4)
