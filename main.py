from turtle import Screen
from player import Player
from score import Score
from car import Car
import time

NUMBER_OF_CARS = 15

screen = Screen()
screen.title("Welcome to Crossy Turtle!")
screen.screensize(canvwidth=600, canvheight=600)
screen.tracer(0)

player = Player()
score = Score()

screen.listen()
screen.onkey(player.up, "Up")

# Makes a finite amount of cars
all_cars = []
for _ in range(NUMBER_OF_CARS):
    car = Car()
    all_cars.append(car)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Move all cars
    for car in range(len(all_cars)):
        all_cars[car].move()
        # detect collision with car, game over
        if player.distance(all_cars[car]) < 20:
            game_is_on = False
            score.game_over()
        # detect if car goes past -300 and reset to start at beginning
        if all_cars[car].xcor() < -325:
            all_cars[car].reset_car()

    # detect collision with top of wall and level up
    if player.ycor() > 270:
        player.reset_turtle()
        score.next_level()
        # only one car was getting updated, so I looped again to get all cars to speed up
        for car in range(len(all_cars)):
            all_cars[car].speed_up()


screen.exitonclick()
