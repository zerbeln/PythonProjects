from scribes.terminal_scribe import TerminalScribe
import time
from termcolor import colored


class FunctionScribe(TerminalScribe):
    def __init__(self, start_pos, func):
        super().__init__(start_pos)

        self.func = func

    def plot_function(self, x, canvas):
        """
        This function takes in x and y values from a function defined externally and plot it
        """
        pos = [x, self.func(x)]

        wall_impact = canvas.hits_wall(pos)
        if not wall_impact[0] and not wall_impact[1]:
            return pos

    def draw(self, pos, canvas):
        """
        Draws the scribe on the canvas
        """
        canvas.set_pos(self.pos, self.trail)
        self.pos = pos
        canvas.set_pos(self.pos, colored(self.mark, 'red'))
        canvas.print()
        time.sleep(canvas.framerate)
