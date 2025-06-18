import tcod
import copy

from engine import Engine
from actors import entities_factory
from dungeon_generator import generate_dungeon
from tiles import color


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

    player = copy.deepcopy(entities_factory.player)
    engine = Engine(player=player)

    engine.game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        engine=engine,
    )
    engine.update_fov()

    engine.message_log.add_message("Hello, Sinner, The Holy One wants you dead!!!", color.welcome_text)

    with tcod.context.new(columns=width, rows=height, tileset=tileset, title="Ayrtonikus", vsync=True,) as context:
        root_console = tcod.console.Console(width, height, order="F")
        while True:
            engine.render(console=root_console, context=context)

            engine.event_handler.handle_events()


if __name__ == "__main__":
    main()
