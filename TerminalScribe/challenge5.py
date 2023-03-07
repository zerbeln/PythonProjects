from scribes.agent_scribe import AgentScribe
from canvases.canvas import Canvas

"""
For this challenge, we are asked to modify the "Forward" function to move the scribe forward a specified distance.
If the scribe hits a wall in either the X or Y direction, it should "bounce" back the opposite direction
"""


if __name__ == '__main__':
    n_scribes = 3

    direction = 45
    start_pos = [5, 5]
    scribe = AgentScribe(start_pos)
    scribe.set_direction(direction)

    canvas = Canvas(30, 30, [scribe])
    scribe.forward_bounce(canvas, distance=100)
