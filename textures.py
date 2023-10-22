import moderngl as mgl
from settings import *
from texture_builder import TextureArrayBuilder


class Textures:
    def __init__(self, eng):
        self.eng = eng
        self.ctx = eng.ctx

        # build texture arrays
        TextureArrayBuilder(should_build=True)

        # load textures
        self.texture_array = self.load('texture_array/texture_array.png')

        # assign texture unit
        self.texture_array.use(location=TEXTURE_UNIT_0)

    def load(self, file_path):
        texture = pg.image.load(f'assets/{file_path}')
        texture = pg.transform.flip(texture, flip_x=True, flip_y=False)

        num_layers = texture.get_height() // texture.get_width()
        texture = self.eng.ctx.texture_array(
            size=(texture.get_width(), texture.get_height() // num_layers, num_layers),
            components=4,
            data=pg.image.tostring(texture, 'RGBA', False)
        )

        texture.anisotropy = 32.0
        texture.build_mipmaps()
        texture.filter = (mgl.NEAREST, mgl.NEAREST)
        return texture
