import pygame as pg
from .. import tools
from .. import setup
from .. import constants as c
from .. components import info

class Menu(tools.State):
    def __init__(self):
        tools.State.__init__(self)
        persist = {
            c.COIN_TOTAL: 0,
            c.SCORE: 0,
            c.LIVES: 3,
            c.TOP_SCORE: 0,
            c.CURRENT_TIME: 0.0,
            c.LEVEL_NUM: 4,
            c.PLAYER_NAME: c.PLAYER_MARIO,
            c.SOUND_ON: True,
            c.SFX_ON: True,
        }
        self.startup(0.0, persist)

    def startup(self, current_time, persist):
        self.next = c.LOAD_SCREEN
        self.persist = persist
        self.game_info = persist
        self.overhead_info = info.Info(self.game_info, c.MAIN_MENU)

        self.setup_background()
        self.setup_cursor()
        self.setup_buttons()

    def setup_background(self):
        self.background = setup.GFX['level_4']
        self.background_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background,
                                    (int(self.background_rect.width * c.BACKGROUND_MULTIPLER),
                                     int(self.background_rect.height * c.BACKGROUND_MULTIPLER)))

        self.viewport = setup.SCREEN.get_rect(bottom=setup.SCREEN_RECT.bottom)
        self.image_dict = {}
        image = tools.get_image(setup.GFX['title_screen'], 1, 60, 176, 88,
                            (255, 0, 220), c.SIZE_MULTIPLIER)
        rect = image.get_rect()
        rect.x, rect.y = (250, 20)
        self.image_dict['GAME_NAME_BOX'] = (image, rect)

    def setup_cursor(self):
        self.cursor = pg.sprite.Sprite()
        self.cursor.image = tools.get_image(setup.GFX[c.ITEM_SHEET], 24, 160, 8, 8, c.BLACK, 3)
        rect = self.cursor.image.get_rect()
        rect.x, rect.y = (250, 50)
        self.cursor.rect = rect
        self.cursor.index = 0

    def setup_buttons(self):
        self.options = ['Start', 'Sound', 'SFX', 'Exit']
        self.button_positions = [(250, 220), (250, 270), (250, 320), (250, 370)]

    def update(self, surface, keys, current_time):
        self.current_time = current_time
        self.game_info[c.CURRENT_TIME] = self.current_time
        self.update_cursor(keys)
        self.overhead_info.update(self.game_info)

        surface.blit(self.background, self.viewport, self.viewport)
        surface.blit(self.image_dict['GAME_NAME_BOX'][0],
                     self.image_dict['GAME_NAME_BOX'][1])
        surface.blit(self.cursor.image, self.cursor.rect)
        self.overhead_info.draw(surface)

    def update_cursor(self, keys):
        if keys[pg.K_DOWN]:
            self.cursor.index = (self.cursor.index + 1) % len(self.options)
            pg.time.delay(200)
        elif keys[pg.K_UP]:
            self.cursor.index = (self.cursor.index - 1) % len(self.options)
            pg.time.delay(200)

        if keys[pg.K_RETURN]:
            self.handle_selection()
            pg.time.delay(200)

        self.cursor.rect.y = self.button_positions[self.cursor.index][1]

    def handle_selection(self):
        selected_option = self.options[self.cursor.index]
        
        if selected_option == 'Start':
            self.reset_game_info()
            self.done = True
        elif selected_option == 'Sound':
            self.game_info[c.SOUND_ON] = not self.game_info[c.SOUND_ON]
            # self.overhead_info.handle_main_state(self.game_info[c.SOUND_ON], self.game_info[c.SFX_ON])
            setup.SOUND.toggle_music()
        elif selected_option == 'SFX':
            self.game_info[c.SFX_ON] = not self.game_info[c.SFX_ON]
            # self.overhead_info.handle_main_state(self.game_info[c.SOUND_ON], self.game_info[c.SFX_ON])
            setup.SOUND.toggle_sfx()
        elif selected_option == 'Exit':
            pg.quit()

    def reset_game_info(self):
        self.game_info[c.COIN_TOTAL] = 0
        self.game_info[c.SCORE] = 0
        self.game_info[c.LIVES] = 3
        self.game_info[c.CURRENT_TIME] = 0.0
        self.game_info[c.LEVEL_NUM] = 4
        self.persist = self.game_info