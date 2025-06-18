from __future__ import annotations
from typing import TYPE_CHECKING

from actors.components.base_component import BaseComponent
from tiles.render_order import RenderOrder
from input_handlers import GameOverEventHandler

if TYPE_CHECKING:
    from actors.entity import Actor


class Fighter(BaseComponent):
    entity: Actor

    def __init__(self, hp: int, defense: int, power: int):
        self.max_hp = hp
        self._hp = hp
        self.defense = defense
        self.power = power

    @property
    def hp(self) -> int:

        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = max(0, min(value, self.max_hp))
        if self._hp == 0 and self.entity.ai:
            self.die()

    def die(self) -> None:
        if self.engine.player == self.entity:
            death_message = "You died!"
            self.engine.event_handler = GameOverEventHandler(self.engine)
        else:
            death_message = f"{self.entity.name} returned to Goddess Embrace"

        self.entity.char = "%"
        self.entity.color = (191, 0, 0)
        self.entity.blocks_movements = False
        self.entity.ai = None
        self.entity.name = f"{self.entity.name} remains"
        self.entity.render_order = RenderOrder.CORPSE

        print(death_message)
