from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from tkcalendar import DateEntry


class Room:

    def __init__(self, root):
        self.root = root
        self.root.geometry('890x385+430+200')
        self.root.title('Room booking')

        ################################### CUSTOMER DETAIL TITLE###################################
        customer_details_title = Label(self.root, bg="black", fg="gold", text="ADD ROOM BOOKING DETAILS",
                                       padx=360, pady=15, font=("new timed roman", 12, "bold"))
        customer_details_title.place(x=0, y=0)
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
            self.root, text='ADD ROOM BOOKING DETAILS', relief=RIDGE, font=("new times roman", 11, "bold"))
        left_side_frame.place(x=2, y=54, width=385, height=330)
        
        ##################################### ADD DETAIL ENTRIES ####################################

        # customer name
        name_lbl = ttk.Label(left_side_frame, text="Customer contact no.", font=(
            "new times roman", 9, "bold"))
        name_lbl.place(x=2, y=2)

        name_entry = ttk.Entry(left_side_frame, font=(
            "new times roman", 9, "bold"),)
        name_entry.place(x=5, y=20, width=160)
        
        #check in date entry
        check_in_lbl = ttk.Label(left_side_frame, text='Check in date', font=(
            "new times roman", 9, "bold"))
        check_in_lbl.place(x=190, y=2)

        check_in_date_entry = DateEntry(
            left_side_frame, font=("new times roman", 9, "bold"),selectmode = 'day')
        check_in_date_entry.place(x=190, y=20, width=160)

        #check out date entry
        check_out_lbl = ttk.Label(left_side_frame,text="Check out date",font=("new times roman",9,"bold"))
        check_out_lbl.place(x=2, y=60)

        check_out_date_entry = DateEntry(left_side_frame,selectmode = 'day',font=("new times roman",9,"bold"))
        check_out_date_entry .place(x=5, y=78, width=160)

        #room type combobox
        room_type_lbl= ttk.Label(
            left_side_frame, text="Room type", font=("new times roman", 9, "bold"))
        room_type_lbl.place(x=190, y=60)

        room_type_combo_box= ttk.Combobox(
            left_side_frame, font=("new times roman", 9, "bold"), width=160)
        room_type_combo_box.place(x=190,y=78,width=160)

        #available room no entry
        available_room_no_lbl = ttk.Label(left_side_frame,text = "Available room no",font=("new times roman",9,"bold"))
        available_room_no_lbl.place(x=2, y=116)

        available_room_no_entry = ttk.Entry(left_side_frame,state="readonly",font=("new times roman",9,"bold"))
        available_room_no_entry.place(x=5, y=135, width=160)

        #meal combo box
        meal_lbl = ttk.Label(left_side_frame,text="Meal",font=("new times roman",9,"bold"))
        meal_lbl.place(x=190, y=116)
        
        meal_combo_box = ttk.Combobox(left_side_frame,font=("new times roman",9,"bold"))
        meal_combo_box.place(x=190, y=135, width=160)

        #no of days entry
        no_of_days_lbl = ttk.Label(left_side_frame, text ="no of days",font=("new times roman",9,"bold"))
        no_of_days_lbl.place(x=2, y=175)
       
        no_of_days_entry = ttk.Entry(left_side_frame,font=("new times roman",9,"bold"))
        no_of_days_entry.place(x=5, y=195,width=160)

        #paid tax entry
        total_cost_lbl = ttk.Label(left_side_frame,text="total cost",font=("new times roman",9,"bold"))
        total_cost_lbl.place(x=190, y=175)

        total_cost_entry = ttk.Entry(left_side_frame,font=("new times roman",9,"bold"),width=160,state="readonly")
        total_cost_entry.place(x=190, y=195, width=160)




        

           

        ############################################################################################


if __name__ == '__main__':
    room_win_root = Tk()
    cusomer_obj = Room(room_win_root)
    room_win_root.mainloop()
