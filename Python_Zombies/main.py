#Micah Perez - Python Zombies - Created October 1st 2020
import pygame as pg
import config as cf
from game_state import GameState
from game import Game

#Main function to initialize varaibles and run main code 
pg.init()

#Creates Screen 
screen = pg.display.set_mode((800,600))

pg.display.set_caption("Shooters")

clock = pg.time.Clock()

game = Game(screen)
game.setUp()

while game.game_state == GameState.RUNNING:
    #Change the clock tick to get a different speed of Game
    clock.tick(500)
    game.update()
    pg.display.flip()


