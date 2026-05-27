# Turtle Race
import turtle as t
import random

my_screen = t.Screen()
my_screen.setup(width=600, height=400)
user_bet = my_screen.textinput(
    title="Make your bet",
    prompt=
    "Who will win the race?Enter the colour?Green,Red,Blue,Purple or Cyan")
t.penup()
t.goto(300, 300)
t.pendown()
t.right(90)
for _ in range(35):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()

#Player_1 Turtle starting position
green = t.Turtle()
green.color("green")
green.shape("turtle")
green.penup()
green.goto(-200, 100)

#Player_2 Turtle starting position
red = green.clone()
red.color("red")
red.shape("turtle")
red.penup()
red.goto(-200, 50)

#Player_3 Turtle starting position
blue = green.clone()
blue.color("blue")
blue.shape("turtle")
blue.penup()
blue.goto(-200, 0)
dice = [1, 2, 3, 4, 5, 6]

#Player_4 Turtle starting position
purple = green.clone()
purple.color("Purple")
purple.shape("turtle")
purple.penup()
purple.goto(-200, -50)

#Player_4 Turtle starting position
cyan = green.clone()
cyan.color("Cyan")
cyan.shape("turtle")
cyan.penup()
cyan.goto(-200, -100)

winner = ""
for i in range(20):
    if green.pos() >= (300, 100):
        winner = "Green"
        break
    elif red.pos() >= (300, 50):
        winner = "Red"
        break
    elif blue.pos() >= (300, 0):
        winner = "Blue"
        break
    elif purple.pos() >= (300, -50):
        winner = "Purple"
        break
    elif cyan.pos() >= (300, -100):
        winner = "Cyan"
        break
    else:
        gen = random.choice(dice)
        dice_1 = gen * 10
        green.forward(dice_1)
        gen = random.choice(dice)
        dice_2 = gen * 10
        red.forward(dice_2)
        gen = random.choice(dice)
        dice_3 = gen * 10
        blue.forward(dice_3)
        gen = random.choice(dice)
        dice_4 = gen * 10
        purple.forward(dice_4)
        gen = random.choice(dice)
        dice_5 = gen * 10
        cyan.forward(dice_5)

if user_bet == winner:
    print(f"You Win.{winner} turtle is the winneer")
else:
    print(f"Your Lose.{winner} turtle is the winner")
my_screen.exitonclick()
