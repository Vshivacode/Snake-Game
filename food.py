from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):             # Food __init__ method
        super().__init__()          # Turtle __init__ method
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)      # Food size in float
        self.color("blue")
        self.speed("fastest")           # speed is used because we dont want the food to be animated slowly
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-280, 280)# (-280,280) used so that food position will not be outside screen
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)
