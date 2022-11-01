from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(900, 600)
screen.title('PONG')
screen.tracer(0)

paddle1 = Paddle(400)
paddle2 = Paddle(-400)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(paddle1.up, 'Up')
screen.onkey(paddle1.down, 'Down')
screen.onkey(paddle2.up, 'w')
screen.onkey(paddle2.down, 's')
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    ball.wallcollider()

    # paddle collision
    if ball.xcor() > 370 or ball.xcor() < -370:
        if ball.distance(paddle1) < 50 or ball.distance(paddle2) < 50:
            ball.x_direction = - ball.x_direction

    # R out of bounds
    if ball.xcor() > 430:
        ball.reset_position()
        ball.x_direction = - ball.x_direction
        scoreboard.increase_l()

    if ball.xcor() < -430:
        ball.reset_position()
        ball.x_direction = - ball.x_direction
        scoreboard.increase_r()

screen.exitonclick()
