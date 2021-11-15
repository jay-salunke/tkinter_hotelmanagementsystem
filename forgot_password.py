from tkinter import *
from tkinter import messagebox
from db_connector import DBConnection
from home import Home
class ForgotPass:
    connection  = DBConnection()
    def validate(self):
            error = False
            if (self.current_pass.get() == ""):
                messagebox.showerror("Error","Current password is emtpy")

            elif (self.new_pass.get() == ""):
                messagebox.showerror("Error","New password is empty")

            elif len(self.new_pass.get()) <8:
                messagebox.showerror("Error","Minimum 8 characters are required")

            elif len(self.confirm_pass.get()) <8:
                messagebox.showerror("Error","Minimum 8 characters are empty")

            elif  self.new_pass.get() != self.confirm_pass.get():
                messagebox.showerror("Error","confirm password is not matching")
            
            elif (self.confirm_pass.get() == ""):
                messagebox.showerror("Error","Confirm pass is empty")
            
            else: error = True

            return error

    def change_pass(self):
        if (self.validate()):
            try:
                cursor = self.connection.db.cursor()
                cursor.execute("select * from admin_details where password = %s",(
                    self.current_pass.get(),
                ))
                rows = cursor.fetchone()
                if rows == None:
                    messagebox.showerror("Error","Password is invalid")
                else:

                    cursor.execute("update admin_details set password = %s where name = %s",(
                        self.new_pass.get(),
                        "admin"
                    ))
                    self.connection.db.commit()
                    messagebox.showinfo("Success","Password has been changed successfully")
                    self.root.destroy()
                    home_screen = Tk()
                    Home(home_screen)   
            except Exception as e:
                messagebox.showwarning("Warning",e)
        return          

    def __init__(self,root):
        self.root = root
        self.root.geometry("400x400")
        self.root.title("Forgot password")
        ################################# Variables #########################################
        self.current_pass = StringVar()
        self.new_pass = StringVar()
        self.confirm_pass = StringVar()
        #####################################################################################
        #current password entry
        current_pass_lbl = Label(self.root,font=("new times roman",12,"bold"),text="Current password: ")
        current_pass_lbl.place(x=100,y=100)
        current_pass_entry = Entry(self.root,font=("new times roman",12,"bold"),textvariable=self.current_pass)
        current_pass_entry.place(x=100,y=130)
        
        #new password entry
        new_pass_lbl = Label(self.root,text="New password: ",font=("new times roman",12,"bold"))
        new_pass_lbl.place(x=100,y=170)
        new_pass_entry = Entry(self.root,textvariable=self.new_pass,font=("new times roman",12,"bold"),show="*")
        new_pass_entry.place(x=100,y=200)
        
        #confirm pass entry
        confirm_pass_lbl = Label(self.root,text="Confirm password",font=("new times roman",12,"bold"))
        confirm_pass_lbl.place(x=100,y=230)
        confirm_pass_entry = Entry(self.root,textvariable=self.confirm_pass,font=("new times roman",12,"bold"),show="*")
        confirm_pass_entry.place(x=100,y=270)
        
        #change pass button
        change_pass_btn = Button(self.root,text="Change password",font=("new times roman",12,"bold"),padx=15,command=self.change_pass)
        change_pass_btn.place(x=100,y=310)
        
        return

if __name__ == "__main__":
    root = Tk()
    ForgotPass(root)
    root.mainloop()