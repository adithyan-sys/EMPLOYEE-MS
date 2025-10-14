from customtkinter import *
from PIL import Image
from tkinter import ttk,messagebox
import database
#functions 

def delete_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error', 'select data to delete')
    else:
        database.delete(identry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success', 'Employee data is deleted successfully')
        print('deleted')
def update_employee():
    selected_items = tree.selection()
    if not selected_items:
        messagebox.showerror('Error', 'No employee selected')
    else:
        database.update(identry.get(), nameentry.get(), phoneentry.get(), rolebox.get(), genderbox.get(), salaryentry.get())   
        treeview_data()
        clear()
        messagebox.showinfo('Success', 'Employee updated successfully')
        print('updated')


def selection(event):
    selected = tree.selection()
    if selected:
        row = tree.item(selected)['values']
        clear()
        identry.insert(0,row[0])
        nameentry.insert(0,row[1])
        phoneentry.insert(0,row[2])
        rolebox.set(row[3])
        genderbox.set(row[4])
        salaryentry.insert(0,row[5])

def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    identry.delete(0,END)
    nameentry.delete(0,END)
    phoneentry.delete(0,END)
    rolebox.set('')
    genderbox.set('Male')
    salaryentry.delete(0,END)

def treeview_data():
    employees = database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('', 'end', values=employee)


def add_employee():
    if identry.get() == '' or nameentry.get() == '' or phoneentry.get() == '' or rolebox.get() == '' or genderbox.get() == '' or salaryentry.get() == '':
        messagebox.showerror('ERROR','ALL Fields are required to enter')
    elif database.id_exists(id):
        messagebox.showerror('ERROR','ID already exists')
    else:
        database.insert(identry.get(),nameentry.get(),phoneentry.get(),rolebox.get(),genderbox.get(),salaryentry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Employee added successfully')
        print('added')


def search_employee():
    if searchentry.get() =='':
        messagebox.showerror('Error','Search field is required')
    elif searchbox.get() == 'by search':                                     #need to correct this def 
        messagebox.showerror('Error','Select a search criteria')
    else:
        searched_data = database.search(searchbox.get(),searchentry.get())
        print( searched_data) 

def show_all():
    treeview_data()
    searchentry.delete(0,END)
    searchbox.set('by search')

def delete_all():
   result = messagebox.showinfo('Info','DO you really want to delete all the data from the database')
   if result:
       database.delete_database()
       messagebox.showinfo('Success','All employee data deleted successfully')
       print('all deleted') 
   
window = CTk()
window.geometry("1080x780+200+200")
window.resizable(1, 0)
window.title("Employee Management System")
window.configure(fg_color='black')
logo = CTkImage(Image.open('bg.png'),size=(930,158))
logoLabel = CTkLabel(window,image=logo,text='')
logoLabel.grid(row=0,column=0,columnspan=2)
leftframe = CTkFrame(window,fg_color='black')
leftframe.grid(row=1,column=0)

idlabel = CTkLabel(leftframe,text='ID',font=('arial',18,'bold'),text_color='white')
idlabel.grid(row =0,column=0,padx=20,pady=15,sticky='w')

identry = CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
identry.grid(row=0,column=1) 

namelabel = CTkLabel(leftframe,text='NAME',font=('arial',18,'bold'),text_color='white')
namelabel.grid(row =1,column=0,padx=20,pady=15,sticky='w')

nameentry = CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
nameentry.grid(row=1,column=1) 

phonelabel = CTkLabel(leftframe,text='Ph.No.',font=('arial',18,'bold'),text_color='white')
phonelabel.grid(row =2,column=0,padx=20,pady=15,sticky='w')

phoneentry = CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
phoneentry.grid(row=2,column=1)  

rolelabel = CTkLabel(leftframe,text='ROLE',font=('arial',18,'bold'),text_color='white')
rolelabel.grid(row =3,column=0,padx=20,pady=15,sticky='w')
role_options = ['WEB DEV', 'CLOUD COMPUTING', 'PYTHON DEV', 'API DEV','NETWORD ENGINEER','SEO','BACK-END DEV', 'FULL-STACK DEV', 'DEVOPS']
rolebox = CTkComboBox(leftframe,values=role_options,width=180,font = ('arial',15,'bold'))
rolebox.grid(row=3,column=1)

genderlabel = CTkLabel(leftframe,text='GENDER',font=('arial',18,'bold'),text_color='white')
genderlabel.grid(row =4,column=0,padx=20,pady=15,sticky='w')
gender_option = ['Male','Female','OPTIMUS PRIME', 'MEGATRON','CYBERTRON','ATTACK HELICOPTER']
genderbox = CTkComboBox(leftframe,values=gender_option,width=180,font = ('arial',15,'bold'))
genderbox.grid(row=4,column=1)

salarylabel = CTkLabel(leftframe,text='SALARY',font=('arial',18,'bold'),text_color='white')
salarylabel.grid(row =5,column=0,padx=20,pady=15,sticky='w')

salaryentry = CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
salaryentry.grid(row=5,column=1)  

rightframe = CTkFrame(window)
rightframe.grid(row=1,column=1)
search_options = ['ID', 'NAME', 'PH.NO.', 'ROLE', 'GENDER', 'SALARY']
searchbox = CTkComboBox(rightframe,values=search_options,state='readonly')
searchbox.grid(row=0,column=0)
searchbox.set('by search')

searchentry = CTkEntry(rightframe)
searchentry.grid(row=0,column=1)  

searchbutton = CTkButton(rightframe,text='SEARCH',width=100,command=search_employee)
searchbutton.grid(row=0,column=2)

showallbutton = CTkButton(rightframe,text='SHOW ALL',width=100,command = show_all)
showallbutton.grid(row=0,column=3,pady=5)
tree = ttk.Treeview(rightframe,height=13)
tree.grid(row=1,column =0,columnspan=4)
tree['columns'] = ('ID','NAME','PH.NO.','ROLE','GENDER','SALARY')
tree.heading('ID',text='ID')
tree.heading('NAME',text='NAME')
tree.heading('PH.NO.',text='PH.NO.')
tree.heading('ROLE',text='ROLE')
tree.heading('GENDER',text='GENDER')
tree.heading('SALARY',text='SALARY')
tree.config(show='headings')
tree.column('ID',width=70) 
tree.column('NAME',width=70) 
tree.column('PH.NO.',width=70)
tree.column('ROLE',width=70)
tree.column('GENDER',width=70)
tree.column('SALARY',width=70) 
stye = ttk.Style()
stye.configure('Treeview.heading',rowheight=27,font=('arial',10,'bold'))
stye.configure('Treeview',font=('arial',10,'bold'),rowheight=27,background='#161C30',fieldbackground='#161C30',foreground='white') 
scrollbar = ttk.Scrollbar(rightframe,orient='vertical')
scrollbar.grid(row=1,column=4,sticky='ns')
buttonframe = CTkFrame(window)
buttonframe.grid(row=2,column=0,columnspan=2)

newbutton = CTkButton(buttonframe,text='NEW EMPLOYEE',font=('arial',15,'bold'),width=160,corner_radius=15,command=lambda:clear(True))
newbutton.grid(row=0,column=0,padx=5,pady=5)

addbutton = CTkButton(buttonframe,text='ADD EMPLOYEE',font=('arial',15,'bold'),width=160,corner_radius=15,command=add_employee)
addbutton.grid(row=0,column=1,padx=5,pady=5)

updatebutton = CTkButton(buttonframe,text='UPDATE EMPLOYEE',font=('arial',15,'bold'),width=160,corner_radius=15,command=update_employee)
updatebutton.grid(row=0,column=2,padx=5,pady=5)

deletebutton = CTkButton(buttonframe,text='DELETE EMPLOYEE',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_employee)
deletebutton.grid(row=0,column=3,padx=5,pady=5)

deleteallbutton = CTkButton(buttonframe,text='DELETE ALL EMPLOYEE',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_all)
deleteallbutton.grid(row=0,column=4,padx=5,pady=5)


window.bind('<ButtonRelease>',selection)
treeview_data()
window.mainloop()