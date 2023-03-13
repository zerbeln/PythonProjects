import random
import turtle
import math


class SnakeGameEnvironment:
    def __init__(self, snake, screen):
        self.time_delay = 100
        self.snake = snake
        self.screen = screen
        self.score = 0

        # Food parameters
        self.food_size = 10 / 20  # Food is 10 pixels
        self.food = turtle.Turtle()
        self.food.color("white")
        self.food.shape("circle")
        self.food.shapesize(self.food_size)
        self.food.penup()
        self.food_pos = self.generate_food()
        self.food.goto(self.food_pos[0], self.food_pos[1])

    def calc_lin_dist(self, pos1, pos2):
        """
        Calculates the linear distance between two points
        """
        x_dist = pos1[0] - pos2[0]
        y_dist = pos1[1] - pos2[1]

        dist = math.sqrt(x_dist**2 + y_dist**2)

        return dist

    def generate_food(self):
        """
        Generate a food object somewhere on the map
        """
        x = random.randint(-self.screen.window_width()/2 + 20, self.screen.window_width()/2 - 20)
        y = random.randint(-self.screen.window_height()/2 + 20, self.screen.window_height()/2 - 20)

        # Prevent food from spawning inside the snake
        while [x, y] in self.snake.body:
            x = random.randint(-self.screen.window_width()/2 + 20, self.screen.window_width()/2 - 20)
            y = random.randint(-self.screen.window_height()/2 + 20, self.screen.window_height()/2 - 20)

        return [x, y]

    def check_food_collision(self):
        """
        Checks to see if the snake has collided with (eaten) food
        """
        if self.calc_lin_dist(self.snake.body[-1], self.food_pos) < 20:
            self.food_pos = self.generate_food()
            self.food.goto(self.food_pos[0], self.food_pos[1])
            self.score += 1  # Score goes up for snake eating food
            return True
        else:
            return False

    def reset_game(self):
        """
        Reset the game to initial state
        """
        self.score = 0
        self.snake.body = [[0, 0], [20, 0], [40, 0]]
        self.snake.snake_direction = "right"
        self.food_pos = self.generate_food()
        self.food.goto(self.food_pos[0], self.food_pos[1])

    def game_loop(self):
        """
        Main game loop where snake moves based on direction inputs.
        """
        self.snake.clearstamps()  # Clears existing stamps

        # Create new snake head along current direction
        new_head = self.snake.body[-1].copy()
        new_head[0] += self.snake.actions[self.snake.snake_direction][0]
        new_head[1] += self.snake.actions[self.snake.snake_direction][1]

        # Check for collisions
        if self.snake.check_collisions(new_head):
            self.reset_game()  # Reset game if a bad collision occurs
        else:
            # Add new head to snake's body
            self.snake.add_to_body(new_head[0], new_head[1])  # Add new snake head to body

            # Check for food Collisions
            if self.check_food_collision():
                pass  # Snake gets a segment added to it
            else:
                self.snake.body.pop(0)  # pop last segment of snake if it did not eat food

            # Redraw the snake
            self.snake.print_snake()
            self.screen.title(f'Snake Game. Score: {self.score}')
            self.screen.update()

        turtle.ontimer(self.game_loop, self.time_delay)
