from settings import *
import numpy as np


class LevelMeshBuilder:
    def __init__(self, mesh):
        self.mesh = mesh
        self.map = mesh.eng.level_map

    def get_ao(self, x, z, plane):
        if plane == 'Y':
            a = not self.is_blocked(x    , z - 1)
            b = not self.is_blocked(x - 1, z - 1)
            c = not self.is_blocked(x - 1, z    )
            d = not self.is_blocked(x - 1, z + 1)
            e = not self.is_blocked(x    , z + 1)
            f = not self.is_blocked(x + 1, z + 1)
            g = not self.is_blocked(x + 1, z    )
            h = not self.is_blocked(x + 1, z - 1)

        elif plane == 'X':
            a = not self.is_blocked(x, z - 1)
            b, c, d = 0, 0, 0
            e = not self.is_blocked(x, z + 1)
            f, g, h = 0, 0, 0

        else:  # Z plane
            a = not self.is_blocked(x - 1, z)
            b, c, d = 0, 0, 0
            e = not self.is_blocked(x + 1, z)
            f, g, h = 0, 0, 0

        ao = (a + b + c), (g + h + a), (e + f + g), (c + d + e)
        return ao

    def is_blocked(self, x, z):
        if not (0 <= x < self.map.width and 0 <= z < self.map.depth):
            return True
        return (x, z) in self.map.wall_map

    def add_data(self, vertex_data, index, *vertices):
        for vertex in vertices:
            for attr in vertex:
                vertex_data[index] = attr
                index += 1
        return index

    def build_mesh(self):
        vertex_data = np.empty(
            [self.map.width * self.map.depth * self.mesh.fmt_size * 18], dtype='uint16'
        )
        index = 0

        for x in range(self.map.width):
            for z in range(self.map.depth):
                # flats
                if pos_not_in_wall_map := (x, z) not in self.map.wall_map:
                    # get ao id
                    ao = self.get_ao(x, z, plane='Y')
                    flip_id = ao[1] + ao[3] > ao[0] + ao[2]

                    # floor
                    if (x, z) in self.map.floor_map:
                        tex_id = self.map.floor_map[(x, z)]
                        face_id = 0

                        v0 = (x    , 0, z    , tex_id, face_id, ao[0], flip_id)
                        v1 = (x + 1, 0, z    , tex_id, face_id, ao[1], flip_id)
                        v2 = (x + 1, 0, z + 1, tex_id, face_id, ao[2], flip_id)
                        v3 = (x    , 0, z + 1, tex_id, face_id, ao[3], flip_id)

                        if flip_id:
                            index = self.add_data(vertex_data, index, v1, v0, v3, v1, v3, v2)
                        else:
                            index = self.add_data(vertex_data, index, v0, v3, v2, v0, v2, v1)

                    # ceil
                    if (x, z) in self.map.ceil_map:
                        tex_id = self.map.ceil_map[(x, z)]
                        face_id = 1

                        v0 = (x    , 1, z    , tex_id, face_id, ao[0], flip_id)
                        v1 = (x + 1, 1, z    , tex_id, face_id, ao[1], flip_id)
                        v2 = (x + 1, 1, z + 1, tex_id, face_id, ao[2], flip_id)
                        v3 = (x    , 1, z + 1, tex_id, face_id, ao[3], flip_id)

                        if flip_id:
                            index = self.add_data(vertex_data, index, v1, v3, v0, v1, v2, v3)
                        else:
                            index = self.add_data(vertex_data, index, v0, v2, v3, v0, v1, v2)

                # wall faces -----------------------------------------------------------------
                if pos_not_in_wall_map:
                    continue

                tex_id = self.map.wall_map[(x, z)]

                # wall back face
                if not self.is_blocked(x, z - 1):
                    face_id = 2
                    ao = self.get_ao(x, z - 1, plane='Z')
                    flip_id = ao[1] + ao[3] > ao[0] + ao[2]

                    v0 = (x    , 0, z, tex_id, face_id, ao[0], flip_id)
                    v1 = (x    , 1, z, tex_id, face_id, ao[1], flip_id)
                    v2 = (x + 1, 1, z, tex_id, face_id, ao[2], flip_id)
                    v3 = (x + 1, 0, z, tex_id, face_id, ao[3], flip_id)

                    if flip_id:
                        index = self.add_data(vertex_data, index, v3, v0, v1, v3, v1, v2)
                    else:
                        index = self.add_data(vertex_data, index, v0, v1, v2, v0, v2, v3)

                # wall front face
                if not self.is_blocked(x, z + 1):
                    face_id = 3
                    ao = self.get_ao(x, z + 1, plane='Z')
                    flip_id = ao[1] + ao[3] > ao[0] + ao[2]

                    v0 = (x    , 0, z + 1, tex_id, face_id, ao[0], flip_id)
                    v1 = (x    , 1, z + 1, tex_id, face_id, ao[1], flip_id)
                    v2 = (x + 1, 1, z + 1, tex_id, face_id, ao[2], flip_id)
                    v3 = (x + 1, 0, z + 1, tex_id, face_id, ao[3], flip_id)

                    if flip_id:
                        index = self.add_data(vertex_data, index, v3, v1, v0, v3, v2, v1)
                    else:
                        index = self.add_data(vertex_data, index, v0, v2, v1, v0, v3, v2)

                # wall right face
                if not self.is_blocked(x + 1, z):
                    face_id = 4
                    ao = self.get_ao(x + 1, z, plane='X')
                    flip_id = ao[1] + ao[3] > ao[0] + ao[2]

                    v0 = (x + 1, 0, z    , tex_id, face_id, ao[0], flip_id)
                    v1 = (x + 1, 1, z    , tex_id, face_id, ao[1], flip_id)
                    v2 = (x + 1, 1, z + 1, tex_id, face_id, ao[2], flip_id)
                    v3 = (x + 1, 0, z + 1, tex_id, face_id, ao[3], flip_id)

                    if flip_id:
                        index = self.add_data(vertex_data, index, v3, v0, v1, v3, v1, v2)
                    else:
                        index = self.add_data(vertex_data, index, v0, v1, v2, v0, v2, v3)

                # wall left face
                if not self.is_blocked(x - 1, z):
                    face_id = 5
                    ao = self.get_ao(x - 1, z, plane='X')
                    flip_id = ao[1] + ao[3] > ao[0] + ao[2]

                    v0 = (x, 0, z    , tex_id, face_id, ao[0], flip_id)
                    v1 = (x, 1, z    , tex_id, face_id, ao[1], flip_id)
                    v2 = (x, 1, z + 1, tex_id, face_id, ao[2], flip_id)
                    v3 = (x, 0, z + 1, tex_id, face_id, ao[3], flip_id)

                    if flip_id:
                        index = self.add_data(vertex_data, index, v3, v1, v0, v3, v2, v1)
                    else:
                        index = self.add_data(vertex_data, index, v0, v2, v1, v0, v3, v2)

        return vertex_data[:index]
