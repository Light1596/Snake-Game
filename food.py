from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(1, 1)
        self.color("green")
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        x_value = random.randint(-280, 280)
        y_value = random.randint(-280, 280)
        self.goto(x_value, y_value)
