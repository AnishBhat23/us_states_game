from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.hideturtle()
        self.penup()


    def display_score(self,x,y,state):
        self.goto(x, y)
        self.write(arg=f"{state}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
