
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

from random import choice,randint,shuffle

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letter =[choice(letters) for _ in range(nr_letters)]

    password_symbol =[choice(symbols) for _ in range(nr_symbols)]
    password_number = [ choice(numbers) for char in range(nr_numbers)]

    password_list = password_letter+password_symbol+password_number
    shuffle(password_list)

    password ="".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_file = {website:
        {"email":email,
         "password":password,
        }
        }

    if len(website)==0 or len(password)==0 :
        message_pop = messagebox.showerror(title="Oops", message ="Please make sure you haven't left any field empty" )

    else:
        try:
            with open("data.json", "r") as data_file:
                #reading the data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_file, data_file, indent=4)
        else:
            data.update(new_file)


            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

#---------------------------- search for password ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="No data File found")
    else:
        if website in data:
            email = data[website]["email"]
            password= data[website]["password"]
            messagebox.showinfo(title = website, message = f"email: {email}\n password:{password}")

        else:
            messagebox.showinfo(title="error", message=f"there are no details for {website}")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()


window.title("Password Manager")

window.config(padx=50,pady=50,)


canvas = Canvas(width= 200 , height= 200)

image_path = PhotoImage(file = "logo.png")

canvas.create_image(100, 100 , image= image_path)
canvas.grid(column = 1, row= 0)

label_website = Label(text="Website:")
label_website.grid(column = 0, row= 1)

label_email = Label(text= "Email/Username:")
label_email.grid(column = 0, row=2)

label_password = Label(text = "Password:")
label_password.grid(column= 0, row= 3)

website_entry = Entry(width = 30)
website_entry.grid(row=1, column =1)

email_entry = Entry(width = 50)
email_entry.grid(row=2,column = 1, columnspan= 2)
email_entry.insert(0,"ishita.kanpur29@gmail.com")

password_entry = Entry(width = 30)
password_entry.grid(row=3,column = 1)


button_generate = Button(text = "Generate Password" ,command=generate_password)
button_generate.grid(column = 2, row= 3)

button_add = Button(text= "Add" ,width = 40 , command = save)
button_add.grid(column = 1, row= 4, columnspan= 2)

button_search = Button(text= "Search", width=20, command=find_password)
button_search.grid(row= 1,column=2)




window.mainloop()


