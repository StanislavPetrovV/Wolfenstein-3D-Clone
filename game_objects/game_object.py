import glm
from settings import H_WALL_SIZE


class GameObject:
    def __init__(self, level_map, tex_id, x, z):
        self.eng = level_map.eng
        self.app = self.eng.app
        self.tex_id = tex_id
        #
        self.pos = glm.vec3(x + H_WALL_SIZE, 0, z + H_WALL_SIZE)  # center of the tile
        self.rot = 0
        self.scale = glm.vec3(1)
        #
        self.m_model: glm.mat4 = None

    def get_model_matrix(self):
        m_model = glm.translate(glm.mat4(), self.pos)
        m_model = glm.rotate(m_model, self.rot, glm.vec3(0, 1, 0))
        m_model = glm.scale(m_model, self.scale)
        return m_model

