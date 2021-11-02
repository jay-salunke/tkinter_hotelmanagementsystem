from os import name
from tkinter import *


class Room:

    def __init__(self, root):
        self.root = root
        self.root.geometry('890x385+430+200')
        self.root.title('Room booking')


if __name__ == '__main__':
    room_win_root = Tk()
    cusomer_obj = Room(room_win_root)
    room_win_root.mainloop()
