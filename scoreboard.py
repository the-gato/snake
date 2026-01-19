from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 14, "normal"))
    
    def increase_score(self):
        self.score += 1

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 14, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 14, "normal"))

