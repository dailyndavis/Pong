from turtle import Turtle 

MOVE_DISTANCE = 20 

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid= 5, stretch_len= 1)
        self.penup()

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

class LeftPaddle(Paddle):
    def __init__(self):
        super().__init__()
        starting_x = -350
        starting_y = 0
        self.setpos(x=starting_x, y=starting_y)

class RightPaddle(Paddle):
    def __init__(self):
        super().__init__()
        starting_x = 350
        starting_y = 0
        self.setpos(x=starting_x, y=starting_y)