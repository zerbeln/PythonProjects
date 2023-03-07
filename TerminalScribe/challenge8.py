from scribes.terminal_scribe import TerminalScribe
from canvases.canvas import Canvas

"""
The purpose of this challenge is to get familiar with defining and using custom exceptions 
"""

if __name__ == '__main__':
    scribe = TerminalScribe([0, 0])
    canvas = Canvas(5, 5, [scribe])

    scribe.draw([10, 10], canvas)
