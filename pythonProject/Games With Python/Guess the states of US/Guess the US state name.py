import turtle as t
import pandas as pd
screen = t.Screen()
screen.title("Guess the US states")
# Changing the turtle shape as our image
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)
# Reading our states csv file
states_file = pd.read_csv("50_states.csv")
no_of_states = 50
states_guessed = 0
states_of_us = list(states_file["state"])
# Game main logic
while no_of_states != 0:
    answer_state = t.textinput(title="Guess the state", prompt=f"{states_guessed}/50,Guess the state?").title()
    if answer_state == "Exit":
        break
    for states in states_file["state"]:
        if answer_state == states:
            states_of_us.remove(answer_state)
            series = states_file[(states_file['state'] == answer_state)]
            x = list(series["x"])
            y = list(series["y"])
            new_t = t.Turtle()
            new_t.hideturtle()
            new_t.penup()
            new_t.goto(x[0], y[0])
            new_t.write(answer_state, align="center", font=("Courier", 8, "normal"))
            no_of_states -= 1
            states_guessed += 1
        else:
            pass
print("The states you missed are:")
for i in states_of_us:
    print(i)
