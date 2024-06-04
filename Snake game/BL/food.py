import random
from turtle import Turtle, Screen
image = "../Files/apple.gif"
s = Screen()
s.addshape(image)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(image)
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("green")
        self.speed("fastest")
        self.refresh_location()

    def refresh_location(self):
        random_x = random.randint(-370, 370)
        random_y = random.randint(-370, 370)
        self.goto(random_x, random_y)
