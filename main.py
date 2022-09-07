from turtle import Screen

from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

DIFFICULTY = 0.1


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("lightblue")
screen.title("Snake Game by Turtle")
screen.tracer(0) # enable tracer to force update

snake = Snake()
food = Food()
score = Scoreboard()

# Use the screen's default onkey functions.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Start the game
game_on = True


while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # get the food
    if snake.head.distance(food) < 15:
        food.refresh_food()
        score.add_score()
        snake.extend()

    # wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        # score.reset_scoreboard()
        # snake.reset_snake()

    # tail collision
    for body_part in snake.body[1:]:
        if snake.head.distance(body_part) < 10:
            game_on = False
            # score.reset_scoreboard()
            # snake.reset_snake()
            # break

score.game_over()
screen.exitonclick()



