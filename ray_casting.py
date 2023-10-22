import glm
from settings import MAX_RAY_DIST


class RayCasting:
    def __init__(self, eng):
        self.eng = eng
        self.level_map = eng.level_map
        self.wall_map = eng.level_map.wall_map
        self.door_map = eng.level_map.door_map
        self.player = eng.player

    @staticmethod
    def get_init_data(pos1, pos2):
        d_ = glm.sign(pos2 - pos1)
        #
        delta_ = min(d_ / (pos2 - pos1), 10000000.0) if d_ != 0 else 10000000.0
        #
        max_ = delta_ * (1.0 - glm.fract(pos1)) if d_ > 0 else delta_ * glm.fract(pos1)
        return d_, delta_, max_

    def run(self, start_pos, direction, max_dist=MAX_RAY_DIST, npc_to_player_flag=True):
        #
        x1, y1, z1 = start_pos  # start point
        x2, y2, z2 = start_pos + direction * max_dist  # end point
        cur_voxel_pos = glm.ivec3(x1, y1, z1)

        # init ray casting
        dx, delta_x, max_x = self.get_init_data(x1, x2)
        dy, delta_y, max_y = self.get_init_data(y1, y2)
        dz, delta_z, max_z = self.get_init_data(z1, z2)

        while not (max_x > 1.0 and max_y > 1.0 and max_z > 1.0):
            #
            cur_tile_pos = (cur_voxel_pos.x, cur_voxel_pos.z)

            # ----------------------------------------------
            # check walls
            if cur_tile_pos in self.wall_map:
                return False
            # check closed doors
            if cur_tile_pos in self.door_map:
                if self.door_map[cur_tile_pos].is_closed:
                    return False

            # check ray from npc or player
            if npc_to_player_flag:
                if self.player.tile_pos == cur_tile_pos:
                    return True
            # from player to npc
            elif cur_tile_pos in self.level_map.npc_map:
                return cur_tile_pos
            # ----------------------------------------------
            if max_x < max_y:
                if max_x < max_z:
                    cur_voxel_pos.x += dx
                    max_x += delta_x
                else:
                    cur_voxel_pos.z += dz
                    max_z += delta_z
            else:
                if max_y < max_z:
                    cur_voxel_pos.y += dy
                    max_y += delta_y
                else:
                    cur_voxel_pos.z += dz
                    max_z += delta_z
        return False
