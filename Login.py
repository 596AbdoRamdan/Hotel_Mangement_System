# -- coding: utf-8 --
"""
Created on Sun Aug  4 17:31:02 2024

@author: fahme
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

font = ('Microsoft YaHei UI Light', 23, 'bold')
root = Tk()
root.title('Login')

root.geometry('1280x832')
root.configure(bg='#aedea2')
root.resizable(False,False)



img_original = Image.open("final.png")
image_tk = ImageTk.PhotoImage(img_original)
Label(root, image=image_tk, bg='white').place(y=0, x=0)


##### frame
frame = Frame(root, width=400, height=340, bg="")
#frame = Frame(root, width=400, height=350, bg='#aedea2')
frame.place(x=440, y=260)


######functions
def login():
    user = usernametxt.get()
    passw = passwordtxt.get()

    if user != "admin" or passw != "admin":
        messagebox.showerror("Error", "Invalid username or password.")


######login
heading = Label(frame, text='Log in', fg='white', bg='#aedea2', font=font)
heading.place(x=150, y=20)

######username
username = Label(frame, text="Username", bg='#aedea2', fg="white", font=('Microsoft YaHei UI Light', 15, 'bold'))
usernametxt = Entry(frame, font=('Microsoft YaHei UI Light', 11), border=1, width=25)
username.place(x=20, y=110)
usernametxt.place(x=150, y=115)

#####password
password = Label(frame, text="Password", font=('Microsoft YaHei UI Light', 15, 'bold'), bg='#aedea2', fg='white')
passwordtxt = Entry(frame, bg='white', show="*", font=('Microsoft YaHei UI Light', 11), border=1, width=25)
password.place(x=20, y=170)
passwordtxt.place(x=150, y=175)

######login button
login_bt = Button(frame, text="login", font=('Microsoft YaHei UI Light', 15, 'bold'), width=12, bg='#62bf4b',
                  fg='white', border=0, command=login)
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