from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from actions import Action, EscapedAction, BumpAction
import tcod.event

if TYPE_CHECKING:
    from engine import Engine


class EventHandler(tcod.event.EventDispatch[Action]):

    def __init__(self, engine: Engine):

        self.engine = engine

        self.KEY_COMMANDS = {
            tcod.event.KeySym.UP: "move N",
            tcod.event.KeySym.DOWN: "move S",
            tcod.event.KeySym.LEFT: "move W",
            tcod.event.KeySym.RIGHT: "move E",
            tcod.event.KeySym.ESCAPE: "move Esc"
        }

    def handle_events(self):

        for event in tcod.event.wait():
            action = self.dispatch(event)

            if action is None:
                continue

            action.perform()

            self.engine.handle_enemy_turn()
            self.engine.update_fov()

    def ev_quit(self, event: tcod.event.Quit, /) -> Optional[Action]:
        raise SystemExit

    def ev_keydown(self, event: tcod.event.KeyDown, /) -> Optional[Action]:

        action: Optional[Action] = None

        key = event.sym
        player = self.engine.player

        if key in self.KEY_COMMANDS:

            if self.KEY_COMMANDS[key] == "move N":
                action = BumpAction(player, dx=0, dy=-1)
            elif self.KEY_COMMANDS[key] == "move S":
                action = BumpAction(player, dx=0, dy=1)
            elif self.KEY_COMMANDS[key] == "move W":
                action = BumpAction(player, dx=-1, dy=0)
            elif self.KEY_COMMANDS[key] == "move E":
                action = BumpAction(player, dx=1, dy=0)

            elif self.KEY_COMMANDS[key] == "move Esc":
                action = EscapedAction(player)

        return action
