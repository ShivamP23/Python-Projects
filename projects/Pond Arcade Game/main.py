from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(800,600) 
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Score()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
 
game_is_on = True
winning_score = 10
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    if ball.xcor()  > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

    if score.l_score == winning_score:
            score.game_over("Left")  # Left player won
            game_is_on = False
    elif score.r_score == winning_score:
            score.game_over("Right")  # Right player won
            game_is_on = False

screen.exitonclick()



