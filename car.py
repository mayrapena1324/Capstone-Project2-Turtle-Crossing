#TODO: get a new car to generate if it is too close to another car
COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
SPEED = 10

from turtle import Turtle
import random


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed = SPEED
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        random_num = random.randint(0, 6)
        self.color(COLORS[random_num])
        random_y = random.randint(-230, 260)
        random_x = random.randint(-300, 300)
        self.goto(x=random_x, y=random_y)

    def move(self):
        self.backward(self.speed)

    def speed_up(self):
        self.speed += 5

    def reset_car(self):
        random_num = random.randint(0, 6)
        self.color(COLORS[random_num])
        random_y = random.randint(-230, 260)
        self.goto(x=300, y=random_y)
