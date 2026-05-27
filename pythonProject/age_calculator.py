from tkinter import *
from datetime import *


# Functions to be used in our app
def find_days():
    bdate = int(date_inp.get())
    mon = int(month_inp.get())
    yr = int(month_inp.get())
    if bdate > 31 or mon > 12:
        error_lbl = Label(app, text=f'Please enter the birth date or month number correctly')
        error_lbl.grid(row=3, column=1, columnspan=4)
    else:
        time_diff = datetime.now() - datetime(day=bdate, month=mon, year=yr)
        days_lived = Label(app, text=f'You lived {time_diff.days} days')
        days_lived.grid(row=3, column=1, columnspan=4)


def find_seconds():
    bdate = int(date_inp.get())
    mon = int(month_inp.get())
    yr = int(month_inp.get())
    if bdate > 31 or mon > 12:
        error_lbl = Label(app, text=f'Please enter the birth date or month number correctly')
        error_lbl.grid(row=3, column=1, columnspan=4)
    else:
        time_diff = datetime.now() - datetime(day=bdate, month=mon, year=yr)
        days_lived = Label(app, text=f'You lived {time_diff.days} days')
        days_lived.grid(row=3, column=1, columnspan=4)


# Setting up our application
app = Tk()
app.title("Age Calculator")
# Adding our message to app
msg1 = Label(app, text='Enter your DOB')
msg1.grid(row=0, column=0)

# Inputting the date
msg2 = Label(app, text='Date: ')
msg2.grid(row=1, column=0)
date_inp = Entry(app, width=2)
date_inp.grid(row=1, column=1)

# Inputting the month
msg3 = Label(app, text='Month: ')
msg3.grid(row=1, column=2)
month_inp = Entry(app, width=2)
month_inp.grid(row=1, column=3)

# Inputting the year
msg4 = Label(app, text='Year: ')
msg4.grid(row=1, column=4)
year_inp = Entry(app, width=4)
year_inp.grid(row=1, column=5)

# Adding the buttons
year_btn = Button(app, text='Total Days', command=find_days)
year_btn.grid(row=2, column=0)
seconds_btn = Button(app, text='Total Seconds', command=find_seconds)
seconds_btn.grid(row=2, column=3)
app.mainloop()
