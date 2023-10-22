from collections import deque
from functools import lru_cache


class PathFinder:
    def __init__(self, eng):
        self.eng = eng
        self.level_map = eng.level_map
        self.wall_map = eng.level_map.wall_map
        self.ways = ([-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [1, -1], [1, 1], [-1, 1])
        self.graph = {}
        self.update_graph()

    @lru_cache
    def find(self, start_pos, end_pos):
        visited = self.bfs(start_pos, end_pos)
        path = [end_pos]
        step = visited.get(end_pos, start_pos)

        while step and step != start_pos:
            path.append(step)
            step = visited[step]
        return path[-1]

    def bfs(self, start, goal):
        queue = deque([start])
        visited = {start: None}

        while queue:
            cur_node = queue.popleft()
            if cur_node == goal:
                break
            next_nodes = self.graph[cur_node]

            for next_node in next_nodes:
                if next_node not in visited and next_node not in self.eng.level_map.npc_map:
                    queue.append(next_node)
                    visited[next_node] = cur_node
        return visited

    def get_next_nodes(self, x, y):
        return [
            (x + dx, y + dy) for dx, dy in self.ways if (x + dx, y + dy) not in self.wall_map
        ]

    def update_graph(self):
        for y in range(self.level_map.depth):
            for x in range(self.level_map.width):
                self.graph[(x, y)] = self.graph.get((x, y), []) + self.get_next_nodes(x, y)
