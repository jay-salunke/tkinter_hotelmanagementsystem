
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import random
import pyttsx3
import re
from db_connector import DBConnection
import requests
from dotenv import load_dotenv
import os
class Customer:
    # db_connector object
    db_con = DBConnection()

    engine = pyttsx3.init()

    ################# VOICE #####################
    # getting details of current voice
    voices = engine.getProperty('voices')

    # engine.setProperty('voice', voices[0].id)
    # changing index, changes voices. o for male

    engine.setProperty('voice', voices[1].id)
   ###############################################

    # return True if no validation_error
    #  else validation_error

    def nation_names(self):
        url = "https://api.countrystatecity.in/v1/countries"

        headers = {
                    'X-CSCAPI-KEY': os.getenv("API_KEY")
                    }

        response = requests.request("GET", url, headers=headers)

        self.data = response.json()
        countries = [x['name'] for x in self.data]
        return countries
        
    def states_names(self,*args):
        dict_countries = {x['name']: x['iso2'] for x in self.data}        
        url = "https://api.countrystatecity.in/v1/countries/"+dict_countries[self.nationality.get()]+"/states"

        headers = {
                    'X-CSCAPI-KEY': os.getenv("API_KEY")
                    }

        response = requests.request("GET", url, headers=headers)

        data = response.json()
        self.customer_state_dropdown_list.set("")
        self.customer_state_dropdown_list['values'] = [x['name'] for x in data]
        return  

    def form_validation(self):
        no_error = False

        if(self.name.get() == ""):
            self.engine.say("Name field is Empty")
            self.engine.runAndWait()
            messagebox.showerror(
                "Error", "Name field is Empty", parent=self.root)

        elif(re.search('[\\d]', self.name.get())):
            self.engine.say('numbers are not allowed')
            self.engine.runAndWait()
            messagebox.showerror(
                "Error", "Numbers are not allowed", parent=self.root)

        elif(self.email_id.get() == ""):
            self.engine.say("Email id field is empty")
            self.engine.runAndWait()
            messagebox.showerror(
                "Error", "Email id is Empty", parent=self.root)

        elif(self.mobile_no.get() == ""):
            self.engine.say("Mobile field is empty")
            self.engine.runAndWait()
            messagebox.showerror(
                "Error", "Mobile no is empty", parent=self.root)

        elif(not re.match('^[\\d]+$', self.mobile_no.get())):
            self.engine.say('characters are not allowed')
            self.engine.runAndWait()
            messagebox.showerror(
                "Error", "Characters are not allowed", parent=self.root)

        elif(len(self.mobile_no.get()) > 10 or len(self.mobile_no.get()) <= 9):
            self.engine.say('Enter 10 digits number only')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Enter the 10 digits number only")

        elif(self.nationality.get() == ""):
            self.engine.say("please fill the nationality field")
            self.engine.runAndWait()
            messagebox.showerror(
                "Error", "please fill the nationality field", parent=self.root)

        elif(self.state.get() == "--Select State" or self.state.get() == ""):
            self.engine.say("please select the state")
            self.engine.runAndWait()
            messagebox.showerror(
                "Error", "Please select the state", parent=self.root)

        elif(self.gender.get() == "--Select Gender--" or self.gender.get() == ""):
            self.engine.say("please select the gender")
            self.engine.runAndWait()
            messagebox.showerror(
                "Error", "please select the gender", parent=self.root)

        elif(self.proof_type.get() == "--Select Proof Type" or self.proof_type.get() == ""):
            self.engine.say("please select the proof type")
            self.engine.runAndWait()
            messagebox.showerror(
                "Error", "please select the proof type", parent=self.root)
        else:
            no_error = True

        return no_error

        # adds the data into database
        # if there is no validation error

    def add_data(self):
        if(self.form_validation()):
            try:
                db_cursor = self.db_con.db.cursor()
                db_cursor.execute("insert into customers_details(ref_id,customer_name,customer_email_id,customer_mobile_no,customer_nationality,customer_state,customer_gender,customer_proof_type) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.id.get(),
                    self.name.get(),
                    self.email_id.get(),
                    self.mobile_no.get(),
                    self.nationality.get(),
                    self.state.get(),
                    self.gender.get(),
                    self.proof_type.get()
                ))
                self.db_con.db.commit()
                self.engine.say("Data inserted successfully")
                self.engine.runAndWait()
                self.fetch_data()
                self.clear_entry()
                messagebox.showinfo(
                    "Success", "Data inserted successfully", parent=self.root)

            except Exception as e:
                self.db_con.db.rollback()
                messagebox.showwarning(
                    "Warning", f"{str(e)}", parent=self.root)
        return

    def user_exists(self):
        if(self.form_validation()):
            user_exist = False
            db_cursor = self.db_con.db.cursor()
            db_cursor.execute("select ref_id from customers_details where ref_id = %s", (
                self.id.get(),
            ))
            row_count = db_cursor.fetchall()
            if len(row_count) == 1:
                user_exist = True
            return user_exist

    def fetch_data(self):
        try:
            db_cursor = self.db_con.db.cursor()
            db_cursor.execute("select * from customers_details")
            rows = db_cursor.fetchall()
            if len(rows) != 0:
                self.customer_details_table.delete(
                    *self.customer_details_table.get_children())
                for i in rows:
                    self.customer_details_table.insert("", END, values=i)
                self.db_con.db.commit()
        except Exception as e:
            messagebox.showerror("Error", f"{self.db_con.db.rollback()}")
            print(e)
        return

    def get_row_details(self, events=""):
        cursor_row = self.customer_details_table.focus()
        row_content = self.customer_details_table.item(cursor_row)
        row = row_content["values"]
        self.id.set(row[0])
        self.name.set(row[1])
        self.email_id.set(row[2])
        self.mobile_no.set(row[3])
        self.nationality.set(row[4])
        self.state.set(row[5])
        self.gender.set(row[6])
        self.proof_type.set(row[7])

    def update_data(self):
        try:
            if(self.user_exists()):
                db_cursor = self.db_con.db.cursor()
                db_cursor.execute("update customers_details SET ref_id = %s ,customer_name = %s ,customer_email_id = %s ,customer_mobile_no = %s,customer_nationality = %s,customer_state = %s,customer_gender = %s,customer_proof_type = %s where ref_id = %s ", (
                    self.id.get(),
                    self.name.get(),
                    self.email_id.get(),
                    self.mobile_no.get(),
                    self.nationality.get(),
                    self.state.get(),
                    self.gender.get(),
                    self.proof_type.get(),
                    self.id.get(),
                ))
                self.db_con.db.commit()
                messagebox.showinfo("Success", "Data updated successfully")
                self.fetch_data()
                self.engine.say("Data updated successfully")
                self.engine.runAndWait()

        except Exception as e:
            messagebox.showerror(
                "Error", f"{self.db_con.db.rollback()}", parent=self.root)
            print(e)

        return

    def delete_data(self):
        if (self.user_exists()):
            try:
                db_cursor = self.db_con.db.cursor()
                db_cursor.execute("delete from customers_details where ref_id = %s", (
                    self.id.get(),
                ))
                self.db_con.db.commit()
                self.fetch_data()
                self.engine.say("Data deleted successfully")
                self.engine.runAndWait()
                messagebox.showinfo(
                    "Success", "Data is deleted successfully", parent=self.root)
                self.clear_entry()
            except Exception as e:
                messagebox.showwarning(
                    "Warning", f"{self.db_con.db.rollback()}", parent=self.root)
                print(e)

        return

    def clear_entry(self):
        self.id.set(str(random.randint(1000, 9999)))
        self.name.set("")
        self.email_id.set("")
        self.mobile_no.set("")
        self.nationality.set("")
        self.state.set("--Select State--")
        self.gender.set("--Select Gender--")
        self.proof_type.set("--Select Proof Type")
        return

    def search_validations(self):
        search_bool = False
        try:
            if self.search_type.get() == "--select search type" or self.search_type.get() == "":
                self.engine.say("Please select the search type")
                self.engine.runAndWait()
                messagebox.showerror("Error", "Please select the search type")

            elif self.entry_text.get() == "":
                self.engine.say("search field is empty")
                self.engine.runAndWait()
                messagebox.showerror(
                    "Error", "Please fill the field to search")
            else:
                search_bool = True

        except Exception as e:
            messagebox.showwarning("Warning", f"{e}")
            print(e)
        return search_bool

    def get_search_data(self):
        if(self.search_validations()):
            query = ""
            data = ""
            if self.search_type.get() == "Mobile no":
                query = """select * from customers_details where customer_mobile_no like %s """

            elif self.search_type.get() == "Name":
                query = """select * from customers_details where customer_name like %s """

            elif self.search_type.get() == "Customer Id":
                query = """select * from customers_details where ref_id like %s"""

            elif self.search_type.get() == "Nationality":
                query = """select * from customers_details where customer_nationality like %s"""

            elif self.search_type.get() == "State":
                query = """select * from customers_details where customer_state like %s"""

            else:
                self.engine.say("Please select right search type")
                self.engine.runAndWait()
                messagebox.showwarning(
                    "Warning", "Please select the right search type")

            db_cursor = self.db_con.db.cursor()
            db_cursor.execute(query, (self.entry_text.get()+"%",))
            rows = db_cursor.fetchall()
            if len(rows) != 0:
                self.customer_details_table.delete(
                    *self.customer_details_table.get_children())
                for i in rows:
                    self.customer_details_table.insert("", END, values=i)
                    self.db_con.db.commit()

        return

    def __init__(self, root):
        load_dotenv()
        self.root = root
        self.root.geometry('890x385+430+200')
        self.root.title('Customer details')
        self.root.resizable(width=False, height=False)

        ################################### VARIABLES ##############################################
        rand_number = random.randint(1000, 9999)
        self.id = StringVar()
        self.id.set(str(rand_number))
        self.name = StringVar()
        self.email_id = StringVar()
        self.mobile_no = StringVar()
        self.nationality = StringVar()
        self.state = StringVar()
        self.gender = StringVar()
        self.proof_type = StringVar()
        ############################################################################################

        ################################### CUSTOMER DETAIL TITLE###################################
        customer_details_title = Label(self.root, bg="black", fg="gold", text="ADD CUSTOMER DETAILS",
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

        #####################################LEFT SIDE FRAME #######################################
        left_side_frame = LabelFrame(
            self.root, text='ADD DETAILS', relief=RIDGE, font=("new times roman", 11, "bold"))
        left_side_frame.place(x=2, y=54, width=385, height=330)

        ##################################### ADD DETAIL ENTRIES ####################################

        # customer name
        name_lbl = ttk.Label(left_side_frame, text="Customer Name", font=(
            "new times roman", 9, "bold"))
        name_lbl.place(x=2, y=2)

        name_entry = ttk.Entry(left_side_frame, font=(
            "new times roman", 9, "bold"), textvariable=self.name)
        name_entry.place(x=5, y=20, width=160)

        # customer email id
        email_lbl = ttk.Label(left_side_frame, text='Customer Email ID', font=(
            "new times roman", 9, "bold"))
        email_lbl.place(x=190, y=2)

        email_entry = ttk.Entry(
            left_side_frame, font=("new times roman", 9, "bold"), textvariable=self.email_id)
        email_entry.place(x=190, y=20, width=160)

        # customer mobile no
        mobile_no_lbl = ttk.Label(left_side_frame, text="Customer Mobile No.", font=(
            "new times roman", 9, "bold"))
        mobile_no_lbl.place(x=2, y=60)

        mobile_no_entry = ttk.Entry(
            left_side_frame, font=("new times roman", 9, "bold"), textvariable=self.mobile_no)
        mobile_no_entry.place(x=5, y=78, width=160)

        # customer nationality
        customer_nationality_lbl = ttk.Label(
            left_side_frame, text="Customer Nationality", font=("new times roman", 9, "bold"))
        customer_nationality_lbl.place(x=190, y=60)

        customer_nationality_dropdown_list = ttk.Combobox(
            left_side_frame,font=("new times roman",9,"bold"),textvariable=self.nationality,width=160)
        customer_nationality_dropdown_list.place(x=190,y=78,width=160)
        customer_nationality_dropdown_list["values"] = self.nation_names()
        customer_nationality_dropdown_list.current(0)
        self.nationality.trace('w',self.states_names)


        # customer state
        customer_state_lbl = ttk.Label(
            left_side_frame, text="Select State", font=("new times roman", 9, "bold"))
        customer_state_lbl.place(x=2, y=116)

        self.customer_state_dropdown_list = ttk.Combobox(
            left_side_frame, font=("new times roman", 9, "bold"), textvariable=self.state, width=160)
        self.customer_state_dropdown_list.place(x=5, y=135, width=160)
        self.customer_state_dropdown_list["values"] = self.states_names()
        

        # customer gender
        gender = ("--Select Gender--", "Male", "Female", "Other")
        customer_gender_lbl = Label(
            left_side_frame, text="Select Gender", font=("new times roman", 9, "bold"))
        customer_gender_lbl.place(x=190, y=116)

        customer_gender_dropdown_list = ttk.Combobox(
            left_side_frame, font=("new times roman", 9, "bold"), textvariable=self.gender)
        customer_gender_dropdown_list['values'] = gender
        customer_gender_dropdown_list.current(0)
        customer_gender_dropdown_list.place(x=190, y=135, width=160)

        # customer proof type
        customer_proofs_type = ("--Select Proof Type",
                                "Aadhaar Card", "Pan Card", "Passport")

        customer_proof_type_lbl = ttk.Label(left_side_frame, font=(
            "new times roman", 9, "bold"), text="Proof type")
        customer_proof_type_lbl.place(x=2, y=175)

        customer_proof_type_dropdown_list = ttk.Combobox(
            left_side_frame, font=("new times roman", 9, "bold"), textvariable=self.proof_type)
        customer_proof_type_dropdown_list.place(x=5, y=195)
        customer_proof_type_dropdown_list['values'] = customer_proofs_type
        customer_proof_type_dropdown_list.current(0)

        # random generated customer ref_id
        customer_ref_id_lbl = Label(left_side_frame, font=(
            "new times roman", 9, "bold"), text="Reference id")
        customer_ref_id_lbl.place(x=190, y=175)

        customer_ref_id_entry = Entry(left_side_frame, textvariable=self.id, font=(
            "new times roman", 9, "bold"), state="readonly")
        customer_ref_id_entry.place(x=190, y=195, width=160)

        ###########################################################################################################

        ###################################### LEFT SIDE FRAME BUTTONS ############################################

        # bottom frame
        bottom_frame = ttk.Frame(left_side_frame, relief=RIDGE)
        bottom_frame.place(x=2, y=225, width=380, height=40)

        # add button
        add_btn = Button(bottom_frame, command=self.add_data, text="ADD", fg="gold", bg="black", font=(
            "new times roman", 12, "bold"), padx=15, pady=2)
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

        ####################################################################################################

        ##################################### RIGHT SIDE FRAME ############################################
        self.search_type = StringVar()
        # frame
        right_side_frame = LabelFrame(
            self.root, text='VIEW DETAILS', relief=RIDGE, font=("new times roman", 11, "bold"))
        right_side_frame.place(x=390, y=54, width=500, height=330)

        # search combo box
        search = ("--select search type", "Mobile no", "Name",
                  "Customer Id", "Nationality", "State")
        combo_search = ttk.Combobox(
            right_side_frame, font=("new times roman", 9, "bold"), textvariable=self.search_type)
        combo_search['values'] = search
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=3)

        # search entry
        self.entry_text = StringVar()
        search_entry = Entry(right_side_frame, font=(
            "new times roman", 9, "bold"), textvariable=self.entry_text)
        search_entry.grid(row=0, column=2, padx=3)

        # show button
        show_btn = Button(right_side_frame, text="SHOW", font=(
            "new times roman", 9, "bold"), fg="gold", bg="black", command=self.get_search_data)
        show_btn.grid(row=0, column=3, padx=3)

        # show all button
        show_all_btn = Button(right_side_frame, text="SHOW ALL", font=(
            "new times roman", 9, "bold"), fg="gold", bg="black", command=self.fetch_data)
        show_all_btn.grid(row=0, column=4, padx=3)

        #######################################TABLE #########################################

        # table frame
        table_frame = Frame(right_side_frame, border=2)
        table_frame.place(x=0, y=40, width=500, height=270)

        # X-axis and Y-axis ScrollBar
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.customer_details_table = ttk.Treeview(table_frame, columns=(
            "id", "name", "email id", "mobile no", "nationality", "state", "gender", "proof type"), xscrollcommand=scroll_x, yscrollcommand=scroll_y)

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.pack(side=BOTTOM, fill=X)

        scroll_x.config(command=self.customer_details_table.xview)
        scroll_y.config(command=self.customer_details_table.yview)

        # table heading
        self.customer_details_table.heading("id", text="Id")
        self.customer_details_table.heading("name", text="Name")
        self.customer_details_table.heading("email id", text="Email ID")
        self.customer_details_table.heading("mobile no", text="Mobile no")
        self.customer_details_table.heading("nationality", text="Nationality")
        self.customer_details_table.heading("state", text="State")
        self.customer_details_table.heading("gender", text="Gender")
        self.customer_details_table.heading("proof type", text="Proof type")
        self.customer_details_table["show"] = "headings"

        # setting column width
        self.customer_details_table.column("id", width=100)
        self.customer_details_table.column("name", width=100)
        self.customer_details_table.column("email id", width=100)
        self.customer_details_table.column("mobile no", width=100)
        self.customer_details_table.column("nationality", width=100)
        self.customer_details_table.column("state", width=100)
        self.customer_details_table.column("gender", width=100)
        self.customer_details_table.column("proof type", width=100)
        self.customer_details_table.bind(
            "<ButtonRelease-1>", self.get_row_details)

        # filling content in frame from both side (i.e from x-axis and y-axis both)
        self.customer_details_table.pack(fill=BOTH, expand=1)
        self.fetch_data()

        ##############################################################################################


if __name__ == '__main__':
    cust_win_root = Tk()
    cusomer_obj = Customer(cust_win_root)
    cust_win_root.mainloop()
