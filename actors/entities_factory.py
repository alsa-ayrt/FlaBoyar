from actors.entity import Entity

player = Entity(char="@", color=(255, 255, 255), name="Player", blocks_movements=True)

orc = Entity(char="o", color=(63, 127, 63), name="Orc", blocks_movements=True)
troll = Entity(char="T", color=(0, 127, 0), name="Troll", blocks_movements=True)