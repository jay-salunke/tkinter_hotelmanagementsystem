from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db_connector import DBConnection
import re

from home import Home
class Login:
    connection = DBConnection()

    def home(self):
        root = Tk()
        Home(root)
        return 
    
    def validate(self):
        error = False
        email_regex = r"[\w\.%+]+@[\w]+\.[\w]{2,}$"
        if self.email.get() == "":
            messagebox.showerror("Error","Email ID is empty")
        
        elif (not re.findall(email_regex,self.email.get())):
            messagebox.showerror("Error","Email ID is invalid")

        elif self.password.get() == "":
            messagebox.showerror("Error","Password is empty")

        else: error = True
        return error


    def check_details(self):
        if self.validate():
            try:
                cursor = self.connection.db.cursor()
                cursor.execute("select * from admin_details where email_id = %s and password= %s",(
                    self.email.get(),
                    self.password.get(),
                ))

                rows= cursor.fetchall()
                if len(rows) >0:
                    messagebox.showinfo("Success","you have successully logged in!.....")
                    self.root.destroy()
                    self.home()
                    
                else:
                    messagebox.showerror("Error","Login Failed")    

            except Exception as e:
                messagebox.showerror("Error",e)    
        return            
     
    def __init__(self,root):
        self.root = root
        self.root.geometry("400x400")
        self.root.title("Login")

        ################### Variables ######################
        self.email = StringVar()
        self.password = StringVar()
        ####################################################

        #Email ID entry
        email_lbl = ttk.Label(self.root,text="Email ID: ",font=("new times roman",12,"bold"))
        email_lbl.place(x=100,y=100)
        email_entry = ttk.Entry(self.root,textvariable=self.email,font=("new times roman",12,"bold"))
        email_entry.place(x=100,y=130)

        #Password entry
        password_lbl = ttk.Label(self.root,text="Password: ",font=(" new times roman",12,"bold"))
        password_lbl.place(x=100, y=170)
        password_entry = ttk.Entry(self.root,textvariable=self.password,font=("new times roman",12,"bold"))
        password_entry.place(x=100,y=200)

        #forgot password
        forgot_password_lbl =Label(self.root,text="Forgot Password?",font=("new times roman",9,"bold"),fg="blue")
        forgot_password_lbl.place(x=100,y=235)

        #login button
        login_btn = Button(self.root,text="LOGIN",font=("new times roman",10,"bold"),padx=70,command=self.check_details)
        login_btn.place(x=100,y=270)


root = Tk()
Login(root)
root.mainloop()
