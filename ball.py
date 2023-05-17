from turtle import Turtle 
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("cadetblue")
        self.penup()
        self.x_speed = 1
        self.y_speed = 1

    def move_ball(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(new_x, new_y)
    
    def bounce_off_wall(self):
        self.y_speed *= -1

    def bounce_off_paddle(self):
        self.x_speed *= -1

    def reset_ball(self):
        self.goto(0,0)
        self.bounce_off_paddle()

    def increase_ball_speed(self):
        self.x_speed += .05
        self.y_speed += .05