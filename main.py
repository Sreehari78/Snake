from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import ScoreBoard
from time import sleep


screen = Screen()
screen.tracer(0)
screen.setup(width=610, height=610)
screen.title("Snake")
screen.bgcolor("black")


snape_the_snake = Snake()
snake_food = Food()
my_score = ScoreBoard()
screen.listen()

screen.onkey(fun=snape_the_snake.up, key="Up")
screen.onkey(fun=snape_the_snake.down, key="Down")
screen.onkey(fun=snape_the_snake.left, key="Left")
screen.onkey(fun=snape_the_snake.right, key="Right")

is_game_on = True

while is_game_on:
    screen.update()
    sleep(0.05)
    snape_the_snake.move()

    # Detect collision with food
    if snape_the_snake.head.distance(snake_food) < 10:
        snake_food.refresh_position()
        snape_the_snake.extend_snake()
        my_score.update_score()

    # Detect collision with walls
    if snape_the_snake.head.xcor() > 290 or snape_the_snake.head.xcor() < -290 or \
            snape_the_snake.head.ycor() > 290 or snape_the_snake.head.ycor() < -290:
        my_score.reset_score()
        snape_the_snake.reset_snake()

    # Detect collision with tail
    for segment in snape_the_snake.segments[1:]:
        if snape_the_snake.head.distance(segment) < 5:
            my_score.reset_score()
            snape_the_snake.reset_snake()

screen.exitonclick()
