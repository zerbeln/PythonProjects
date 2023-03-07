import turtle

"""
This file will eventually contain code for the snake game!
"""


class Snake(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.body = []  # This will contain a list of the coordinates that define our snake (the dots)

    def add_to_body(self, x, y):
        """
        Adds segment to the snake
        """
        self.body.append([x, y])

    def print_snake(self):
        for segment in self.body:
            self.goto(segment[0], segment[1])
            self.stamp()

    def snake_left(self, snake_head):
        x = snake_head[0] - 20
        y = snake_head[1]

        return x, y

    def snake_right(self, snake_head):
        x = snake_head[0] + 20
        y = snake_head[1]

        return x, y

    def snake_up(self, snake_head):
        x = snake_head[0]
        y = snake_head[1] - 20

        return x, y

    def snake_down(self, snake_head):
        x = snake_head[0] + 20
        y = snake_head[1]

        return [x, y]

    def move_snake(self):
        self.clearstamps()  # Clears existing stamps
        new_head = self.snake_right(self.body[-1])
        self.add_to_body(new_head[0], new_head[1])
        self.body.pop(0)

        # Redraw the snake
        self.print_snake()
