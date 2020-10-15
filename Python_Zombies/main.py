import pygame as pg
import config as cf
from game_state import GameState
from game import Game

pg.init()

screen = pg.display.set_mode((800,600))

pg.display.set_caption("Shooters")

clock = pg.time.Clock()

game = Game(screen)
game.setUp()

while game.game_state == GameState.RUNNING:
    clock.tick(50)
    game.update()
    pg.display.flip()
