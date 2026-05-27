from tkinter import *


# Constants to be used in our program
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
counter = None

# Creating the countdown mechanism


def count_down(count):
    mint = int(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{mint}:{sec}")
    if count > 0:
        global counter
        counter = window.after(1000, count_down, count-1)
    else:
        start_countdown()

# Start Countdown


def start_countdown():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Long Break", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Short Break", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))

# Function to reset timer


def reset_timer():
    window.after_cancel(counter)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")


# UI Setup
window = Tk()
window.title("Pomodoro Technique App")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=225, bg=YELLOW, highlightthickness=0)
t_image = PhotoImage(file="Pomodoro Technique App IMG.png")
canvas.create_image(100, 112.5, image=t_image)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")

# Creating a heading label
timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
timer.place(x=50, y=-40)

# Creating the start button
start = Button(text="Start", command=start_countdown)
start.place(x=10, y=230)

# Creating the reset button
reset = Button(text="Reset", command=reset_timer)
reset.place(x=180, y=230)
canvas.pack()
window.mainloop()
