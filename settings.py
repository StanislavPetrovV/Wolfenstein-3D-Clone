import math
import glm
import pygame as pg
from texture_id import ID

# opengl
MAJOR_VERSION = 3
MINOR_VERSION = 3
DEPTH_SIZE =24

# resolution
WIN_RES = glm.vec2(1280, 720)
# WIN_RES = glm.vec2(1600, 900)

# control keys
KEYS = {
    'FORWARD': pg.K_w,
    'BACK': pg.K_s,
    'UP': pg.K_q,
    'DOWN': pg.K_e,
    'STRAFE_L': pg.K_a,
    'STRAFE_R': pg.K_d,
    'INTERACT': pg.K_f,
    'WEAPON_1': pg.K_1,
    'WEAPON_2': pg.K_2,
    'WEAPON_3': pg.K_3,
}

# camera
ASPECT_RATIO = WIN_RES.x / WIN_RES.y
FOV_DEG = 50
V_FOV = glm.radians(FOV_DEG)  # vertical FOV
H_FOV = 2 * math.atan(math.tan(V_FOV * 0.5) * ASPECT_RATIO)  # horizontal FOV
NEAR = 0.01
FAR = 2000.0
PITCH_MAX = glm.radians(89)

# player
MOUSE_SENSITIVITY = 0.0015
PLAYER_SIZE = 0.15
PLAYER_SPEED = 0.0035
PLAYER_ROT_SPEED = 0.003
PLAYER_HEIGHT = 0.6
PLAYER_POS = glm.vec3(1.5, PLAYER_HEIGHT, 1.5)

PLAYER_INIT_HEALTH = 80
PLAYER_INIT_AMMO = 25
MAX_HEALTH_VALUE = 100
MAX_AMMO_VALUE = 999

#
NUM_LEVELS = 2

# colors
BG_COLOR = glm.vec3(0.1, 0.16, 0.25)

# textures
TEX_SIZE = 256
TEXTURE_UNIT_0 = 0

# walls
WALL_SIZE = 1
H_WALL_SIZE = WALL_SIZE / 2

# timer
SYNC_PULSE = 10  # ms

# ray casting
MAX_RAY_DIST = 20

# animations
ANIM_DOOR_SPEED = 0.03

# sound
MAX_SOUND_CHANNELS = 10

# number of textures
NUM_TEXTURES = len(ID)

# item settings
ITEM_SETTINGS = {
    ID.AMMO: {
        'scale': 0.2,
        'value': 8
    },
    ID.MED_KIT: {
        'scale': 0.3,
        'value': 20
    },
    ID.PISTOL_ICON: {
        'scale': 1.0
    },
    ID.RIFLE_ICON: {
        'scale': 1.0
    },
    ID.KEY: {
        'scale': 0.9
    }
}

# hud object IDs
ID.HEALTH_DIGIT_0 = 0 + NUM_TEXTURES
ID.HEALTH_DIGIT_1 = 1 + NUM_TEXTURES
ID.HEALTH_DIGIT_2 = 2 + NUM_TEXTURES
ID.AMMO_DIGIT_0 = 3 + NUM_TEXTURES
ID.AMMO_DIGIT_1 = 4 + NUM_TEXTURES
ID.AMMO_DIGIT_2 = 5 + NUM_TEXTURES
ID.FPS_DIGIT_0 = 6 + NUM_TEXTURES
ID.FPS_DIGIT_1 = 7 + NUM_TEXTURES
ID.FPS_DIGIT_2 = 8 + NUM_TEXTURES
ID.FPS_DIGIT_3 = 9 + NUM_TEXTURES

HUD_SETTINGS = {
    ID.HEALTH_DIGIT_0: {
        'scale': 0.1,
        'pos': glm.vec2(0.85, -0.95),
    },
    ID.HEALTH_DIGIT_1: {
        'scale': 0.1,
        'pos': glm.vec2(0.90, -0.95),
    },
    ID.HEALTH_DIGIT_2: {
        'scale': 0.1,
        'pos': glm.vec2(0.95, -0.95),
    },
    ID.AMMO_DIGIT_0: {
        'scale': 0.1,
        'pos': glm.vec2(-0.95, -0.95),
    },
    ID.AMMO_DIGIT_1: {
        'scale': 0.1,
        'pos': glm.vec2(-0.90, -0.95),
    },
    ID.AMMO_DIGIT_2: {
        'scale': 0.1,
        'pos': glm.vec2(-0.85, -0.95),
    },
    ID.AMMO: {
        'scale': 0.25,
        'pos': glm.vec2(-0.9, -0.82),
    },
    ID.MED_KIT: {
        'scale': 0.25,
        'pos': glm.vec2(0.9, -0.82),
    },
    ID.FPS_DIGIT_0: {
        'scale': 0.11,
        'pos': glm.vec2(-0.75, 0.87),
    },
    ID.FPS_DIGIT_1: {
        'scale': 0.11,
        'pos': glm.vec2(-0.68, 0.87),
    },
    ID.FPS_DIGIT_2: {
        'scale': 0.11,
        'pos': glm.vec2(-0.61, 0.87),
    },
    ID.FPS_DIGIT_3: {
        'scale': 0.11,
        'pos': glm.vec2(-0.54, 0.87),
    },
    ID.FPS: {
        'scale': 0.35,
        'pos': glm.vec2(-0.89, 0.74),
    },
    ID.YELLOW_SCREEN: {
        'scale': 4.0,
        'pos': glm.vec2(0.0, -2.0),
    },
    ID.RED_SCREEN: {
        'scale': 4.0,
        'pos': glm.vec2(0.0, -2.0),
    },
}

# weapon settings
WEAPON_SCALE = 1.9
WEAPON_NUM_FRAMES = 5
WEAPON_POS = glm.vec3(0.0, -1.0, 0.0)
WEAPON_ANIM_PERIODS = 4

WEAPON_SETTINGS = {
    ID.KNIFE_0: {
        'ammo_consumption': 0,
        'damage': 8,
        'max_dist': 2,
        'miss_probability': 0.3
    },
    ID.PISTOL_0: {
        'ammo_consumption': 1,
        'damage': 20,
        'max_dist': 10,
        'miss_probability': 0.1
    },
    ID.RIFLE_0: {
        'ammo_consumption': 2,
        'damage': 41,
        'max_dist': 30,
        'miss_probability': 0.045
    },
}

# npc settings
NPC_SETTINGS = {
    #
    ID.SOLDIER_BROWN_0: {
        'scale': glm.vec3(1.00),
        'anim_periods': 9,
        'num_frames': {
            'walk': 4, 'attack': 2, 'hurt': 2, 'death': 5
        },
        'state_tex_id': {
            'walk': ID.SOLDIER_BROWN_0,
            'attack': ID.SOLDIER_BROWN_0 + 4,
            'hurt': ID.SOLDIER_BROWN_0 + 6,
            'death': ID.SOLDIER_BROWN_0 + 6,
        },
        'attack_dist': 3,
        'health': 100,
        'speed': 0.004,
        'size': 0.3,
        'damage': 5,
        'hit_probability': 0.001,
        'drop_item': ID.AMMO
    },
    #
    ID.SOLDIER_BLUE_0: {
        'scale': glm.vec3(0.85),
        'anim_periods': 9,
        'num_frames': {
            'walk': 4, 'attack': 2, 'hurt': 2, 'death': 5
        },
        'state_tex_id': {
            'walk': ID.SOLDIER_BLUE_0,
            'attack': ID.SOLDIER_BLUE_0 + 4,
            'hurt': ID.SOLDIER_BLUE_0 + 6,
            'death': ID.SOLDIER_BLUE_0 + 6,
        },
        'attack_dist': 4,
        'health': 300,
        'speed': 0.0045,
        'size': 0.3,
        'damage': 7,
        'hit_probability': 0.0015,
        'drop_item': ID.AMMO
    },
    #
    ID.RAT_0: {
        'scale': glm.vec3(1.0),
        'anim_periods': 12,
        'num_frames': {
            'walk': 4, 'attack': 3, 'hurt': 2, 'death': 5
        },
        'state_tex_id': {
            'walk': ID.RAT_0,
            'attack': ID.RAT_0 + 4,
            'hurt': ID.RAT_0 + 7,
            'death': ID.RAT_0 + 7,
        },
        'attack_dist': 0.6,
        'health': 30,
        'speed': 0.0045,
        'size': 0.2,
        'damage': 2,
        'hit_probability': 0.002,
        'drop_item': None
    },
}
