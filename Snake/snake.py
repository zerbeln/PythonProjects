import turtle


class Snake(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.body = []  # This will contain a list of the coordinates that define our snake (the dots)
        self.actions = {  # Actions associated with snake directions
            "up": (0, 20),
            "down": (0, -20),
            "left": (-20, 0),
            "right": (20, 0)
        }
        self.snake_direction = "right"

    def add_to_body(self, x, y):
        """
        Adds segment to the snake
        """
        self.body.append([x, y])

    def print_snake(self):
        """
        print each segment of the snake to the screen
        """
        for segment in self.body:
            self.goto(segment[0], segment[1])
            self.stamp()

    def set_snake_direction(self, direction):
        """
        Set the snake's direction based on key inputs
        """
        if direction == "up" and self.snake_direction != "down":
            self.snake_direction = "up"
        elif direction == "down" and self.snake_direction != "up":
            self.snake_direction = "down"
        elif direction == "right" and self.snake_direction != "left":
            self.snake_direction = "right"
        elif direction == "left" and self.snake_direction != "right":
            self.snake_direction = "left"
        else:
            pass

    def check_collisions(self, new_head):
        """
        Check for snake collisions with itself or boundaries
        """
        if new_head in self.body:
            return True
        elif new_head[0] < -self.screen.window_width()/2 or new_head[0] > self.screen.window_width()/2:
            return True
        elif new_head[1] < -self.screen.window_height()/2 or new_head[1] > self.screen.window_height()/2:
            return True
        else:
            return False
