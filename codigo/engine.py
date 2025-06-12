from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console

from actions import EscapedAction, MovementAction
from entity import Entity
from input_handlers import EventHandler

class Engine:
    def __init__(self, entities):

