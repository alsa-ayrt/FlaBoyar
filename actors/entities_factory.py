from actors.entity import Actor, Item
from actors.components.ai import HostileAi
from actors.components.fighter import Fighter
from actors.components.consumable import HealingConsumable
from actors.components.inventory import Inventory

player = Actor(char="@",
               color=(255, 255, 255),
               name="Player",
               ai_cls=HostileAi,
               fighter=Fighter(hp=30, defense=2, power=5),
               inventory=Inventory(capacity=26),)

orc = Actor(char="o",
            color=(63, 127, 63),
            name="Orc",
            ai_cls=HostileAi,
            fighter=Fighter(hp=10, defense=0, power=3),
            inventory=Inventory(capacity=0),)

troll = Actor(char="T",
              color=(0, 127, 0),
              name="Troll",
              ai_cls=HostileAi,
              fighter=Fighter(hp=16, defense=1, power=4),
              inventory=Inventory(capacity=0),)

health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=HealingConsumable(amount=4)
)
