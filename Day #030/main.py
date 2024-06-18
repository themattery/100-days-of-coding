# Updated password manager from day 29
# Now able to deal with exception errors 
# and json data
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Attention!", message="You left an untouched entry!")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            print("File not found.")
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            # Updating olda data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)

        finally:  
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    # 1. get hold of entry
    website = website_entry.get()
    # 2. get hold of data.json data
    try:
        with open("data.json", "r") as data_file:
            # 3. check if entry is in data.json
            data = json.load(data_file)
    except FileNotFoundError:
        # 5. in case data file not found, get exception error messagebox "No data file found"
        messagebox.showinfo(title="Alert", message="File Not Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            # 4. if so, show website name & password in messagebox
            messagebox.showinfo(title="Your data", message=f"Website: {website}\nEmail: {email}\nPassword: {password}")
        else:
            # 6. if website not found, show messagebox "no details for the website exists"
            messagebox.showinfo(title="Attention!", message="No details for the website exists.")  

        

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(window, width=200, height=200) # highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_lb = Label(text="Website: ")
website_lb.grid(column=0, row=1)

email_lb = Label(text="Email/Username: ")
email_lb.grid(column=0, row=2)

password_lb = Label(text="Password: ")
password_lb.grid(column=0, row=3)

# Entries
website = StringVar()
website_entry = Entry(width=35, textvariable=website)
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "email@email.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons
search_btn = Button(text="Search", command=find_password)
search_btn.grid(column=2, row=1, sticky="EW")

generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(column=2, row=3, sticky="EW")

add_user_btn = Button(text="Add", width=36, command=save)
add_user_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
