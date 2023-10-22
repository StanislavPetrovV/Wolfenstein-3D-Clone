import pygame as pg
from texture_id import *
from settings import MAX_SOUND_CHANNELS


class Sound:
    def __init__(self):
        pg.mixer.init()
        pg.mixer.set_num_channels(MAX_SOUND_CHANNELS)
        self.channel = 0
        self.path = 'assets/sounds/'
        #
        self.player_attack = {
            ID.KNIFE_0: self.load('w_knife.ogg', volume=0.2),
            ID.PISTOL_0: self.load('w_pistol.wav', volume=0.2),
            ID.RIFLE_0: self.load('w_rifle.ogg', volume=0.2)
        }
        #
        self.player_hurt = self.load('p_hurt.ogg')
        #
        self.player_death = self.load('p_death.ogg')
        #
        self.player_missed = self.load('p_missed.wav')
        #
        self.open_door = self.load('p_open_door.wav', volume=1.0)
        #
        self.pick_up = {
            ID.AMMO: self.load('p_ammo.ogg'),
            ID.MED_KIT: self.load('p_med_kit.mp3'),
            ID.KEY: self.load('p_key.wav'),
        }
        self.pick_up[ID.PISTOL_ICON] = self.pick_up[ID.AMMO]
        self.pick_up[ID.RIFLE_ICON] = self.pick_up[ID.AMMO]
        #
        self.enemy_attack = {
            ID.SOLDIER_BLUE_0: self.load('n_soldier_attack.mp3', volume=0.8),
            ID.SOLDIER_BROWN_0: self.load('n_soldier_attack.mp3', volume=0.8),
            ID.RAT_0: self.load('n_rat_attack.ogg', volume=0.2),
        }
        #
        self.spotted = {
            ID.SOLDIER_BLUE_0: self.load('n_soldier_spotted.ogg', volume=1.0),
            ID.SOLDIER_BROWN_0: self.load('n_brown_spotted.ogg', volume=0.8),
            ID.RAT_0: self.load('n_rat_spotted.ogg', volume=0.5),
        }
        #
        self.death = {
            ID.SOLDIER_BLUE_0: self.load('n_blue_death.ogg', volume=0.8),
            ID.SOLDIER_BROWN_0: self.load('n_brown_death.ogg', volume=0.8),
            ID.RAT_0: self.load('no_sound.mp3', volume=0.0),
        }
        #
        pg.mixer.music.load(self.path + 'theme.ogg')
        pg.mixer.music.set_volume(0.1)

    def load(self, file_name, volume=0.5):
        sound = pg.mixer.Sound(self.path + file_name)
        sound.set_volume(volume)
        return sound

    def play(self, sound):
        pg.mixer.Channel(self.channel).play(sound)
        self.channel += 1
        if self.channel == MAX_SOUND_CHANNELS:
            self.channel = 0
