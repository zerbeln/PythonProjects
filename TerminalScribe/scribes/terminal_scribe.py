import time
import math
from termcolor import colored


class TerminalScribe:
    def __init__(self, start_pos):
        self.trail = '.'
        self.mark = '*'
        self.pos = start_pos
        self.direction = [0, 1]  # The direction vector in [x, y]
        self.moves = []

    def get_moves(self, action):
        """
        Add an action to the scribes move set. An action consists of [degrees, distance]
        """
        self.moves.append(action)

    def set_direction(self, degrees):
        """
        Sets the scribes current direction or heading
        """
        d_radians = (degrees/180) * math.pi
        self.direction = [math.sin(d_radians), -math.cos(d_radians)]

    def set_position(self, pos):
        """
        Sets the position of the scribe
        """
        self.pos = pos

    def draw(self, pos, canvas):
        """
        Draws the scribe on the canvas
        """
        canvas.set_pos(self.pos, self.trail)
        self.pos = pos
        canvas.set_pos(self.pos, colored(self.mark, 'red'))
        canvas.print()
        time.sleep(canvas.framerate)

    def bounce(self, reflection):
        """
        If the scribe hits a wall, the bounce function will invert either the x and y components of the direction
        based off of the wall it hit (vertical or horizontal).
        """
        self.direction[0] *= reflection[0]
        self.direction[1] *= reflection[1]

    def forward(self, canvas, direction, distance):
        """
        The scribe moves forward by a given distance along its current heading
        """
        self.set_direction(direction)
        for d in range(distance):
            pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]

            wall_impact = canvas.hits_wall(pos)

            # Will draw the scribe on Canvas if it does not hit a wall
            if not wall_impact[0] and not wall_impact[1]:
                self.draw(pos, canvas)
