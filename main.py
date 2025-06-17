import tcod
import copy

from engine import Engine
from input_handlers import EventHandler
from actors import entities_factory
from dungeon_generator import generate_dungeon


def main():

    width = 100
    height = 60
    map_width = 100
    map_height = 55

    room_min_size = 6
    room_max_size = 10
    max_rooms = 20

    max_monsters_per_room = 2

    tileset = tcod.tileset.load_tilesheet("img1.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

    event_handler = EventHandler()

    player = copy.deepcopy(entities_factory.player)

    game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        player=player,
    )

    engine = Engine(event_handler=event_handler, game_map=game_map, player=player)

    with tcod.context.new(columns=width, rows=height, tileset=tileset, title="Ayrtonikus", vsync=True,) as context:
        root_console = tcod.console.Console(width, height, order="F")
        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()
            engine.handle_events(events)


if __name__ == "__main__":
    main()
