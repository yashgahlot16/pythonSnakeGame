from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,370)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(arg=f"Score : {self.score}",  align="center", font=("Arial", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER !", align="center", font=("Arial", 20, "normal"))





