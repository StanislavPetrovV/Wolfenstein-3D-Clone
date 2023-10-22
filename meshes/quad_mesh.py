from meshes.base_mesh import BaseMesh
from settings import *
import numpy as np


class QuadMesh:
    def __init__(self, eng, shader_program):
        self.eng = eng
        self.ctx = eng.ctx
        self.program = shader_program

        self.vbo_format = '4f 2f'
        self.vbo_attrs = ('in_position', 'in_uv')
        self.vao = self.get_vao()

    def get_vao(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        vao = self.ctx.vertex_array(
            self.program,
            [
                (vbo, self.vbo_format, *self.vbo_attrs)
            ],
            skip_errors=True
        )
        return vao

    def render(self):
        self.vao.render()

    def get_vertex_data(self):
        vert_position = (
            [-0.5, 0.0, 0.0, 1.0], [-0.5, 1.0, 0.0, 1.0],
            [ 0.5, 1.0, 0.0, 1.0], [ 0.5, 0.0, 0.0, 1.0]
        )

        uv_coords = (
            [1, 1], [1, 0], [0, 0], [0, 1]
        )

        vert_indices = [
            0, 2, 1, 0, 3, 2
        ]

        vert_data = []
        for vert_index in vert_indices:
            vert_data += vert_position[vert_index]
            vert_data += uv_coords[vert_index]

        vert_data = np.array(vert_data, dtype='float32')
        return vert_data
