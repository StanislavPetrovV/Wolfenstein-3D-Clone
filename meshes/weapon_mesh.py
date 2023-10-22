from meshes.quad_mesh import QuadMesh


class WeaponMesh(QuadMesh):
    def __init__(self, eng, shader_program, weapon_instance):
        super().__init__(eng, shader_program)
        #
        self.weapon = weapon_instance

    def set_uniforms(self):
        self.program['m_model'].write(self.weapon.m_model)
        self.program['tex_id'] = self.weapon.frame + self.weapon.weapon_id

    def render(self):
        self.set_uniforms()
        self.vao.render()
