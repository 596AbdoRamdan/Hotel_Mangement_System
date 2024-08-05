from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from mainPage import HotelMangementSystem

# Connect to database and create table if not exists
db = sqlite3.connect('hotel.db')
cr = db.cursor()
cr.execute("CREATE TABLE if not exists users (user_id INTEGER, name TEXT, pass TEXT)")

# Insert data to tables if they do not exist
users_data = [
    (1, 'Yomna', 'Yo123'),
    (2, 'Yasmine', 'Ya456'),
    (3, 'Ramadan', 'Ra789'),
    (4, 'Bebo', 'Be3094')
]
# Using executemany to avoid duplicate entries
for user in users_data:
    cr.execute("INSERT OR IGNORE INTO users (user_id, name, pass) VALUES (?, ?, ?)", user)

# Save and close database
db.commit()
db.close()

# Set up the GUI
font = ('Microsoft YaHei UI Light', 23, 'bold')
root = Tk()
root.title('Login')
root.geometry("1550x800+0+0")
root.configure(bg='#aedea2')
root.resizable(False, False)

img_original = Image.open("Login_Icon.jpg")
new_image = img_original.resize((1550, 800))
new_image.save('hotel2.jpg')
image_tk = ImageTk.PhotoImage(new_image)
Label(root, image=image_tk, bg='white').place(y=0, x=0)

# Frame
frame = Frame(root, width=420, height=350, bg="sienna")
frame.place(x=580, y=350)

# Functions
def login():
    user = usernametxt.get()
    passw = passwordtxt.get()

    # Connect to database to check credentials
    db = sqlite3.connect('hotel.db')
    cr = db.cursor()
    cr.execute("SELECT * FROM users WHERE name = ? AND pass = ?", (user, passw))
    result = cr.fetchone()
    db.close()

    if result:
        root.destroy()  # Destroy the login window
        new_window = Tk()  # Create a new Tkinter window
        app = HotelMangementSystem(new_window)  # Initialize the main menu page
    else:
        messagebox.showerror("Error", "Invalid username or password.")

# Login GUI elements
heading = Label(frame, text='Log in', fg='white', bg='sienna', font=font)
heading.place(x=150, y=20)

username = Label(frame, text="Username", bg='sienna', fg="white", font=('Microsoft YaHei UI Light', 17, 'bold'))
usernametxt = Entry(frame, font=('Microsoft YaHei UI Light', 11), border=1, width=25)
username.place(x=20, y=110)
usernametxt.place(x=150, y=115)

password = Label(frame, text="Password", font=('Microsoft YaHei UI Light', 17, 'bold'), bg='sienna', fg='white')
passwordtxt = Entry(frame, bg='white', show="*", font=('Microsoft YaHei UI Light', 11), border=1, width=25)
password.place(x=20, y=170)
passwordtxt.place(x=150, y=175)

login_bt = Button(frame, text="login", font=('Microsoft YaHei UI Light', 17, 'bold'), width=12, bg='sienna', fg='white', border=0, command=login)
login_bt.place(x=120, y=250)

root.mainloop()
