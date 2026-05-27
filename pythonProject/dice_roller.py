from tkinter import *
import random

# Die unicode symbols
die = {
    0: '🎲',
    1: '⚀',
    2: '⚁',
    3: '⚂',
    4: '⚃',
    5: '⚄',
    6: '⚅'
}

# Setting up our application
app = Tk()
app.title('Dice roller')
app.geometry('250x200')

# Setting up our initial display
initialDis = Label(app, text=die[0], font=('Times', 100))
initialDis.grid(row=0, column=0, padx=50)


# Rolling the die
def displayDie():
    die_number = random.randint(1, 6)
    msg = Label(app, text=die[die_number], font=('Times', 100), width=2)
    msg.grid(row=0, column=0, padx=50)


# Button to roll the die
roller_btn = Button(app, text='Roll', command=displayDie)
roller_btn.grid()
app.mainloop()
