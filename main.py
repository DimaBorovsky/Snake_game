from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")

score = 0


game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food) < 15:
        food.regenerate()
        scoreboard.increase_score()


screen.exitonclick()
