from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
     def __init__(self):
         super().__init__()

     def create(self):
         self.shape("turtle")
         self.color("blue")
         self.penup()
         self.setheading(90)
         self.goto(0,-280)

     def move(self):
         current_pos_y=self.ycor()+MOVE_DISTANCE
         current_pos_x=self.xcor()
         self.goto(current_pos_x,current_pos_y)


