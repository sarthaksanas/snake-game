from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, 280)
        self.color("white")
        self.penup()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 8, "normal"))


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 8, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 8, "normal"))

