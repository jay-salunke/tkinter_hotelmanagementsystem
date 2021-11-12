
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import pyttsx3
from db_connector import DBConnection

class RoomManage:
    db_con = DBConnection()

    engine = pyttsx3.init()

    ################# VOICE #####################
    # getting details of current voice
    voices = engine.getProperty('voices')

    # engine.setProperty('voice', voices[0].id)
    # changing index, changes voices. o for male

    engine.setProperty('voice', voices[1].id)
   ###############################################

    def form_validation(self):
        
        error = False
        if self.Floor.get() == "":
            self.engine.say("Floor entry is empty")
            self.engine.runAndWait()
            messagebox.showerror("Error","Floor entry is empty")

        elif self.Room_no.get() == "":
            self.engine.say("Room no entry is empty")
            self.engine.runAndWait()
            messagebox.showerror("Error","Room no entry is empty")

        elif self.Room_type.get() == "":
            self.engine.say("Room type entry is empty")
            self.engine.runAndWait()
            messagebox.showerror("Error","Room type entry is empty")

        else:
            error = True    
            
        return error

    def add_data(self):
        if(self.form_validation()):
            try:
                db_cursor = self.db_con.db.cursor()
                db_cursor.execute("insert into room_details(Floor,Room_no,Room_type) VALUES(%s,%s,%s)", (
                    self.Floor.get(),
                    self.Room_no.get(),
                    self.Room_type.get()
                ))
                self.db_con.db.commit()
                self.engine.say("Data inserted successfully")
                self.engine.runAndWait()
                messagebox.showinfo(
                    "Success", "Data inserted successfully", parent=self.root)

            except Exception as e:
                self.db_con.db.rollback()
                messagebox.showwarning(
                    "Warning", f"{str(e)}", parent=self.root)
        return
 
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
       left_side_frame.place(x=2, y=54, width=385, height=302)

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
           "new times roman", 12, "bold"), padx=15, pady=2,command=self.add_data)
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

        ##################################### RIGHT SIDE FRAME ############################################
       self.search_type = StringVar()
        # frame
       right_side_frame = LabelFrame(
            self.root, text='VIEW ROOM DETAILS', relief=RIDGE, font=("new times roman", 11, "bold"))
       right_side_frame.place(x=390, y=54, width=500, height=302)
 
        ############################################# TABLE ###############################################

        # table frame
       table_frame = Frame(right_side_frame, border=2)
       table_frame.place(x=0, y=10, width=500, height=270)
       # X-axis and Y-axis ScrollBar
       scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
       scroll_y = Scrollbar(table_frame, orient=VERTICAL)
       self.room_table = ttk.Treeview(table_frame, columns=(
           "floor", "room_no", "room_type"), xscrollcommand=scroll_x, yscrollcommand=scroll_y)
       scroll_y.pack(side=RIGHT, fill=Y)
       scroll_x.pack(side=BOTTOM, fill=X)
       scroll_x.config(command=self.room_table.xview)
       scroll_y.config(command=self.room_table.yview)
       # table heading
       self.room_table.heading("floor", text="Floor")
       self.room_table.heading("room_no", text="Room no")
       self.room_table.heading("room_type", text="Room type")
       
       self.room_table["show"] = "headings"
       # setting column width
       self.room_table.column("floor", width=100)
       self.room_table.column("room_no", width=100)
       self.room_table.column("room_type", width=100)
      
        # self.room_table.bind(
        #     "<ButtonRelease-1>", self.get_row_details)

        # filling content in frame from both side (i.e from x-axis and y-axis both)
       self.room_table.pack(fill=BOTH, expand=1)

        #####################################################################################################




       ###################################################################################################### 
       
if __name__ == '__main__':
    root = Tk()
    RoomManage(root)
    root.mainloop()