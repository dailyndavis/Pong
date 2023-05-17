# Create the screen > height = 600, width = 800, background black
# Create and move a paddle 
# Create another paddle
# Create the ball and make it move 
# Detect collision with wall and bounce
# Detect collision with paddle 
# Detect when paddle misses 
# Keep score 

from turtle import Screen, Turtle
from paddle import LeftPaddle, RightPaddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = RightPaddle()
l_paddle = LeftPaddle()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move_ball()
    # Detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_off_wall()
        
    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320: 
        ball.bounce_off_paddle()
        ball.increase_ball_speed()

    # Detect R paddle miss: 
    if ball.xcor() > 400: 
        ball.reset_ball()
        scoreboard.l_point()

    # Detect L paddle miss: 
    if ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.r_point()

screen.exitonclick()