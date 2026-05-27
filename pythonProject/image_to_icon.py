from tkinter import *
from PIL import Image
from tkinter import filedialog

# Setting up our application
app = Tk()
app.title('Image to Icon')


# Functions to be used in our app
def open_image():
    # noinspection PyGlobalUndefined
    global img
    app.image_dir = filedialog.askopenfilename(initialdir='C:', filetypes=(
        ('PNG Images', '*.png'), ('JPG Images', '*.jpg'), ('JPEG Images', '*.jpeg'))
                                               )
    img = Image.open(app.image_dir)


def convert_img():
    img.save(f'{file_name.get()}.ico', format='ICO', sizes=[(iconSize.get(), iconSize.get())])
    success_window = Toplevel()
    success_window.title('Image converted successfully')
    msg = Label(success_window, text='Conversion Successful')
    msg.pack()
    success_window.mainloop()


def img_preview():
    prev = Toplevel()
    prev.title('Icon Preview')
    prev.iconbitmap(f'{file_name.get()}.ico')
    msg = Label(prev, text='Checkout your icon!')
    msg.pack()
    prev.mainloop()


# Choosing the image from user
lbl1 = Label(app, text='Select your Image: ')
lbl1.grid(row=0, column=0)
chooseBtn = Button(app, text='Choose', command=open_image)
chooseBtn.grid(row=0, column=1)

# Selecting the size of icon
iconSize = IntVar()
sizes = [16, 24, 32, 48, 64, 128, 255]
iconSize.set(32)
lbl2 = Label(app, text='Choose the size')
lbl2.grid(row=1, column=0)
iconSizeMenu = OptionMenu(app, iconSize, *sizes)
iconSizeMenu.grid(row=1, column=1)

# Naming our icon
lbl3 = Label(app, text='Enter the icon name: ')
lbl3.grid(row=2, column=0)
file_name = Entry(app)
file_name.grid(row=2, column=1)

# Creating the convert and preview button
convertBtn = Button(app, text='Convert', command=convert_img)
convertBtn.grid(row=3, column=0)
previewBtn = Button(app, text='Preview', command=img_preview)
previewBtn.grid(row=3, column=1)
app.mainloop()
