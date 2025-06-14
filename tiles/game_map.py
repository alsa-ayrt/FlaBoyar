import numpy as np
from tiles import tile_types
from tcod.console import Console


class GameMap:
    def __init__(self, width: int, heigth: int):
        self.width = width
        self.height = heigth
        self.tiles = np.full((width, heigth), fill_value=tile_types.wall, order="F")

    def in_bounds(self, x: int, y: int):

        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        console.rgb[0:self.width, 0:self.height] = self.tiles["dark"]

