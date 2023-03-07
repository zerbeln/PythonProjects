from scribes.agent_scribe import AgentScribe
from canvases.canvas import Canvas

"""
For challenge 2, we are creating a function that draws a square of a given size.
"""

if __name__ == '__main__':
    start_pos = [0, 0]
    square_size = 5
    canvas_size = 30

    scribe = AgentScribe(start_pos)
    scribe.draw_square(square_size)

    canvas = Canvas(canvas_size, canvas_size, [scribe])
    canvas.go()
