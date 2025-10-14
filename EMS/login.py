
from customtkinter import *
from PIL import Image
from tkinter import messagebox
def login():
    if usernameEntry.get() == '' or PasswordEntry.get() == '':
        messagebox.showerror('Error','All fields are required')
        print('error')
    elif usernameEntry.get() == 'admin' and PasswordEntry.get() == 'admin':
        messagebox.showinfo('Success','Welcome to Employee Management System')
        print('success','admin')
        root.destroy()
    elif usernameEntry.get() == 'Adi' and PasswordEntry.get() == '1234':
        messagebox.showinfo('Success','Welcome to Employee Management System')
        print('success','Adi')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','Invalid username or password')
        print('invalid')
root = CTk()
root.geometry("930x478")
root.resizable(0,0)
root.title('login page')
image = CTkImage(Image.open('ems2.png'),size = (930,478))
imageLabel = CTkLabel(root,image = image,text = '')
imageLabel.place(x=0,y=0) 
HeadingLabel = CTkLabel(root,text='Employee Management system',bg_color='#FAFAFA',font=('Goudy Old Style',20,'bold'))
HeadingLabel.place(x=20,y=100)
usernameEntry = CTkEntry(root,placeholder_text='enter your user name',width=180)
usernameEntry.place(x=50,y=150)

PasswordEntry = CTkEntry(root,placeholder_text='enter your Password',width=180,show='*')
PasswordEntry.place(x=50,y=200)

loginbutton = CTkButton(root,text='Login',cursor='hand2',command=login)
loginbutton.place(x=70,y=250)
root.mainloop()
