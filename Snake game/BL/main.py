import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake(length_of_snake=3)
food = Food()
scoreboard = Scoreboard()

# Listening to the events triggered by keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main Game Loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    # collision detection with food
    if snake.snake_head.distance(food) < 20:
        food.refresh_location()
        snake.increase_segment()
        scoreboard.increase_score()

    # collision detection with tail
    for segment in snake.snake_segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_is_on = False
            scoreboard.set_high_score()
            scoreboard.game_over()

screen.exitonclick()
