import os
import threading
from termcolor import colored


class Canvas:
    def __init__(self, width, height, scribes, framerate=0.2):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]
        self.scribes = scribes
        self.framerate = framerate

    def hits_wall(self, point):
        """
        Checks to see if scribe hits a wall (either vertical or horizontal)
        """
        wall_x = True if round(point[0]) < 0 or round(point[0]) >= self._x else False
        wall_y = True if round(point[1]) < 0 or round(point[1]) >= self._y else False

        return [wall_x, wall_y]

    def go(self):
        """
        Each scribe in list executes its move set
        """

        scribe_threads = [threading.Thread(target=self.step, args=(sc,)) for sc in self.scribes]
        [t.start() for t in scribe_threads]
        [t.join() for t in scribe_threads]

    def step(self, scribe):
        """
        The scribe executes the set its current action
        """
        for action in scribe.moves:
            scribe.forward(self, action[0], distance=action[1])

    def set_pos(self, pos, mark):
        try:
            self._canvas[round(pos[0])][round(pos[1])] = mark
        except Exception as e:
            raise InvalidParameter('Cannot set position to {} '.format(pos))

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))


class ScribeException(Exception):
    def __init__(self, message=''):
        super().__init__(colored(message, 'red'))


class InvalidParameter(ScribeException):
    """
    The parameter being used is not valid for the specified assignment
    """
    pass
