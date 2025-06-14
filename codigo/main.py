import tcod

from engine import Engine
from input_handlers import EventHandler
from codigo.actors.entity import Entity
from codigo.tiles.game_map import GameMap


def main():

    width = 60
    height = 60
    map_width = 60
    map_height = 55

    tileset = tcod.tileset.load_tilesheet("img1.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

    event_handler = EventHandler()

    player = Entity(int(width / 2), int(height / 2), "@", (255, 255, 255))
    npc = Entity(1, 1, "@", (255, 255, 0))
    entities = {npc, player}

    game_map = GameMap(map_width, map_height)

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    with tcod.context.new(columns=width, rows=height, tileset=tileset, title="Ayrtonikus", vsync=True,) as context:
        root_console = tcod.console.Console(width, height, order="F")
        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()
            engine.handle_events(events)


if __name__ == "__main__":
    main()
