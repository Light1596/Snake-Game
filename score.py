from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.total_score = 0
        self.penup()
        self.goto(0,280)
        self.write(f"YOU SCORE : {self.total_score}", align="center", font=('Arial', 10, 'normal'))
        self.hideturtle()

    def check_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.",align="center", font=('Arial', 15, 'bold'))

    def score_increase(self):
        self.total_score += 1
        self.clear()
        self.write(f"YOU SCORE : {self.total_score}", align="center", font=('Arial', 10, 'normal'))

