from snake import Snake
import turtle
import time


if __name__ == '__main__':
    screen_height = 500
    screen_width = 500
    time_delay = 0.75  # seconds
    screen = turtle.Screen()
    screen.setup(screen_width, screen_height)
    screen.title("Snake Game")
    screen.bgcolor("blue")
    screen.tracer(0)  # Turns off automatic animations

    # Define the snake
    snake = Snake()
    snake.color("white")
    snake.shape("circle")
    snake.shapesize(10 / 20)  # Number of Pixels you want / 20 (default size)
    snake.penup()

    snake.body = [[0, 0], [20, 0], [40, 0]]
    snake.print_snake()

    # Draw the snake
    for i in range(6):
        snake.move_snake()
        screen.update()
        time.sleep(time_delay)

    turtle.done()

