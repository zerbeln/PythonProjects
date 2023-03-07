import turtle


def draw_square(turt, size):
    """
    Turtle draws a square of a given size
    """

    turt.forward(size)
    turt.left(90)  # This is how much it turns in degrees (not direction of travel)
    turt.forward(size)
    turt.left(90)
    turt.forward(size)
    turt.left(90)
    turt.forward(size)

    turtle.done()


if __name__ == '__main__':
    width = 500
    height = 500
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.title("Turtle Test")
    screen.bgcolor("cyan")

    turt = turtle.Turtle()
    turt.shape("turtle")
    turt.color("red")

    # Getting familiar with turtle graphics module
    draw_square(turt, 100)

