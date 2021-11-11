
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import random
import pyttsx3
import re
from db_connector import DBConnection
import requests
import os
class room_manage:
        def __init__(self, root):
         self.root = root
         self.root.geometry('890x385+430+200')
         self.root.title('MANAGE ROOM')
         self.root.resizable(width=False, height=False)

if __name__ == '__main__':
    root = Tk()
    room_mng = room_manage(root)
    root.mainloop()