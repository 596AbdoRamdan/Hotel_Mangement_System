# -- coding: utf-8 --
"""
Created on Sun Aug  4 17:31:02 2024

@author: fahme
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from mainPage import HotelMangementSystem
db = sqlite3.connect('hotel.db')
cr = db.cursor()
#create the tables and fields
cr.execute("CREATE TABLE if not exists users (user_id INTEGER, name TEXT, pass password)")

#insert data to tables
cr.execute("insert into users (user_id , name ,pass) values(1, 'Yomna', 'Yo123')")
cr.execute("insert into users (user_id , name ,pass) values(2, 'Yasmine', 'Ya456')")
cr.execute("insert into users (user_id , name ,pass) values(3, 'Ramadan', 'Ra789')")
cr.execute("insert into users (user_id , name ,pass) values(4, 'Bebo', 'Be3094')")
#save data that we add
db.commit()
#close database
db.close()

font = ('Microsoft YaHei UI Light', 23, 'bold')
root = Tk()
root.title('Login')

root.geometry("1550x800+0+0")
root.configure(bg='#aedea2')
root.resizable(False,False)



img_original = Image.open("Login_Icon.jpg")
new_image = img_original.resize((1550, 800))
new_image.save('hotel2.jpg')
image_tk = ImageTk.PhotoImage(new_image)
Label(root, image=image_tk, bg='white').place(y=0, x=0)


##### frame
frame = Frame(root, width=420, height=350, bg="sienna")
frame.place(x=580, y=350)


######functions
def login():
    user = usernametxt.get()
    passw = passwordtxt.get()

    if user != "admin" or passw != "admin":
        messagebox.showerror("Error", "Invalid username or password.")
    else :
        # root.destroy()
        # rt = Tk()
        # rt.geometry('0x0')
        new_window=Toplevel(root)
        app = HotelMangementSystem(new_window)



######login

heading = Label(frame, text='Log in', fg='white', bg='sienna', font=font)
heading.place(x=150, y=20)

######username
username = Label(frame, text="Username", bg='sienna', fg="white", font=('Microsoft YaHei UI Light', 17, 'bold'))
usernametxt = Entry(frame, font=('Microsoft YaHei UI Light', 11), border=1, width=25)
username.place(x=20, y=110)
usernametxt.place(x=150, y=115)

#####password
password = Label(frame, text="Password", font=('Microsoft YaHei UI Light', 17, 'bold'), bg='sienna', fg='white')
passwordtxt = Entry(frame, bg='white', show="*", font=('Microsoft YaHei UI Light', 11), border=1, width=25)
password.place(x=20, y=170)
passwordtxt.place(x=150, y=175)

######login button
login_bt = Button(frame, text="login", font=('Microsoft YaHei UI Light', 17, 'bold'), width=12, bg='sienna',fg='white', border=0, command=login)
login_bt.place(x=120, y=250)

######signup button
# signup_label = Label(frame, text="Don't have an account?", fg="white", bg="#aedea2",
#                      font=('Microsoft YaHei UI Light', 13, 'bold'))
# signup_bt = Button(frame, text="Sign up", cursor='hand2', font=('Microsoft YaHei UI Light', 13, 'bold'), bg='#aedea2',
#                    fg='#1d820c', width=6, border=0)
# signup_label.place(x=50, y=313)
# signup_bt.place(x=260, y=310)
# signup_bt= Button(frame, text="signup", font=('Microsoft YaHei UI Light', 15, 'bold') , bg='#62bf4b', fg='white',width=12, border=0)


root.mainloop()
