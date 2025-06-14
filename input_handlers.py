from typing import Optional
from actions import Action, EscapedAction, MovementAction
import tcod.event


class EventHandler(tcod.event.EventDispatch[Action]):

    def __init__(self):

        self.KEY_COMMANDS = {
            tcod.event.KeySym.UP: "move N",
            tcod.event.KeySym.DOWN: "move S",
            tcod.event.KeySym.LEFT: "move W",
            tcod.event.KeySym.RIGHT: "move E",
            tcod.event.KeySym.ESCAPE: "move Esc"
        }

    def ev_quit(self, event: tcod.event.Quit, /) -> Optional[Action]:
        raise SystemExit

    def ev_keydown(self, event: tcod.event.KeyDown, /) -> Optional[Action]:

        action: Optional[Action] = None

        key = event.sym

        if key in self.KEY_COMMANDS:

            if self.KEY_COMMANDS[key] == "move N":
                action = MovementAction(dx=0, dy=-1)
            elif self.KEY_COMMANDS[key] == "move S":
                action = MovementAction(dx=0, dy=1)
            elif self.KEY_COMMANDS[key] == "move W":
                action = MovementAction(dx=-1, dy=0)
            elif self.KEY_COMMANDS[key] == "move E":
                action = MovementAction(dx=1, dy=0)

            elif self.KEY_COMMANDS[key] == "move Esc":
                action = EscapedAction()

        return action
