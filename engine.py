from player import Player, PlayerAttribs
from scene import Scene
from shader_program import ShaderProgram
from path_finding import PathFinder
from ray_casting import RayCasting
from level_map import LevelMap
from textures import Textures
from sound import Sound
import pygame as pg


class Engine:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.num_level = 0

        self.textures = Textures(self)
        self.sound = Sound()

        self.player_attribs = PlayerAttribs()
        self.player: Player = None
        self.shader_program: ShaderProgram = None
        self.scene: Scene = None

        self.level_map: LevelMap = None
        self.ray_casting: RayCasting = None
        self.path_finder: PathFinder = None
        self.new_game()

    def new_game(self):
        pg.mixer.music.play(-1)
        self.player = Player(self)
        self.shader_program = ShaderProgram(self)
        self.level_map = LevelMap(
            self, tmx_file=f'level_{self.player_attribs.num_level}.tmx'
        )
        self.ray_casting = RayCasting(self)
        self.path_finder = PathFinder(self)
        self.scene = Scene(self)

    def update_npc_map(self):
        new_npc_map = {}
        for npc in self.level_map.npc_list:
            if npc.is_alive:
                new_npc_map[npc.tile_pos] = npc
            else:
                self.level_map.npc_list.remove(npc)
        #
        self.level_map.npc_map = new_npc_map

    def handle_events(self, event):
        self.player.handle_events(event=event)

    def update(self):
        self.update_npc_map()
        self.player.update()
        self.shader_program.update()
        self.scene.update()

    def render(self):
        self.scene.render()
