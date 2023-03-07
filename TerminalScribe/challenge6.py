from scribes.function_scribe import FunctionScribe
from canvases.canvas_axes import AxesCanvas
import math

"""
For this challenge, the goal is to modify the Terminal scribe so that it will plot a function you pass into it.
The terminal scribe should cycle through the X-axis values (based on size of Canvas) and use the function 
passed in to get the corresponding y-value.
"""


# Functions to be passed into the scribe to be plotted
def sq_function(x):

    return x


def sin_function(x):

    return math.sin(x) + 1


if __name__ == '__main__':
    scribe = FunctionScribe([0, 0], sin_function)

    c_size = 30
    canvas = AxesCanvas(c_size, c_size, [scribe])

    # Plot the function
    canvas.construct_function_plot()

