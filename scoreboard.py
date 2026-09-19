from turtle import Turtle

class ScoreBoard(Turtle):


    def __init__(self):
        super().__init__()
        self.score  = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.ht()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} HighScore:{self.highscore}", align="center", font=("Arial", 24, "normal"))


    def reset(self):
        if self.score > self.highscore:
            self.highscore =self.score

        self.score = 0
        self.update_score()



    def increase_score(self):
        self.score += 1
        self.update_score()
