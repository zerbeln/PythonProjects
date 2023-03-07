from scribes.terminal_scribe import TerminalScribe
from canvases.canvas import Canvas
import random


"""
For Challenge 4 we need to create a data structure which defines some number of scribes with instructions for them
Then we are to create a function that has each scribe carry out its task.
"""

if __name__ == '__main__':
    n_scribes = 3
    n_moves = 5
    canvas_size = 30
    scribes = []
    scribe_directions = []

    # Generate scribe data
    for i in range(n_scribes):
        start_pos = [random.randint(0, canvas_size-1), random.randint(0, canvas_size-1)]
        scribes.append(TerminalScribe(start_pos))
        for j in range(n_moves):
            scribes[i].moves.append([random.randint(0, 180), random.randint(3, 6)])

    canvas = Canvas(30, 30, scribes)
    canvas.go()
