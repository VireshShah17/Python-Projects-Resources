from tkinter import *

# Setting up our application
app = Tk()
app.title("Length Converter")
scales = ['Meters', 'Inches', 'Foot']


# Functions to be used
def converter():
    from_value = _from.get()
    to_value = _to.get()
    conversion_value = float(value_num.get())
    # Converting values from meter
    if from_value == 'Meters':
        if to_value == ' Meters':
            display_value = Label(app, text=conversion_value)
            display_value.grid(row=1, column=2)
        elif to_value == 'Inches':
            display_value = Label(app, text=conversion_value * 39.37)
            display_value.grid(row=1, column=2)
        else:
            display_value = Label(app, text=conversion_value * 3.28)
            display_value.grid(row=1, column=2)
    # Converting values from inches
    elif from_value == 'Inches':
        if to_value == 'Meters':
            display_value = Label(app, text=conversion_value * 0.0254)
            display_value.grid(row=1, column=2)
        elif to_value == 'Inches':
            display_value = Label(app, text=conversion_value)
            display_value.grid(row=1, column=2)
        else:
            display_value = Label(app, text=conversion_value * 0.0834)
            display_value.grid(row=1, column=2)
    # Converting values from foot
    else:
        if to_value == 'Meters':
            display_value = Label(app, text=conversion_value * 0.3048)
            display_value.grid(row=1, column=2)
        elif to_value == 'Inches':
            display_value = Label(app, text=conversion_value * 12)
            display_value.grid(row=1, column=2)
        else:
            display_value = Label(app, text=conversion_value)
            display_value.grid(row=1, column=2)


# Creating the from menu for conversion
_from = StringVar()
from_menu = OptionMenu(app, _from, *scales)
from_menu.grid(row=0, column=0)

to_label = Label(app, text='convert to', font=('Times', 15))
to_label.grid(row=0, column=1)

# Creating the to menu for conversion
_to = StringVar()
to_menu = OptionMenu(app, _to, *scales)
to_menu.grid(row=0, column=2)

# Creating the entry field
label1 = Label(app, text='Enter the number', font=('Times', 15))
label1.grid(row=1, column=0)
value_num = Entry(app)
value_num.grid(row=1, column=1)

# Creating the button
conversion_btn = Button(app, text='Convert', command=converter)
conversion_btn.grid()
app.mainloop()
