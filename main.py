import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player=Player()
score=Scoreboard()
cars=CarManager()

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player.create()
score.start_screen()



screen.onkey(player.move,"Up")

def run_game():
    car_sleep = 0.1
    game_is_on = True
    score.create_score()

    while game_is_on:


        time.sleep(car_sleep)
        cars.create()
        cars.move()
        screen.update()
        for i in cars.all_cars:
          if player.distance(i)<15:
              player.color("red")
              time.sleep(1)
              game_is_on=False
              score.game_over()
          if player.ycor()>300:
              print("player reached end")
              player.goto(0,-280)
              score.add_score()
              car_sleep *=0.9
              time.sleep(car_sleep)
              cars.move()


screen.onkey(run_game,"w")

screen.exitonclick()