from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 25, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 360)
        self.get_high_score()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGN, font=FONT)

    def get_high_score(self):
        with open("../Files/data.txt") as file:
            self.high_score = int(file.read())

    def set_high_score(self):
        if self.score > self.high_score:
            with open("../Files/data.txt", "w") as file:
                file.write(f"{self.score}")
