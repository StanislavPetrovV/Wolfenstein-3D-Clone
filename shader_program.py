from settings import *
from texture_id import ID


class ShaderProgram:
    def __init__(self, eng):
        self.eng = eng
        self.ctx = eng.ctx
        self.player = eng.player

        # -------- shaders -------- #
        self.level = self.get_program(shader_name='level')
        self.instanced_door = self.get_program(shader_name='instanced_door')
        self.instanced_billboard = self.get_program(shader_name='instanced_billboard')
        self.instanced_hud = self.get_program(shader_name='instanced_hud')
        self.weapon = self.get_program(shader_name='weapon')
        # ------------------------- #
        self.set_uniforms_on_init()

    def set_uniforms_on_init(self):
        # level
        self.level['m_proj'].write(self.player.m_proj)
        self.level['u_texture_array_0'] = TEXTURE_UNIT_0

        # instanced door
        self.instanced_door['m_proj'].write(self.player.m_proj)
        self.instanced_door['u_texture_array_0'] = TEXTURE_UNIT_0

        # billboard
        self.instanced_billboard['m_proj'].write(self.player.m_proj)
        self.instanced_billboard['u_texture_array_0'] = TEXTURE_UNIT_0

        # hud
        self.instanced_hud['u_texture_array_0'] = TEXTURE_UNIT_0

        # weapon
        self.weapon['u_texture_array_0'] = TEXTURE_UNIT_0

    def update(self):
        self.level['m_view'].write(self.player.m_view)
        self.instanced_door['m_view'].write(self.player.m_view)
        self.instanced_billboard['m_view'].write(self.player.m_view)

    def get_program(self, shader_name):
        with open(f'shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()

        with open(f'shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()

        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program
