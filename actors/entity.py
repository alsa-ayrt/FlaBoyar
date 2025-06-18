from __future__ import annotations
from typing import Tuple, TypeVar, TYPE_CHECKING, Optional, Type

import copy

from tiles.render_order import RenderOrder

if TYPE_CHECKING:
    from tiles.game_map import GameMap
    from actors.components.ai import BaseAi
    from actors.components.fighter import Fighter

T = TypeVar("T", bound="Entity")


class Entity:

    gamemap: GameMap

    def __init__(self,
                 gamemap: Optional[GameMap] = None,
                 x: int = 0,
                 y: int = 0,
                 char: str = "?",
                 color: Tuple[int, int, int] = (255, 255, 255),
                 name: str = "<Unnamed>",
                 blocks_movements: bool = False,
                 render_order: RenderOrder = RenderOrder.CORPSE,):

        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks_movements = blocks_movements
        self.render_order = render_order

        if gamemap:
            self.gamemap = gamemap
            gamemap.entities.add(self)

    def spawn(self: T, gamemap: GameMap, x: int, y: int) -> T:
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        clone.gamemap = gamemap
        gamemap.entities.add(clone)
        return clone

    def place(self, x: int, y: int, gamemap: Optional[GameMap] = None) -> None:
        self.x = x
        self.y = y

        if gamemap:
            if hasattr(self, "gamemap"):
                self.gamemap.entities.remove(self)
            self.gamemap = gamemap
            gamemap.entities.add(self)

    def move(self, dx: int, dy: int) -> None:

        self.x += dx
        self.y += dy


class Actor(Entity):
    def __init__(self,
                 *,
                 x: int = 0,
                 y: int = 0,
                 char: str = "?",
                 color: Tuple[int, int, int] = Tuple[255, 255, 255],
                 name: str = "<Unnamed>",
                 ai_cls: Type[BaseAi],
                 fighter: Fighter):
        super().__init__(
            x=x,
            y=y,
            char=char,
            color=color,
            name=name,
            blocks_movements=True,
            render_order=RenderOrder.ACTOR,
        )

        self.ai: Optional[BaseAi] = ai_cls(self)
        self.fighter = fighter
        self.fighter.entity = self

    @property
    def is_alive(self) -> bool:

        return bool(self.ai)
