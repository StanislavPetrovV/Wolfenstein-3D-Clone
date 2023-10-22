from meshes.quad_mesh import QuadMesh
from game_objects.game_object import GameObject
from settings import *


class HUDObject:
    def __init__(self, hud, tex_id):
        self.tex_id = tex_id
        self.pos = glm.vec3(HUD_SETTINGS[tex_id]['pos'], 0)
        self.rot = 0
        #
        hud.objects.append(self)
        #
        scale = HUD_SETTINGS[tex_id]['scale']
        self.scale = glm.vec3(scale / ASPECT_RATIO, scale, 0)
        #
        self.m_model = GameObject.get_model_matrix(self)


class HUD:
    def __init__(self, eng):
        self.eng = eng
        self.app = eng.app
        #
        self.objects = []
        #
        self.health = HUDObject(self, ID.MED_KIT)
        self.ammo = HUDObject(self, ID.AMMO)
        self.fps = HUDObject(self, ID.FPS)
        #
        self.ammo_digit_0 = HUDObject(self, ID.AMMO_DIGIT_0)
        self.ammo_digit_1 = HUDObject(self, ID.AMMO_DIGIT_1)
        self.ammo_digit_2 = HUDObject(self, ID.AMMO_DIGIT_2)
        #
        self.health_digit_0 = HUDObject(self, ID.HEALTH_DIGIT_0)
        self.health_digit_1 = HUDObject(self, ID.HEALTH_DIGIT_1)
        self.health_digit_2 = HUDObject(self, ID.HEALTH_DIGIT_2)
        #
        self.fps_digit_0 = HUDObject(self, ID.FPS_DIGIT_0)
        self.fps_digit_1 = HUDObject(self, ID.FPS_DIGIT_1)
        self.fps_digit_2 = HUDObject(self, ID.FPS_DIGIT_2)
        #
        self.digits = [0, 0, 0]

    def update_digits(self, value):
        value = min(value, 999)
        self.digits[2] = value % 10
        #
        value //= 10
        self.digits[1] = value % 10
        #
        value //= 10
        self.digits[0] = value % 10

    def update(self):
        # ammo
        self.update_digits(self.eng.player.ammo)
        self.ammo_digit_0.tex_id = self.digits[0] + ID.DIGIT_0
        self.ammo_digit_1.tex_id = self.digits[1] + ID.DIGIT_0
        self.ammo_digit_2.tex_id = self.digits[2] + ID.DIGIT_0

        # health
        self.update_digits(self.eng.player.health)
        self.health_digit_0.tex_id = self.digits[0] + ID.DIGIT_0
        self.health_digit_1.tex_id = self.digits[1] + ID.DIGIT_0
        self.health_digit_2.tex_id = self.digits[2] + ID.DIGIT_0

        # fps
        self.update_digits(self.eng.app.fps_value)
        self.fps_digit_0.tex_id = self.digits[0] + ID.DIGIT_0
        self.fps_digit_1.tex_id = self.digits[1] + ID.DIGIT_0
        self.fps_digit_2.tex_id = self.digits[2] + ID.DIGIT_0
