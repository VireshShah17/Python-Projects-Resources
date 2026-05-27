from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"


# Function to get the new card


def new_card():
    global random_index, text, flip_timer
    window.after_cancel(flip_timer)
    random_index = random.randint(0, len(df) - 1)
    text = df[random_index]
    canvas.itemconfig(title, text='French', fill="black")
    canvas.itemconfig(text1, text=text['French'], fill="black")
    canvas.itemconfig(img, image=fcd_image)
    flip_timer = window.after(3000, func=flip_card)


# Function to flip the card after 3 seconds


def flip_card():
    canvas.itemconfig(img, image=bdc_image)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(text1, text=text['English'], fill="white")


# Function to remove the known cards


def is_known():
    df.remove(df[random_index])
    new_card()
    data = pd.DataFrame(df)
    data.to_csv("words_to_learn.csv", index=False)


# Reading from the csv file
df = {}
try:
    file_data = pd.read_csv("words_to_learn.csv")
    df = file_data.to_dict(orient="records")
except FileNotFoundError:
    file_data = pd.read_csv("french_words.csv")
    df = file_data.to_dict(orient="records")
finally:
    random_index = random.randint(0, len(df) - 1)
    text = df[random_index]

# User Interface setup
window = Tk()
window.title("French FlashCard")
window.minsize(width=800, height=700)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Displaying the front Image
canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
fcd_image = PhotoImage(file="card_front.png")
bdc_image = PhotoImage(file="card_back.png")
img = canvas.create_image(400, 263, image=fcd_image)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
text1 = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.pack()

# Displaying the cross button
cross_img = PhotoImage(file="wrong.png")
cross_button = Button(image=cross_img, border=0, bg=BACKGROUND_COLOR, command=new_card)
cross_button.place(x=50, y=550)

# Displaying the right button
right_img = PhotoImage(file="right.png")
right_button = Button(image=right_img, border=0, bg=BACKGROUND_COLOR, command=is_known)
right_button.place(x=650, y=550)
new_card()
window.mainloop()
