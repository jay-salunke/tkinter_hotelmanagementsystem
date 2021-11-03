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
        name_entry.place(x=5, y=20, width=120)
        
        #fetchbutton
        fetch_button = Button(left_side_frame,font=("new times roman",9,"bold"),text="FETCH", fg="gold", bg="black", padx=5,pady=-130)
        fetch_button.place(x=127,y=18)
        
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
        no_of_days_lbl = ttk.Label(left_side_frame, text ="No of days",font=("new times roman",9,"bold"))
        no_of_days_lbl.place(x=2, y=175)
       
        no_of_days_entry = ttk.Entry(left_side_frame,font=("new times roman",9,"bold"))
        no_of_days_entry.place(x=5, y=195,width=160)

        #paid tax entry
        total_cost_lbl = ttk.Label(left_side_frame,text="Total cost",font=("new times roman",9,"bold"))
        total_cost_lbl.place(x=190, y=175)

        total_cost_entry = ttk.Entry(left_side_frame,font=("new times roman",9,"bold"),width=160,state="readonly")
        total_cost_entry.place(x=190, y=195, width=160)
           
        ############################################################################################################

         ###################################### LEFT SIDE FRAME BUTTONS ############################################

        # bottom frame
        bottom_frame = ttk.Frame(left_side_frame, relief=RIDGE)
        bottom_frame.place(x=2, y=225, width=380, height=78)

        # add button
        add_btn = Button(bottom_frame,text="ADD", fg="gold", bg="black", font=(
            "new times roman", 12, "bold"), padx=15, pady=2)
        add_btn.grid(row=0, column=0)

        # update button
        update_btn = Button(bottom_frame, text="UPDATE", fg="gold", bg="black", font=(
            "new times roman", 12, "bold"), padx=15, pady=2,)
        update_btn.grid(row=0, column=1, padx=1)

        # delete button
        delete_btn = Button(bottom_frame, text="DELETE", fg="gold", bg="black", font=(
            "new times roman", 12, "bold"), padx=15, pady=2,)
        delete_btn.grid(row=0, column=2, padx=1)

        # clear button
        clear_btn = Button(bottom_frame, text="CLEAR", fg="gold", bg="black", font=(
            "new times roman", 12, "bold"), padx=5, pady=2,)
        clear_btn.grid(row=0, column=3, padx=1, pady=3)

        bill_btn = Button(bottom_frame,text="BILL",fg="gold", bg="black", font=(
            "new times roman", 12, "bold"), padx=15, pady=2)
        bill_btn.grid(row=1, column=0, padx=2)

        ####################################################################################################
         ##################################### RIGHT SIDE FRAME ############################################
        self.search_type = StringVar()
        # frame
        right_side_frame = LabelFrame(
            self.root, text='VIEW DETAILS', relief=RIDGE, font=("new times roman", 11, "bold"))
        right_side_frame.place(x=390, y=54, width=500, height=330)

        # search combo box
        search = ("--select search type", "Contact no","Room no")
        combo_search = ttk.Combobox(
            right_side_frame, font=("new times roman", 9, "bold"))
        combo_search['values'] = search
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=3)

        # search entry
        self.entry_text = StringVar()
        search_entry = Entry(right_side_frame, font=(
            "new times roman", 9, "bold"))
        search_entry.grid(row=0, column=2, padx=3)

        # show button
        show_btn = Button(right_side_frame, text="SHOW", font=(
            "new times roman", 9, "bold"), fg="gold", bg="black")
        show_btn.grid(row=0, column=3, padx=3)

        # show all button
        show_all_btn = Button(right_side_frame, text="SHOW ALL", font=(
            "new times roman", 9, "bold"), fg="gold", bg="black")
        show_all_btn.grid(row=0, column=4, padx=3)

        table_frame = Frame(right_side_frame, border=2)
        table_frame.place(x=0, y=40, width=500, height=270)

        #######################################TABLE #########################################
        # X-axis and Y-axis ScrollBar
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.room_table = ttk.Treeview(table_frame, columns=(
            "Contact no", "Check in date", "Check out date", "Room type", "Room available", "Meal", "No of days", "Total cost"), xscrollcommand=scroll_x, yscrollcommand=scroll_y)

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.pack(side=BOTTOM, fill=X)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        # table heading
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
        # self.customer_details_table.bind(
        #     "<ButtonRelease-1>", self.get_row_details)

        # filling content in frame from both side (i.e from x-axis and y-axis both)
        self.room_table.pack(fill=BOTH, expand=1)

if __name__ == '__main__':
    room_win_root = Tk()
    cusomer_obj = Room(room_win_root)
    room_win_root.mainloop()
