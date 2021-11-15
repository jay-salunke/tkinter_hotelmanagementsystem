from tkinter import *
from tkinter.font import BOLD
from PIL import Image, ImageTk
from customer import Customer
from room import Room
from room_manage import RoomManage
from login import Login



class Home:
    def customer_window(self):
        self.customer_window = Toplevel(self.root)
        Customer(self.customer_window)

    def room_windows(self):
        self.room_window = Toplevel(self.root)
        Room(self.room_window)

    def room_manage(self):
        self.room_manage = Toplevel(self.root)
        RoomManage(self.room_manage)
    
    def logout(self):
        self.root.destroy()  
        login_screen = Tk()
        Login(login_screen)
           

    def __init__(self, root):

        self.root = root

        self.root.title('HOME PAGE')

        self.root.geometry('1100x600+230+30')

        self.root.resizable(width=False, height=False)

        ########################################### HOTEL LOGO #########################################################
        img_1 = Image.open(
            'D:\python_tkinter_project\images\golden-hotel-logo-free-graphics-472233.jpg')
        img_1 = img_1.resize((250, 100), Image.ANTIALIAS)
        self.photo_img_1 = ImageTk.PhotoImage(img_1)
        image_lbl_1 = Label(
            self.root, image=self.photo_img_1, relief=RIDGE, bd=2)
        image_lbl_1.place(x=0, y=0)
        ########################################### HOTEL LOGO #########################################################

        img_2 = Image.open(
            'D:\python_tkinter_project\images\palace-hotels-india-hero.jpg')
        img_2 = img_2.resize((1100, 100), Image.ANTIALIAS)
        self.photo_img_2 = ImageTk.PhotoImage(img_2)
        image_lbl_2 = Label(
            self.root, image=self.photo_img_2, relief=RIDGE, bd=2)
        image_lbl_2.place(x=230, y=0)

        lbl_title = Label(self.root, text='HOTEL ROYAL', fg='gold', bd=3,
                          bg='black', padx=485, pady=10, font=('new times roman', 13, BOLD))
        lbl_title.place(x=3, y=105)

        ######################################## FRAME ##############################################################################
        main_frame = Frame(self.root, width=1100, height=600, relief=RIDGE)
        main_frame.place(x=0, y=140)

        ####################################### MENU BAR ##########################################################################
        menu_lbl = Label(self.root, fg='gold', bg='black', relief=RIDGE, text='MENU', font=(
            'new times roman', 12, BOLD), padx=68, pady=7)
        menu_lbl.place(x=2, y=141)

        ################################### BUTTON FRAME #######################################################
        button_frame = Frame(main_frame, width=172, height=400,)
        button_frame.place(x=2, y=35)

        ################################################# BUTTONS ###############################################

        # customer button
        customer_btn = Button(button_frame, width=15, bg='black', text="CUSTOMER", fg='gold', padx=15, pady=4, font=(
            'new times roman', 12, 'bold'), cursor='hand1', command=self.customer_window)
        customer_btn.grid(row=0, column=0)

        # room button
        room_booking_btn = Button(button_frame, width=15, bg='black', text="ROOM", fg='gold', padx=15, pady=4, font=(
            'new times roman', 12, 'bold'), cursor='hand1', command=self.room_windows)
        room_booking_btn.grid(row=1, column=0)

        # details button
        details_btn = Button(button_frame, width=15, bg='black', text="DETAILS", fg='gold',
                             padx=15, pady=4, font=('new times roman', 12, 'bold'), cursor='hand1', command=self.room_manage)
        details_btn.grid(row=2, column=0)

        # Logout button

        logout_btn = Button(button_frame, width=15, bg='black', text="LOGOUT", fg='gold',
                            padx=15, pady=4, font=('new times roman', 12, 'bold'), cursor='hand1',command=self.logout)
        logout_btn.grid(row=3, column=0)

        #################################### RIGHT SIDE IMAGE #############################################

        ##################################### FOOD IMAGE1 ###############################################
        food_img_1 = Image.open(
            'D:\\python_tkinter_project\\images\\food_image_2.jpg')
        food_img_1 = food_img_1.resize((188, 121), Image.ANTIALIAS)
        self.food_image_1 = ImageTk.PhotoImage(food_img_1)
        food_image_lbl_1 = Label(self.root, image=self.food_image_1)
        food_image_lbl_1.place(x=1, y=326)
        ##################################### FOOD IMAGE2 ###############################################

        food_image_2 = Image.open(
            'D:\\python_tkinter_project\\images\\food_image.jpg')
        food_image_2 = food_image_2.resize((186, 115), Image.ANTIALIAS)
        self.food_image_2 = ImageTk.PhotoImage(food_image_2)
        food_image_lbl_2 = Label(self.root, image=self.food_image_2)
        food_image_lbl_2.place(x=1, y=450)

        ######################### END OF RIGHT SIDE IMAGES #############################################

        ################################## BLACK BAR #################################################
        bar_lbl = Label(self.root, fg='gold', bg='black',
                        width=1100, height=2, text='Copyright')
        bar_lbl.place(x=0, y=570)


if __name__ == '__main__':
    root = Tk()
    reg_obj = Home(root)
    root.mainloop()
