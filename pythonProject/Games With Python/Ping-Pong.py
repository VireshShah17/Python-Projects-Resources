# Ping Pong Game

import turtle as t
from turtle import Turtle
import time

# Setting up the game screen


screen = t.Screen()
screen.setup(width=800, height=600)
screen.title("Ping-Pong Game")
screen.bgcolor("black")
screen.listen()
screen.tracer(0)


# Making the paddles and making them move


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(self.x, self.y)
        self.shapesize(stretch_len=1, stretch_wid=5)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


# Creating and moving the ball
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.x_move *= -1
        self.move_speed *= 0.9


# Keeping the track of score
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(f"{self.r_score}", align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()


paddle1 = Paddle(350, 0)
paddle2 = Paddle(-350, 0)
ball = Ball()
score = Score()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    # Detecting the collisions
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Hitting ball with paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.hit()

    # Checking ball that it passed your paddle
    if ball.xcor() > 370:
        ball.goto(0, 0)
        ball.move_speed = 0.1
        ball.hit()
        score.l_point()

    if ball.xcor() < -370:
        ball.goto(0, 0)
        ball.move_speed = 0.1
        ball.hit()
        score.r_point()

    screen.update()
screen.exitonclick()
