import pygame as pg
from . import setup, tools
from . import constants as c
from .states import main_menu, load_screen, level

def main():
    pg.mixer.init()
    setup.SOUND.play_music(setup.SOUND.soundtrack)
    game = tools.Control()
    state_dict = {c.MAIN_MENU: main_menu.Menu(),
                  c.LOAD_SCREEN: load_screen.LoadScreen(),
                  c.LEVEL: level.Level(),
                  c.VICTORY: load_screen.Victory(),
                  c.GAME_OVER: load_screen.GameOver(),
                  c.TIME_OUT: load_screen.TimeOut()}
    game.setup_states(state_dict, c.MAIN_MENU)
    game.main()
