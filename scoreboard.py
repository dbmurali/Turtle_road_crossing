from turtle import  Turtle



FONT = ("Arial", 24, "bold")
ALIGN="center"


class Scoreboard(Turtle):
     def __init__(self):
         super().__init__()
         self.score=0
         self.clear()
         self.penup()
         self.hideturtle()
         self.color("white")

     def create_score(self):
         self.clear()
         self.goto(-170, 250)
         self.write(f"Level: {self.score}", align=ALIGN, font=FONT)


     def add_score(self):
         self.score+=1
         self.create_score()


     def start_screen(self):
         self.clear()

         self.penup()
         self.goto(0, 0)
         self.color("white")

         self.write("Welcome to Turtle Cross",align=ALIGN,font=FONT)




     def game_over(self):
         #self.clear()
         self.goto(0,0)
         self.write("GAME OVER",align=ALIGN,font=FONT)



