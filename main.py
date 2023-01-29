

from tkinter import *
from tkinter import messagebox  # This is not a class, so we need to import it again
import json
import pyperclip  # To automatically copy the password if it is generated or saved so that user can just take it and paste to portal


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

from passwordGenerator import generatePassword

def genPassClicked():
    
    # Clearing old password from box before suggesting new
    passwordInput.delete(0, END)
    
    newPass = generatePassword()
    passwordInput.insert(0,newPass)
    pyperclip.copy(newPass) # To automatically copy the generated password

# ---------------------------- SEARCH ------------------------------- #

def Search():
    
    query = webInput.get()  # the website entered by the user
    
    try:
        with open("Data.json","r") as f:
            data = json.load(f)
        
        # for (key,value) in data.items():
            
        # if(key == query):
        
    except FileNotFoundError:
        # if file is not there, means there is no data anyways so we will show error
        messagebox.showwarning(title="No Data Found", message=f"There is no result for {query}")
    
        
    else:
        if query in data:
            
            foundData = data[query]
            
            
            email = foundData["email"]
            password = foundData["password"]
            # now we will show user info box giving the password
            
            messagebox.showinfo(title= "Your Data", message=f"Website: {query}\nEmail: { email }\nPassword: {password}\n")
            # webInput.delete(0,END)
            

        else:
            messagebox.showwarning(title="No Data Found", message=f"There is no result for {query}")
            # webInput.delete(0,END)
        

    finally:    
        webInput.delete(0,END)
                    
                    
                    
                    
                



# ---------------------------- SAVE PASSWORD ------------------------------- #

def Save():
    website = webInput.get()
    email = emailInput.get()
    password = passwordInput.get()
    
    # JSON data
    newData = {
        website : { 
            "email":email,
            "password":password
        }
    }
    
    # Validation
    if (len(website) == 0) or (len(email) == 0) or (len(password) == 0):
        messagebox.showwarning(title="Data Missing :-(",message="Please do not leave any data column blank!")
        
    else:
        
        # Verification
        isOK = messagebox.askokcancel(title=website, message=f"Verify your data\n\n\tEmail: {email}\n\tPassword: {password}\n\nAre you sure you want to save this data?")
        
        if isOK:
            
            try:
            
                with open("Data.json", "r") as f:
                    
                    # To store the data in JSON
                    
                    # First we will read the existing data
                    existingData = json.load(f)
            
            except FileNotFoundError:
                
                with open("Data.json", "w") as f:
                         
                    json.dump(newData, f, indent=4)  
                    
        
                    
            else: # if the TRY block runs means there is already file and no need to create new, then we will just update
                
                # Secondly we will update the data
                existingData.update(newData)    # now the new entry is added
                    
                with open("Data.json", "w") as f:
                    
                    # Third step is to write
                    # JSON writing
                    json.dump(existingData, f, indent=4)  # this method takes the data and name of file and many other arguments
                    
                    

            finally: # no matter whether new file or old, we will have to clear the screen input 
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



webInput = Entry(width=22)
webInput.focus()
webInput.grid(row=1, column =1 , pady=5)

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

searchButton = Button(text="Search", width=10, command= Search, bg="crimson", fg="white")
searchButton.grid(row=1, column =2, pady=5)

win.mainloop()


