
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import random
import pyttsx3
import re
from db_connector import DBConnection
class room_manage:
        def __init__(self, root):
         self.root = root
         self.root.geometry('890x385+430+200')
         self.root.title('MANAGE ROOM')
         self.root.resizable(width=False, height=False)

         room_manage_title = Label(self.root, bg="black", fg="gold", text="ADD ROOM  DETAILS",
                                       padx=360, pady=15, font=("new timed roman", 12, "bold"))
         room_manage_title.place(x=0, y=0)
        ############################################################################################

        ############################## LEFT SIDE LOGO IMAGE #######################################
         hotel_logo = Image.open(
            'D:\python_tkinter_project\images\golden-hotel-logo-free-graphics-472233.jpg')
         hotel_logo = hotel_logo.resize((60, 50), Image.ANTIALIAS)
         self.hotel_logo1 = ImageTk.PhotoImage(hotel_logo)
         hotel_logo1_label = Label(
             self.root, image=self.hotel_logo1, relief=RIDGE)
         hotel_logo1_label.place(x=0, y=0)
        ############################################################################################

        ######################################LEFT SIDE FRAME #######################################
         left_side_frame = LabelFrame(
             self.root, text='ADD NEW ROOM', relief=RIDGE, font=("new times roman", 11, "bold"))
         left_side_frame.place(x=2, y=54, width=385, height=323)

         #floor
         floor_lbl  = ttk.Label(left_side_frame,text="Floor: ",font=(
            "new times roman", 9, "bold")
            )
         floor_lbl.grid(row=0,column=0)

         floor_entry = Entry(left_side_frame, font=(
            "new times roman", 9, "bold"),width=23)
         floor_entry.grid(row=0 ,column=1)   


         #room_no
         room_no_lbl  = Label(left_side_frame,text="Room no: ",font=(
            "new times roman", 9, "bold")
            )
         room_no_lbl.grid(row=1,column=0,pady=20)
         
         room_no_entry = Entry(left_side_frame, font=(
            "new times roman", 9, "bold"),width=23)
         room_no_entry.grid(row=1 ,column=1,pady=20)


         #room_type
         room_type_lbl  = ttk.Label(left_side_frame,text="Room no: ",font=(
            "new times roman", 9, "bold")
            )
         room_type_lbl.grid(row=2,column=0,pady=10)

         room_type_combo_box = ttk.Combobox(left_side_frame,font=("new times roman", 9, "bold"))
         room_type_combo_box.grid(row=2,column=1,pady=10)

          ###################################### LEFT SIDE FRAME BUTTONS #######################################

        # bottom frame
         bottom_frame = ttk.Frame(left_side_frame, relief=RIDGE)
         bottom_frame.place(x=2, y=145, width=380, height=40)

        # add button
         add_btn = Button(bottom_frame, text="ADD", fg="gold", bg="black", font=(
             "new times roman", 12, "bold"), padx=15, pady=2)
         add_btn.grid(row=0, column=0)

        # update button
         update_btn = Button(bottom_frame, text="UPDATE", fg="gold", bg="black", font=(
             "new times roman", 12, "bold"), padx=15, pady=2)
         update_btn.grid(row=0, column=1, padx=1)

         # delete button
         delete_btn = Button(bottom_frame, text="DELETE", fg="gold", bg="black", font=(
             "new times roman", 12, "bold"), padx=15, pady=2,)
         delete_btn.grid(row=0, column=2, padx=1)    

         # clear button
         clear_btn = Button(bottom_frame, text="CLEAR", fg="gold", bg="black", font=(
             "new times roman", 12, "bold"), padx=5, pady=2)
         clear_btn.grid(row=0, column=3, padx=1, pady=3)
        ###################################################################################################### 

        ###########################################RIGHT SIDE FRAME###########################################
         right_side_frame = LabelFrame(
            self.root, text='ROOM DETAILS', relief=RIDGE, font=("new times roman", 11, "bold"))
         right_side_frame.place(x=390, y=54, width=500, height=323)

         table_frame = Frame(right_side_frame, border=2)
         table_frame.place(x=0, y=40, width=500, height=270)

        # X-axis and Y-axis ScrollBar
         scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
         scroll_y = Scrollbar(table_frame, orient=VERTICAL)

         self.room_table = ttk.Treeview(table_frame, columns=(
            "Contact no", "Check in date", "Check out date", "Room type", "Room available", "Meal", "No of days", "Total cost"), xscrollcommand=scroll_x, yscrollcommand=scroll_y)

         scroll_y.pack(side=RIGHT, fill=Y)
         scroll_x.pack(side=BOTTOM, fill=X)
 
         scroll_x.config(command=self.room_table.xview)
         scroll_y.config(command=self.room_table.yview)
 
          
 
         self.room_table.heading("Contact no", text="Contact")
         self.room_table.heading("Check in date", text="Checkin")
         self.room_table.heading("Check out date", text="Checkout")
         self.room_table.heading("Room type", text="Roomtype")
         self.room_table.heading("Room available", text="RoomAvailable")
         self.room_table.heading("Meal", text="Meal")
         self.room_table.heading("No of days", text="No_of_Days")
         self.room_table.heading("Total cost", text="Total cost")
         self.room_table["show"] = "headings"

        # setting column width
         self.room_table.column("Contact no", width=100)
         self.room_table.column("Check in date", width=100)
         self.room_table.column("Check out date", width=100)
         self.room_table.column("Room type", width=100)
         self.room_table.column("Room available", width=100)
         self.room_table.column("Meal", width=100)
         self.room_table.column("No of days", width=100)
         self.room_table.column("Total cost", width=100)
        

        # filling content in frame from both side (i.e from x-axis and y-axis both)
         self.room_table.pack(fill=BOTH, expand=1)


        ######################################################################################################



if __name__ == '__main__':
    root = Tk()
    room_mng = room_manage(root)
    root.mainloop()