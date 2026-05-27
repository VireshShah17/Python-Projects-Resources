# Snake Game With Python

import turtle as t
from turtle import Turtle
import random
import time

# Setting up the screen
screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Welcome to the Snake Game")
screen.tracer(0)
screen.listen()

starting_positions = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # Designing the snake's body
        for position in starting_positions:
            self.add_segment(position)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move_snake(self):
        # Animating the snake's body
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

        def turn_up():
            if self.segments[0].heading() != 270:
                self.segments[0].setheading(90)

        def turn_left():
            if self.segments[0].heading() != 0:
                self.segments[0].setheading(180)

        def turn_right():
            if self.segments[0].heading() != 180:
                self.segments[0].setheading(0)

        def turn_down():
            if self.segments[0].heading() != 90:
                self.segments[0].setheading(270)

        screen.onkey(key="Left", fun=turn_left)
        screen.onkey(key="Right", fun=turn_right)
        screen.onkey(key="Down", fun=turn_down)
        screen.onkey(key="Up", fun=turn_up)

    def add_segment(self, position):
        new_segment = t.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # Extending the snake body
        self.add_segment(self.segments[-1].position())


# Generating the food
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update()
        self.hideturtle()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}", align="center", font=("Courier", 24, "normal"))

    def inc_scr(self):
        self.score += 1
        self.update()


snake = Snake()
food = Food()
scoreboard = ScoreBoard()
snake.create_snake()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.inc_scr()
    if (snake.segments[0].xcor() > 300) or (snake.segments[0].xcor() < -300) or \
            (snake.segments[0].ycor() > 300) or (snake.segments[0].ycor() < -300):
        scoreboard.reset()
        snake.reset()
    for seg in snake.segments:
        if seg == snake.head:
            continue
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()
t.color("white")
t.write("Game Over!", align="center", font=("Courier", 24, "normal"))
screen.exitonclick()
