from turtle import *
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detecting collision with food
    if snake.head.distance(food) < 15 :
        new_x = food.xcor()
        new_y = food.ycor()
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detecting collision with wall
    if snake.head.xcor()>380 or snake.head.xcor()<-380 or snake.head.ycor()>380 or snake.head.ycor()<-380:
        game_is_on = False
        scoreboard.game_over()

    #detecting collision with own tail
    for seg in snake.segments:
        if snake.head  == seg:
            pass
        elif snake.head.distance(seg) < 10 :
            game_is_on = False
            scoreboard.game_over()








screen.exitonclick()