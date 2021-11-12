
import re
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter import messagebox
from db_connector import DBConnection
import pyttsx3
from time import strftime
from datetime import datetime
from datetime import date


class Room:
    db_con = DBConnection()

    engine = pyttsx3.init()

    ################# VOICE #####################
    # getting details of current voice
    voices = engine.getProperty('voices')

    # engine.setProperty('voice', voices[0].id)
    # changing index, changes voices. o for male

    engine.setProperty('voice', voices[1].id)

    def total(self):
        indate = self.checkin_date.get()
        outdate = self.checkout_date.get()
        indate = datetime.strptime(indate, "%d/%m/%Y")
        outdate = datetime.strptime(outdate, "%d/%m/%Y")
        self.no_of_days.set(abs(outdate-indate).days)
        ac_charges = 2500
        non_ac_charges = 1000
        luxury_charges = 3200
        duplex_charges = 3000
        no_of_days = int(self.no_of_days.get())
        gst_tax = 0
        total_cost = 0
        if  self.room_type.get() == "AC":
            total_cost = no_of_days*ac_charges+800
            gst_tax = (total_cost*9+9)/100

        elif self.room_type.get() == "NON AC":
            total_cost = no_of_days*non_ac_charges+700
            gst_tax = (total_cost*9+9)/100

        elif self.room_type.get() == "Duplex":
            total_cost = no_of_days*duplex_charges+900
            gst_tax = (total_cost*9+9)/100

        elif self.room_type.get() == "Luxury":
            total_cost = no_of_days*luxury_charges+1000
            gst_tax = (total_cost*9+9)/100

        print(gst_tax)
        print(total_cost)
        messagebox.showinfo(
            "Total cost", f"SGST tax:{int(gst_tax/2)} \n CGST tax:{int(gst_tax/2)} \n Total tax: {int(gst_tax)}",parent = self.root)
        self.total_cost.set(int(total_cost+gst_tax))
        return

    def get_row_details(self, events=""):
        cursor_row = self.room_table.focus()
        row_content = self.room_table.item(cursor_row)
        row = row_content["values"]
        self.contact_num.set(row[0])
        self.checkin_date.set(row[1])
        self.checkout_date.set(row[2])
        self.room_type.set(row[3])
        self.available_room.set(row[4])
        self.meal.set(row[5])
        self.no_of_days.set(row[6])
        self.total_cost.set(row[7])

    def fetch_data(self):
        if self.contact_num.get() == "":
            messagebox.showerror(
                "error", "Please enter phone number", parent=self.root)
        else:

            try:
                db_cursor = self.db_con.db.cursor()
                query = (
                    "select * from customers_details where customer_mobile_no = %s")
                value = (self.contact_num.get(),)
                db_cursor.execute(query, value)
                row = db_cursor.fetchall()

                if len(row) == 0:
                    messagebox.showerror(
                        "Error", "This number is not found", parent=self.root)
                else:
                    self.db_con.db.commit()
                    messagebox.showinfo("Success",
                                        f"Data found!\n Customer id: {row[0][0]} \n Customer name: {row[0][1]} \n Customer email: {row[0][2]} \n Customer mobile: {row[0][3]} \n Customer nation: {row[0][4]} \n Customer state: {row[0][5]}\n Customer gender: {row[0][6]}\n Customer proof type: {row[0][7]}", parent=self.root)

            except Exception as e:
                messagebox.showwarning("Warning", f"{str(e)}",parent = self.root)

        return

    def fetch_room_numbers(self,*args):
        try:
            cursor = self.db_con.db.cursor()
            cursor.execute("select Room_no from room_details where Room_type = %s",(
                self.room_type.get(),
            ))
            rows = cursor.fetchall()
            self.available_room_no_combobox.set("")
            self.available_room_no_combobox['values'] = [x for x in rows]
        except Exception as e:
            print("")    
        return     

    def form_validation(self):
        no_error = False
        try:
            checkin_date = [int(x) for x in self.checkin_date.get().split('/')]
            checkout_date = [int(x)
                             for x in self.checkout_date.get().split('/')]

            

            if self.contact_num.get() == "":
                self.engine.say("mobile field is empty")
                self.engine.runAndWait()
                messagebox.showerror("Error", "mobile field is empty",parent = self.root)

            elif(not re.match('^[\\d]+$', self.contact_num.get())):
                self.engine.say('characters are not allowed')
                self.engine.runAndWait()
                messagebox.showerror(
                    "Error", "Characters are not allowed", parent=self.root)

            elif(len(self.contact_num.get()) > 10 or len(self.contact_num.get()) <= 9):
                self.engine.say('Enter 10 digits number only')
                self.engine.runAndWait()
                messagebox.showerror(
                    "Error", "Enter the 10 digits number only",parent = self.root)

            elif self.checkin_date.get() == "":
                self.engine.say("please fill checkin date")
                self.engine.runAndWait()
                messagebox.showerror("Error", "check in date is empty",parent = self.root)

            elif checkin_date[0] > 32 or checkout_date[0] > 32:
                self.engine.say("please enter valid date")
                self.engine.runAndWait()
                messagebox.showerror("Error", "Please enter the valid month",parent = self.root)

            elif checkin_date[1] > 13 or checkout_date[1] > 13:
                self.engine.say("please enter valid month")
                self.engine.runAndWait()
                messagebox.showerror("Error", "Please enter the valid date",parent = self.root)

            elif checkin_date[2] > checkout_date[2]:
                self.engine.say(
                    "check in year is bigger. please enter valid year")
                self.engine.runAndWait()
                messagebox.showerror(
                    "Error", "check in year is bigger. please enter valid year",parent = self.root)

            elif checkout_date[2] < checkin_date[2]:
                self.engine.say("you have entered wrong check out date")
                self.engine.runAndWait()
                messagebox.showerror("Error","you have entered wrong check out date",parent = self.root)

            elif checkin_date[0] > checkout_date[0]:
                self.engine.say(
                    "check in date month is bigger. please enter valid month")
                self.engine.runAndWait()
                messagebox.showerror(
                    "Error", "check in date month is bigger. please enter valid month",parent = self.root)

            elif self.room_type.get() == "":
                self.engine.say("please select room type")
                self.engine.runAndWait()
                messagebox.showerror("Error", "please select room type",parent = self.root)

            elif self.room_type.get() == "--Select room type":
                self.engine.say("Please select the room type")
                self.engine.runAndWait()
                messagebox.showerror("Error", "Please select the room type",parent = self.root)

            elif self.available_room.get() == "":
                self.engine.say("please enter room number")
                self.engine.runAndWait()
                messagebox.showerror("Error", "please enter room no",parent = self.root)

            elif self.meal.get() == "":
                self.engine.say("please select meal field")
                self.engine.runAndWait()
                messagebox.showerror("Error", "please select meal field",parent = self.root)

            elif self.meal.get() == "--Select meal--":
                self.engine.say("Please select the meal type")
                self.engine.runAndWait()
                messagebox.showerror("Error", "Please slect the meal type",parent = self.root)

            elif self.no_of_days.get() == "":
                self.engine.say("no of days field is empty")
                self.engine.runAndWait()
                messagebox.showerror("Error", "no of days field is empty",parent = self.root)

            elif self.total_cost.get() == "":
                self.engine.say("Total cost field is empty")
                self.engine.runAndWait()
                messagebox.showerror("Error", "Total cost field is empty",parent = self.root)

            else:
                no_error = True
        except Exception as e:
            self.engine.say(str(e))
            self.engine.runAndWait()
            messagebox.showerror("Error", f"{str(e)}",parent = self.root)

        return no_error

    def fetch_all_data(self):
        try:
            db_cursor = self.db_con.db.cursor()
            query = ("select * from roombooking_details")
            db_cursor.execute(query)
            row = db_cursor.fetchall()
            if len(row) != 0:
                self.room_table.delete(*self.room_table.get_children())
                for i in row:
                    self.room_table.insert("", END, values=i)
                self.db_con.db.commit()

        except Exception as e:
            print(f"{str(e)}")
        return

    def user_exists(self):
        exists = False
        try:
            db_cursor = self.db_con.db.cursor()
            query = (
                "select * from customers_details where customer_mobile_no = %s")
            value = (self.contact_num.get(),)
            db_cursor.execute(query, value)
            row = db_cursor.fetchone()
            if row != None:
                exists = True
            else:
                messagebox.showerror(
                    "Error", "user doesn't exists. first please register the user",parent = self.root)

            return exists

        except Exception as e:
            print(e)
        return

    def delete_data(self):
        if self.user_exists():
            try:
                confirmation_msgbox = messagebox.askyesno(
                    "hotel management system", "do you really want to remove the details of the user", parent=self.root)
                if confirmation_msgbox > 0:
                    db_cursor = self.db_con.db.cursor()
                    query = (
                        "delete from roombooking_details where Contact_no = %s")
                    value = (self.contact_num.get(),)
                    db_cursor.execute(query, value)
                    self.db_con.db.commit()
                    self.engine.say("Data deleted successfully")
                    self.engine.runAndWait()
                    messagebox.showinfo("Success", "Data deleted successfully",parent = self.root)
                    self.fetch_all_data()

            except Exception as e:
                print(self.db_con.db.rollback())
        return

    def add_data(self):
        if(self.form_validation() and self.user_exists()):
            try:
                db_cursor = self.db_con.db.cursor()
                query = ("insert into roombooking_details(Contact_no,Checkin_date,Checkout_date,roomtype,room_available,meal,NoOfDays,Totalcost) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)")
                values = (
                    self.contact_num.get(),
                    self.checkin_date.get(),
                    self.checkout_date.get(),
                    self.room_type.get(),
                    self.available_room.get(),
                    self.meal.get(),
                    self.no_of_days.get(),
                    self.total_cost.get()
                )
                db_cursor.execute(query, values)
                self.db_con.db.commit()
                self.engine.say("Data inserted successfully")
                self.engine.runAndWait()
                messagebox.showinfo("Success", "Room booked successfully",parent = self.root)
                self.fetch_all_data()
            except Exception as e:
                messagebox.showwarning("Warning", f"{str(e)}",parent = self.root)
        return

    def clear_entry(self):
        today = date.today()
        today_date = today.strftime("%m/%d/%Y")
        self.contact_num.set("")
        self.checkin_date.set(today_date)
        self.checkout_date.set(today_date)
        self.room_type.set("--Select room type--")
        self.available_room.set("")
        self.meal.set("--Select meal type--")
        self.no_of_days.set("")
        self.total_cost.set("")
        return

    def update_data(self):
        try:
            if(self.user_exists()):
                db_cursor = self.db_con.db.cursor()
                query=("update roombooking_details SET Checkin_date = %s,Checkout_date = %s,roomtype = %s,room_available = %s,meal =%s,NoOfDays = %s,Totalcost =%s where Contact_no = %s")
                values = (
                    self.checkin_date.get(),
                    self.checkout_date.get(),
                    self.room_type.get(),
                    self.available_room.get(),
                    self.meal.get(),
                    self.no_of_days.get(),
                    self.total_cost.get(),
                    self.contact_num.get(),
                )
                db_cursor.execute(query,values)
                self.db_con.db.commit()
                messagebox.showinfo("Success", "Data updated successfully",parent = self.root)
                self.fetch_all_data()
                self.engine.say("Data updated successfully")
                self.engine.runAndWait()

        except Exception as e:
            messagebox.showerror(
                "Error", f"{self.db_con.db.rollback()}", parent=self.root)
            print(e)

    
    def search_validations(self):
        search_bool = False
        if self.search_type.get() == "--select search type" or self.search_type.get() == "":
                self.engine.say("Please select the search type")
                self.engine.runAndWait()
                messagebox.showerror("Error", "Please select the search type",parent = self.root)

        elif self.entry_text.get() == "":
                self.engine.say("search field is empty")
                self.engine.runAndWait()
                messagebox.showerror(
                    "Error", "Please fill the field to search",parent = self.root)
        else:
                search_bool = True

        
        return search_bool

    def get_search_data(self):
        if(self.search_validations()):
            query = ""
            data = ""
            if self.search_type.get() == "Contact no":
                query = """select * from roombooking_details where Contact_no like %s """

            elif self.search_type.get() == "Room no":
                query = """select * from roombooking_details where room_available like %s """

            else:
                self.engine.say("Please select right search type")
                self.engine.runAndWait()
                messagebox.showwarning(
                    "Warning", "Please select the right search type",parent = self.root)

            db_cursor = self.db_con.db.cursor()
            db_cursor.execute(query, (self.entry_text.get()+"%",))
            rows = db_cursor.fetchall()
            if len(rows) != 0:
                self.room_table.delete(
                    *self.room_table.get_children())
                for i in rows:
                    self.room_table.insert("", END, values=i)
                    self.db_con.db.commit()

        return

    def __init__(self, root):

        self.root = root
        self.root.geometry('890x385+430+200')
        self.root.title('Room booking')

        ################################### VARIABLES ##############################################
        self.contact_num = StringVar()
        self.checkin_date = StringVar()
        self.checkout_date = StringVar()
        self.room_type = StringVar()
        self.available_room = StringVar()
        self.meal = StringVar()
        self.no_of_days = StringVar()
        self.total_cost = StringVar()
        ############################################################################################

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

        contact_entry = ttk.Entry(left_side_frame, font=(
            "new times roman", 9, "bold"), textvariable=self.contact_num)
        contact_entry.place(x=5, y=20, width=120)

        # fetchbutton
        fetch_button = Button(left_side_frame, font=("new times roman", 9, "bold"),
                              text="FETCH", command=self.fetch_data, fg="gold", bg="black", padx=5, pady=-130)
        fetch_button.place(x=127, y=18)

        # check in date entry
        check_in_lbl = ttk.Label(left_side_frame, text='Check in date', font=(
            "new times roman", 9, "bold"))
        check_in_lbl.place(x=190, y=2)

        check_in_date_entry = DateEntry(
            left_side_frame, font=("new times roman", 9, "bold"), date_pattern="dd/mm/y", mindate=date.today(), selectmode='day', textvariable=self.checkin_date)
        check_in_date_entry.place(x=190, y=20, width=160)

        # check out date entry
        check_out_lbl = ttk.Label(
            left_side_frame, text="Check out date", font=("new times roman", 9, "bold"))
        check_out_lbl.place(x=2, y=60)

        check_out_date_entry = DateEntry(left_side_frame, selectmode='day', mindate=date.today(), date_pattern="dd/mm/y", font=(
            "new times roman", 9, "bold"), textvariable=self.checkout_date)
        check_out_date_entry .place(x=5, y=78, width=160)

        # room type combobox
        room_type_lbl = ttk.Label(
            left_side_frame, text="Room type", font=("new times roman", 9, "bold"))
        room_type_lbl.place(x=190, y=60)

        room_type_combo_box = ttk.Combobox(
            left_side_frame, font=("new times roman", 9, "bold"), width=160, textvariable=self.room_type)
        room_type_combo_box["values"] = [
            "--Select room type---", "AC", "NON AC", "Duplex", "Luxury"]
        room_type_combo_box.current(0)
        room_type_combo_box.place(x=190, y=78, width=160)
        self.room_type.trace('w',self.fetch_room_numbers)

        # available room no entry
        available_room_no_lbl = ttk.Label(
            left_side_frame, text="Available room no", font=("new times roman", 9, "bold"))
        available_room_no_lbl.place(x=2, y=116)

        self.available_room_no_combobox = ttk.Combobox(left_side_frame,font=("new times roman",9,"bold"),textvariable=self.available_room)
        self.available_room_no_combobox["values"] = self.fetch_room_numbers()
        self.available_room_no_combobox.place(x=5,y=135,width=160)

        # meal combo box
        meal_lbl = ttk.Label(left_side_frame, text="Meal",
                             font=("new times roman", 9, "bold"))
        meal_lbl.place(x=190, y=116)

        meal_combo_box = ttk.Combobox(left_side_frame, font=(
            "new times roman", 9, "bold"), textvariable=self.meal)
        meal_combo_box.place(x=190, y=135, width=160)
        meal_combo_box["values"] = ["--Select meal--",
                                    "Breakfast", "Brunch", "Lunch", "Dinner"]
        meal_combo_box.current(0)

        # no of days entry
        no_of_days_lbl = ttk.Label(
            left_side_frame, text="No of days", font=("new times roman", 9, "bold"))
        no_of_days_lbl.place(x=2, y=175)

        no_of_days_entry = ttk.Entry(left_side_frame, font=(
            "new times roman", 9, "bold"), textvariable=self.no_of_days)
        no_of_days_entry.place(x=5, y=195, width=160)

        # paid tax entry
        total_cost_lbl = ttk.Label(
            left_side_frame, text="Total cost", font=("new times roman", 9, "bold"))
        total_cost_lbl.place(x=190, y=175)

        total_cost_entry = ttk.Entry(left_side_frame, font=(
            "new times roman", 9, "bold"), width=160, textvariable=self.total_cost)
        total_cost_entry.place(x=190, y=195, width=160)

        ############################################################################################################

        ###################################### LEFT SIDE FRAME BUTTONS ############################################

        # bottom frame
        bottom_frame = ttk.Frame(left_side_frame, relief=RIDGE)
        bottom_frame.place(x=2, y=225, width=380, height=78)

        # add button
        add_btn = Button(bottom_frame, text="ADD", fg="gold", bg="black", font=(
            "new times roman", 12, "bold"), padx=15, pady=2, command=self.add_data)
        add_btn.grid(row=0, column=0)

        # update button
        update_btn = Button(bottom_frame, text="UPDATE", fg="gold", bg="black", font=(
            "new times roman", 12, "bold"), padx=15, pady=2, command=self.update_data)
        update_btn.grid(row=0, column=1, padx=1)

        # delete button
        delete_btn = Button(bottom_frame, text="DELETE", fg="gold", bg="black", font=(
            "new times roman", 12, "bold"), padx=15, pady=2, command=self.delete_data)
        delete_btn.grid(row=0, column=2, padx=1)

        # clear button
        clear_btn = Button(bottom_frame, text="CLEAR", fg="gold", bg="black", font=(
            "new times roman", 12, "bold"), padx=5, pady=2, command=self.clear_entry)
        clear_btn.grid(row=0, column=3, padx=1, pady=3)

        bill_btn = Button(bottom_frame, command=self.total, text="BILL", fg="gold", bg="black", font=(
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
        search = ("--select search type", "Contact no", "Room no")
        combo_search = ttk.Combobox(
            right_side_frame, textvariable=self.search_type,font=("new times roman", 9, "bold"))
        combo_search['values'] = search
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=3)

        # search entry
        self.entry_text = StringVar()
        search_entry = Entry(right_side_frame,textvariable=self.entry_text ,font=(
            "new times roman", 9, "bold"))
        search_entry.grid(row=0, column=2, padx=3)

        # show button
        show_btn = Button(right_side_frame, text="SHOW", font=(
            "new times roman", 9, "bold"), fg="gold", bg="black",command=self.get_search_data)
        show_btn.grid(row=0, column=3, padx=3)

        # show all button
        show_all_btn = Button(right_side_frame, text="SHOW ALL", font=(
            "new times roman", 9, "bold"), fg="gold", bg="black",command=self.fetch_all_data)
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
        self.room_table.bind(
            "<ButtonRelease-1>", self.get_row_details)

        # filling content in frame from both side (i.e from x-axis and y-axis both)
        self.room_table.pack(fill=BOTH, expand=1)
        self.fetch_all_data()


if __name__ == '__main__':
    room_win_root = Tk()
    cusomer_obj = Room(room_win_root)
    room_win_root.mainloop()
