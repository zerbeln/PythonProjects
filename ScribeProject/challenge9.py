from scribes.terminal_scribe import TerminalScribe
from canvases.canvas import Canvas

"""
The goal of this challenge is to become familiar with threading in Python.
"""


if __name__ == '__main__':
    scribe1 = TerminalScribe([1, 1])
    scribe1.get_moves([180, 5])
    scribe1.get_moves([90, 5])
    scribe2 = TerminalScribe([6, 6])
    scribe2.get_moves([0, 5])
    scribe2.get_moves([270, 5])

    scribes = [scribe1, scribe2]

    canvas = Canvas(30, 30, scribes)
    canvas.go()
