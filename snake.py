from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snakes()

    def create_snakes(self):
        for position in STARTING_POSITIONS:
            new_snake = Turtle(shape="square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(position)
            self.snake_body.append(new_snake)




    def move_snake(self):
        for snake_num in range(len(self.snake_body) - 1, 0, -1):
            newx = self.snake_body[snake_num - 1].xcor()
            newy = self.snake_body[snake_num - 1].ycor()
            self.snake_body[snake_num].goto(newx, newy)

        self.snake_body[0].forward(MOVE_DISTANCE)


