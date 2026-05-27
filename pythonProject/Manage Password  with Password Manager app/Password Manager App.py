from tkinter import *
import random
from tkinter import messagebox
import json


# Function to add the data entered by the user to his local disk's


def add_data():
    web_name = entry1.get()
    user_name = entry2.get()
    user_pass = entry3.get()
    new_data = {web_name: {'email': user_name, 'password': user_pass}}
    # Checking if there are any empty fields or not
    if len(web_name) == 0 or len(user_name) == 0 or len(user_pass) == 0:
        messagebox.showinfo(title="Empty field", message="Fields can't be left empty")
    else:
        # Message box to confirm users entry
        is_ok = messagebox.askokcancel(title="Confirm Your Inputs",
                                       message=f"{web_name}\n{user_name}\n{user_pass}\nIs it ok to save?")
        if is_ok:
            try:
                with open("passwords.json") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open(file="passwords.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("passwords.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                entry1.delete(0, END)
                entry3.delete(0, END)


# Function to generate user's random password
def random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    ran_pass = "".join(password_list)
    entry3.insert(END, ran_pass)


# Function to search an existing password
def search_password():
    email = entry1.get()
    try:
        with open("passwords.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="File Not Found", message="No file existed to store the password please Add first")
    else:
        if email in data:
            em = data[email]['email']
            pass_word = data[email]['password']
            messagebox.showinfo(title="Your Password", message=f"Email:{em}\nPassword:{pass_word}")
        else:
            messagebox.showinfo(title="Password Not Found", message="No password saved for that website")


# Setting up the user interface
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
window.minsize(width=600, height=420)

# Adding logo to our app
canvas = Canvas(width=200, height=200)
l_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=l_image)
canvas.pack()

# Adding the website entry function to our app
website = Label(text="Website:", font=("Times new roman", 15, "normal"))
website.place(x=100, y=200)
entry1 = Entry(width=30)
entry1.place(x=210, y=205)
entry1.focus()

# Adding a search to button to search for a existing password
search = Button(text="Search Password", font=("Times new roman", 10, "normal"), command=search_password)
search.place(x=400, y=205)

# Adding email/username entry function to our app
u_name = Label(text="E-mail/Username:", font=("Times new roman", 15, "normal"))
u_name.place(x=40, y=250)
entry2 = Entry(width=50)
entry2.insert(0, "vireshshah@gmail.com")
entry2.place(x=210, y=250)

# Adding Password entry function to our app
password = Label(text="Password:", font=("Times new roman", 15, "normal"))
password.place(x=100, y=295)
entry3 = Entry(width=25)
entry3.place(x=210, y=295)

# Adding a random password generator button
paa_gen = Button(text="Generate Password", font=("Times new roman", 10, "normal"), width=21, command=random_password)
paa_gen.place(x=400, y=290)

# Adding a button to save the user's password
add = Button(text="Add", font=("Times new roman", 15, "normal"), width=36, command=add_data)
add.place(x=100, y=345)
window.mainloop()
