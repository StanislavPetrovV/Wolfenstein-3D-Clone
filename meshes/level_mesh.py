from meshes.level_mesh_builder import LevelMeshBuilder


class LevelMesh:
    def __init__(self, eng):
        self.eng = eng
        self.ctx = self.eng.ctx
        self.program = self.eng.shader_program.level

        self.vbo_format = '3u2 1u2 1u2 1u2 1u2'
        self.fmt_size = sum(int(fmt[:1]) for fmt in self.vbo_format.split())
        self.vbo_attrs = ('in_position', 'in_tex_id', 'face_id', 'ao_id', 'flip_id')

        self.mesh_builder = LevelMeshBuilder(self)
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
        vertex_data = self.mesh_builder.build_mesh()
        print('Num level vertices: ', len(vertex_data) // 7 * 3)
        return vertex_data
