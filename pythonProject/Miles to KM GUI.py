from tkinter import *

# Setting up the screen
window = Tk()
window.title("Miles to KM converter")
window.minsize(width=300, height=50)
# Inputting the distance in Miles
mile = Entry(width=7)
mile.place(x=120, y=40)
# Printing the unit
text1 = Label(text="Miles", font=("Times New Roman", 15, "normal"))
text1.place(x=220, y=30)
# Printing the text for better understanding
text2 = Label(text="is equal to", font=("Times New Roman", 15, "normal"))
text2.place(x=10, y=80)
# Printing value of distance in KM's
km = Label(text=0, font=("Times New Roman", 15, "normal"))
km.place(x=130, y=80)
text3 = Label(text="K.M.", font=("Times New Roman", 15, "normal"))
text3.place(x=220, y=80)


# Function to calculate Miles into KM's
def mile_to_km():
    d_in_mile = float(mile.get())
    d_in_km = d_in_mile * 1.609
    km.config(text=d_in_km)


# Creating a Button to calculate
button = Button(text="Calculate", command=mile_to_km)
button.place(x=120, y=120)
window.mainloop()
