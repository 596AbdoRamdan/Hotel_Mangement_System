# Refactored Login.py

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from mainPage import HotelMangementSystem

class LoginPage():
    def __init__(self, root):
        icon = PhotoImage(file=r"images/hotel.png")
        root.iconphoto(True, icon)
        self.root = root
        self.root.title('Login')
        self.root.geometry("1550x800+0+0")
        self.root.configure(bg='#aedea2')
        self.root.resizable(False, False)

        # Connect to database and create table if not exists
        self.setup_database()

        img_original = Image.open("Login_Icon.jpg")
        new_image = img_original.resize((1550, 800))
        new_image.save('hotel2.jpg')
        image_tk = ImageTk.PhotoImage(new_image)
        Label(self.root, image=image_tk, bg='white').place(y=0, x=0)

        # Frame
        frame = Frame(self.root, width=420, height=350, bg="sienna")
        frame.place(x=580, y=350)

        # Login GUI elements
        font = ('Microsoft YaHei UI Light', 23, 'bold')
        heading = Label(frame, text='Log in', fg='white', bg='sienna', font=font)
        heading.place(x=150, y=20)

        username = Label(frame, text="Username", bg='sienna', fg="white", font=('Microsoft YaHei UI Light', 17, 'bold'))
        self.usernametxt = Entry(frame, font=('Microsoft YaHei UI Light', 11), border=1, width=25)
        username.place(x=20, y=110)
        self.usernametxt.place(x=150, y=115)

        password = Label(frame, text="Password", font=('Microsoft YaHei UI Light', 17, 'bold'), bg='sienna', fg='white')
        self.passwordtxt = Entry(frame, bg='white', show="*", font=('Microsoft YaHei UI Light', 11), border=1, width=25)
        password.place(x=20, y=170)
        self.passwordtxt.place(x=150, y=175)

        login_bt = Button(frame, text="login", font=('Microsoft YaHei UI Light', 17, 'bold'), width=12, bg='sienna', fg='white', border=0, command=self.login)
        login_bt.place(x=120, y=250)

        self.root.mainloop()

    def setup_database(self):
        db = sqlite3.connect('hotel.db')
        cr = db.cursor()
        cr.execute("CREATE TABLE if not exists users (user_id INTEGER, name TEXT, pass TEXT)")

        users_data = [
            # (1, 'Yomna', 'Yo123'),
            # (2, 'Yasmine', 'Ya456'),
            # (3, 'Ramadan', 'Ra789'),
            # (4, 'Bebo', 'Be3094')
            # (5, 'wafdy', '1234')
        ]
        for user in users_data:
            cr.execute("INSERT OR IGNORE INTO users (user_id, name, pass) VALUES (?, ?, ?)", user)

        db.commit()
        db.close()

    def login(self):
        user = self.usernametxt.get()
        passw = self.passwordtxt.get()

        db = sqlite3.connect('hotel.db')
        cr = db.cursor()
        cr.execute("SELECT * FROM users WHERE name = ? AND pass = ?", (user, passw))
        result = cr.fetchone()
        db.close()

        if result:
            self.root.destroy()
            new_window = Tk()
            app = HotelMangementSystem(new_window)
        else:
            messagebox.showerror("Error", "Invalid username or password.")

if __name__ == "__main__":
    root = Tk()
    app = LoginPage(root)
