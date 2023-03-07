from scribes.terminal_scribe import TerminalScribe
from canvases.canvas import Canvas


"""
For challenge 3, we are creating a direction attribute for TerminalScribe that indicates where the scribe points.
We are then creating a forward function that will move it in that direction.

Assumptions: 
    I am assuming that the forward function will only move forward one time step
    Currently TerminalScribe does not have a speed attribute, so the default will be 1 unit/timestep
"""

if __name__ == '__main__':
    start_pos = [0, 0]
    scribe = TerminalScribe(start_pos)
    distance = 15  # The distance the scribe will move
    direction = 120  # Direction in degrees (0 is up, 180 is down)
    scribe.get_moves([direction, distance])

    canvas = Canvas(20, 20, [scribe])
    canvas.go()
