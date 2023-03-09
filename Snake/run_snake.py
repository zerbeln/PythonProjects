from snake import Snake
from game_environment import SnakeGameEnvironment
import turtle


if __name__ == '__main__':
    # Define Screen parameters
    screen_height = 500
    screen_width = 500
    screen = turtle.Screen()
    screen.setup(screen_width, screen_height)
    screen.title("Snake Game")
    screen.bgcolor("blue")
    screen.tracer(0)  # Turns off automatic animations

    # Define the snake parameters
    snake = Snake()
    snake.color("white")
    snake.shape("circle")
    snake.shapesize(10 / 20)  # Number of Pixels you want / 20 (default size)
    snake.penup()
    snake.body = [[0, 0], [20, 0], [40, 0]]
    snake.print_snake()

    # Event Handlers (Listens for arrow key presses to interact with snake)
    screen.listen()
    screen.onkey(lambda: snake.set_snake_direction("up"), "Up")
    screen.onkey(lambda: snake.set_snake_direction("down"), "Down")
    screen.onkey(lambda: snake.set_snake_direction("left"), "Left")
    screen.onkey(lambda: snake.set_snake_direction("right"), "Right")

    # Create instance of game
    game = SnakeGameEnvironment(snake, screen)
    game.game_loop()

    turtle.done()

