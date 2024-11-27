import random
from turtle import Turtle



COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars=[]

    def create(self):
        chance_of_car=random.randint(1,4)
        if chance_of_car ==1:
            car=Turtle("square")
            car.shapesize(1,2)
            car.penup()
            car.color(random.choice(COLORS))
            y=car.ycor()+random.randint(-250,600)
            car.goto(305,y)
            self.all_cars.append(car)

    def move(self):
        for i in self.all_cars:
            x=i.xcor()-STARTING_MOVE_DISTANCE
            y=i.ycor()
            i.goto(x,y)
            self.all_cars=[car for car in self.all_cars if car.xcor() >=-350]















