from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP_TURN_ANGLE = 90
LEFT_TURN_ANGLE = 180
RIGHT_TURN_ANGLE = 0
DOWN_TURN_ANGLE = 270

class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snakes()
        self.head = self.snake_body[0]

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

        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN_TURN_ANGLE:
            self.head.setheading(UP_TURN_ANGLE)


    def down(self):
        if self.head.heading() != UP_TURN_ANGLE:
            self.head.setheading(DOWN_TURN_ANGLE)


    def right(self):
        if self.head.heading() != LEFT_TURN_ANGLE:
            self.head.setheading(RIGHT_TURN_ANGLE)

    def left(self):
        if self.head.heading() != RIGHT_TURN_ANGLE:
            self.head.setheading(LEFT_TURN_ANGLE)
