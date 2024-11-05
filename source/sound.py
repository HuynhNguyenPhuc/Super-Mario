from pygame import mixer

class Sound:
    def __init__(self):
        self.music_channel = mixer.Channel(0)
        self.music_channel.set_volume(0.2)
        self.sfx_channel = mixer.Channel(1)
        self.sfx_channel.set_volume(0.2)

        self.allowSFX = True
        self.allowMusic = True

        self.soundtrack = mixer.Sound("./resources/sfx/main_theme.ogg")
        self.coin = mixer.Sound("./resources/sfx/coin.ogg")
        self.bump = mixer.Sound("./resources/sfx/bump.ogg")
        self.stomp = mixer.Sound("./resources/sfx/stomp.ogg")
        self.jump = mixer.Sound("./resources/sfx/small_jump.ogg")
        self.death = mixer.Sound("./resources/sfx/death.wav")
        self.kick = mixer.Sound("./resources/sfx/kick.ogg")
        self.brick_bump = mixer.Sound("./resources/sfx/brick-bump.ogg")
        self.powerup = mixer.Sound('./resources/sfx/powerup.ogg')
        self.powerup_appear = mixer.Sound('./resources/sfx/powerup_appears.ogg')
        self.pipe = mixer.Sound('./resources/sfx/pipe.ogg')

    def play_sfx(self, sfx):
        if self.allowSFX:
            self.sfx_channel.play(sfx)

    def play_music(self, music):
        if self.allowMusic:
            self.music_channel.play(music, loops=-1)

    def toggle_sfx(self):
        self.allowSFX = not self.allowSFX

    def toggle_music(self):
        if self.allowMusic:
            self.music_channel.stop()
        else:
            self.music_channel.play(self.soundtrack, loops=-1)
        self.allowMusic = not self.allowMusic