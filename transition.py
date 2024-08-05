from tkinter import Tk
from Login import LoginPage
from mainPage import HotelMangementSystem

def open_login_page():
    root = Tk()
    app = LoginPage(root)
    root.mainloop()

def open_main_page():
    root = Tk()
    app = HotelMangementSystem(root)
    root.mainloop()
