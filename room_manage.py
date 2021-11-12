
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import pyttsx3
from db_connector import DBConnection

class RoomManage:
   def __init__(self,root):

       db_con = DBConnection()
       self.root = root
       self.root.geometry('890x385+430+200')
       self.root.title('Add room booking details')
       self.root.resizable(width=False, height=False)
       ################################### VARIABLES #############################################
       self.Floor = StringVar()
       self.Room_no = StringVar()
       self.Room_type = StringVar()
       ###########################################################################################
       
       ################################### CUSTOMER DETAIL TITLE###################################
       customer_details_title = Label(self.root, bg="black", fg="gold", text="ADD CUSTOMER DETAILS",
                                      padx=360, pady=15, font=("new timed roman", 12, "bold"))
       customer_details_title.place(x=0, y=0)

       hotel_logo = Image.open('D:\python_tkinter_project\images\golden-hotel-logo-free-graphics-472233.jpg')
       hotel_logo = hotel_logo.resize((60, 50), Image.ANTIALIAS)
       self.hotel_logo1 = ImageTk.PhotoImage(hotel_logo)
       hotel_logo1_label = Label(
       self.root, image=self.hotel_logo1, relief=RIDGE)
       hotel_logo1_label.place(x=0, y=0)

       ####################################### LEFT SIDE FRAME ######################################### 
       left_side_frame = LabelFrame(self.root, text='ADD ROOM DETAILS', relief=RIDGE, font=("new times roman", 11, "bold"))
       left_side_frame.place(x=2, y=54, width=385, height=330)

       #floor entry
       floor_lbl = Label(left_side_frame,text="Floor: ",font=("new times roman",9,"bold"))
       floor_lbl.grid(row=0,column=0)

       floor_entry = Entry(left_side_frame,font=("new times roman",9,"bold"),textvariable=self.Floor)
       floor_entry.grid(row=0,column=1)

       #room no entry
       room_no_lbl = Label(left_side_frame,text="Room no: ",font=("new times roman",9,"bold"))
       room_no_lbl.grid(row=1,column=0,pady=20)

       room_entry = Entry(left_side_frame,font=("new times romnan",9,"bold"),textvariable=self.Room_no)
       room_entry.grid(row=1,column=1,pady=20)

       #room type entry
       room_type_lbl = Label(left_side_frame,text="Room type: ",font=("new times roman",9,"bold"))
       room_type_lbl.grid(row=2,column=0,pady=5)

       room_type_combo_box = ttk.Combobox(left_side_frame,font=("new times roman",9,"bold"),width=17,textvariable=self.Room_type)
       room_type_combo_box.grid(row=2,column=1,pady=5)
       ###################################### LEFT SIDE FRAME BUTTONS ############################################

        # bottom frame
       bottom_frame = ttk.Frame(left_side_frame, relief=RIDGE)
       bottom_frame.place(x=2, y=140, width=380, height=40)

        # add button
       add_btn = Button(bottom_frame,text="ADD", fg="gold", bg="black", font=(
           "new times roman", 12, "bold"), padx=15, pady=2)
       add_btn.grid(row=0, column=0)

        # update button
       update_btn = Button(bottom_frame, text="UPDATE", fg="gold", bg="black", font=(
           "new times roman", 12, "bold"), padx=15, pady=2)
       update_btn.grid(row=0, column=1, padx=1)

        # delete button
       delete_btn = Button(bottom_frame, text="DELETE", fg="gold", bg="black", font=(
           "new times roman", 12, "bold"), padx=15, pady=2)
       delete_btn.grid(row=0, column=2, padx=1)

        # clear button
       clear_btn = Button(bottom_frame, text="CLEAR", fg="gold", bg="black", font=(
           "new times roman", 12, "bold"), padx=5, pady=2)
       clear_btn.grid(row=0, column=3, padx=1, pady=3)

        ####################################################################################################



       ################################################################################################# 
       
if __name__ == '__main__':
    root = Tk()
    RoomManage(root)
    root.mainloop()