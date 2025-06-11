import tcod
from actions import EscapedAction, MovementAction
from input_handlers import EventHandler


def main():

    width = 80
    height = 80
    player_x = int(width / 2)
    player_y = int(height / 2)

    tileset = tcod.tileset.load_tilesheet("codigo/img1.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

    event_handler = EventHandler()
    with tcod.context.new(columns=width, rows=height, tileset=tileset, title="Ayrtonikus", vsync=True,) as context:
        root_console = tcod.console.Console(width, height, order="F")
        while True:
            root_console.print(x=player_x, y=player_y, string="@")

            context.present(root_console)
            root_console.clear()

            for event in tcod.event.wait():

                action = event_handler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                elif isinstance(action, EscapedAction):
                    raise SystemExit


if __name__ == "__main__":
    main()
