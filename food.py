from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("brown")
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))
