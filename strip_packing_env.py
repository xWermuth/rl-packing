import numpy as np
from enum import Enum


class Alignment(Enum):
    LEFT = 0
    RIGHT = 1


class Dimension():
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height


class Rect(Dimension):
    def __init__(self, width: int, height: int, x: int, y: int) -> None:
        super(width, height)
        self.x = x
        self.y = y


class FirstFitStrip:
    def __init__(self, strip_height, strip_width):
        '''
        This cannot handle dynamic sized bin nor number of bins. 
        '''
        # Set strip dimensions
        self.strip_height = strip_height
        self.strip_width = strip_width
        self.cells = []
        # Rects that are placed
        self.state = []
    # Pack

    def _init_state(self):
        state = [

        ]
        return np.array(state, dtype=int)

    def _place_rect(self, rect: Rect, alignment: Alignment, cell_location):
        cell = self._find_fitting_cell(rect, cell_location)

        if cell is None:
            return False

        if alignment == Alignment.LEFT:
            # Place rect
            self.state.append(Rect(rect.width, rect.height, cell.x, cell.y))
        elif alignment == Alignment.RIGHT:
            new_x = cell.x + cell.width - rect.width
            self.state.append(Rect(rect.width, rect.height, new_x, cell.y))

        return True

    def _overlaps(self, rect: Dimension, cell: Dimension):
        return rect.width <= cell.width and rect.height <= cell.height

    def _find_fitting_cell(self, rect: Dimension, cell_location: int):
        cell = self.cells[cell_location]

        if self._overlaps(rect, cell):
            # TODO finde new cell
            for (i, cell) in enumerate(self.cells):
                if not self._overlaps(rect, cell):
                    return cell

        return None

    def _get_state(self):
        '''
        State contains
            - Free cells
            - Occupied cells
            - Placement height
            - Max min height difference
        '''
        pass

    def step(self, action: list, rect: Dimension):
        '''
        Action should place: binId, cell_location, alignment
        '''
        done = False
        reward = 0
        state = []

        alignment, cell_location = self._get_action(action)

        could_place = self._place_rect(rect, alignment, cell_location)

        if not could_place:
            reward = -10
            done = True

        # Check if cell is free

        return done, reward, state

    def reset(self):
        self.cells = []
        return self.state

    def _get_action(action: list):

        # Determine alignment from action
        alignment = Alignment.RIGHT
        if(action[0] == 1):
            alignment = Alignment.LEFT
        elif(action[1] == 1):
            alignment = Alignment.RIGHT

        # Determine Cell location
        cell_location = 0
        cells = action[3:len(action)]

        for(i, cell) in enumerate(cells):
            if(cell == 1):
                cell_location = i
                break

        return alignment, cell_location

    def _get_state():
        state = [
            # Free cells

            # Occupied cells

            # Placement height

            # Max min height difference
        ]

        return state

    def compute_reward(self):
        pass


class RandService:
    def __init__(self, rects_length):
        self.rects_length = rects_length

    def generateSet(self):
        '''Generate random data set'''
        return []
