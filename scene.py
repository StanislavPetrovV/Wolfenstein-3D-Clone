from meshes.level_mesh import LevelMesh
from meshes.instanced_quad_mesh import InstancedQuadMesh
from game_objects.hud import HUD
from game_objects.weapon import Weapon
from meshes.weapon_mesh import WeaponMesh


class Scene:
    def __init__(self, eng):
        self.eng = eng
        self.level_mesh = LevelMesh(eng)

        self.hud = HUD(eng)
        self.doors = self.eng.level_map.door_map.values()
        self.items = self.eng.level_map.item_map.values()
        self.npc = self.eng.level_map.npc_map.values()
        self.weapon = Weapon(eng)

        self.instanced_door_mesh = InstancedQuadMesh(
            eng, self.doors, eng.shader_program.instanced_door
        )
        self.instanced_item_mesh = InstancedQuadMesh(
            eng, self.items, eng.shader_program.instanced_billboard
        )
        self.instanced_hud_mesh = InstancedQuadMesh(
            eng, self.hud.objects, eng.shader_program.instanced_hud
        )
        self.instanced_npc_mesh = InstancedQuadMesh(
            eng, self.npc, eng.shader_program.instanced_billboard
        )
        self.weapon_mesh = WeaponMesh(eng, eng.shader_program.weapon, self.weapon)

    def update(self):
        for door in self.doors:
            door.update()
        for npc in self.npc:
            npc.update()
        self.hud.update()
        self.weapon.update()

    def render(self):
        # level
        self.level_mesh.render()
        # doors
        self.instanced_door_mesh.render()
        # items
        self.instanced_item_mesh.render()
        # hud
        self.instanced_hud_mesh.render()
        # npc
        self.instanced_npc_mesh.render()
        # weapon
        self.weapon_mesh.render()
