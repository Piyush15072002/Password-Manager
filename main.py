from tkinter import *
from tkinter import messagebox  # This is not a class, so we need to import it again

import pyperclip  # To automatically copy the password if it is generated or saved so that user can just take it and paste to portal


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

from passwordGenerator import generatePassword

def genPassClicked():
    
    # Clearing old password from box before suggesting new
    passwordInput.delete(0, END)
    
    newPass = generatePassword()
    passwordInput.insert(0,newPass)
    pyperclip.copy(newPass) # To automatically copy the generated password

# ---------------------------- SAVE PASSWORD ------------------------------- #

def Save():
    website = webInput.get()
    email = emailInput.get()
    password = passwordInput.get()
    
    
    # Validation
    if (len(website) == 0) or (len(email) == 0) or (len(password) == 0):
        messagebox.showwarning(title="Data Missing :-(",message="Please do not leave any data column blank!")
        
    else:
        
        # Verification
        isOK = messagebox.askokcancel(title=website, message=f"Verify your data\n\n\tEmail: {email}\n\tPassword: {password}\n\nAre you sure you want to save this data?")
        
        if isOK:
            
            with open("Data.txt", "a") as f:
                f.write(f"{website} | {email} | {password}\n")
                # After getting data, then we will delete it from screen input
                webInput.delete(0, END)
                passwordInput.delete(0, END)
                




# ---------------------------- UI SETUP ------------------------------- #

win = Tk()

win.title("Password Manager")
win.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)

logo = PhotoImage(file="logo.png")

canvas.create_image(100,100,image=logo)

canvas.grid(row = 0, column =1)


# Labels

website = Label(text="Website:")
website.grid(row=1, column =0, pady=5)

email = Label(text="Email:")
email.grid(row=2, column =0, pady=5)


password = Label(text="Password:")
password.grid(row=3, column =0, pady=5)


# Inputs



webInput = Entry(width=40)
webInput.focus()
webInput.grid(row=1, column =1 , columnspan=2, pady=5)

emailInput = Entry(width=40)
emailInput.grid(row=2, column =1 , columnspan=2, pady=5)
emailInput.insert(0, "mail@email.com")

passwordInput = Entry(width=22)
passwordInput.grid(row=3, column =1, pady=5) 


# Button

genPass = Button(text="Generate Password", bg="#FFD4D4",  highlightthickness=0, command= genPassClicked)
genPass.grid(row=3, column =2, pady=5) 


addButton = Button(text="Add Data", width=35, command= Save, bg="black", fg="white")
addButton.grid(row=4, column =1, columnspan=2, pady=5)



win.mainloop()


