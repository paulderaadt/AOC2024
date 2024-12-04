from enum import Enum

class CardinalDirections(Enum):
    NORTH_WEST = (-1, -1)
    NORTH = (-1, -0)
    NORTH_EAST = ( -1, 1)
    WEST = ( 0, -1)
    EAST = ( 0, 1)
    SOUTH_WEST = ( 1, -1)
    SOUTH = ( 1, 0)
    SOUTH_EAST = ( 1, 1)

    def __init__(self, x, y):
        self.x = x
        self.y = y