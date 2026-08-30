from turtle import Turtle,Screen
from time import sleep
from snake import Snake


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")

score = 0

screen.title("My Snake Game")
screen.tracer(n=1,delay=5)
 



game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.2)

    snake = Snake()
    snake.move_snake(snake_body=snake.create_snakes())

screen.exitonclick()