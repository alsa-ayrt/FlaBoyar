import tcod
from actions import EscapedAction, MovementAction
from input_handlers import EventHandler
from entity import Entity


def main():

    width = 80
    height = 80


    tileset = tcod.tileset.load_tilesheet("img1.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

    event_handler = EventHandler()

    player = Entity(int(width / 2 ), int(height / 2), "@", (255, 255, 255))
    npc = Entity(1, 1, "@", (255, 255, 0))
    entities = {npc, player}

    with tcod.context.new(columns=width, rows=height, tileset=tileset, title="Ayrtonikus", vsync=True,) as context:
        root_console = tcod.console.Console(width, height, order="F")
        while True:
            root_console.print(x=player.x, y=player.y, string=player.char, fg=player.color)

            context.present(root_console)
            root_console.clear()

            for event in tcod.event.wait():

                action = event_handler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):

                    player.move(dx=action.dx, dy=action.dy)

                elif isinstance(action, EscapedAction):
                    raise SystemExit


if __name__ == "__main__":
    main()
