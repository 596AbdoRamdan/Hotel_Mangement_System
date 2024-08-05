from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import sqlite3
from tkinter import messagebox


class RoomBooking:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1295x550+230+220')
        self.root.title('Room Booking')
        root.resizable(False, False)

        icon = PhotoImage(file=r"images/hotel.png")
        root.iconphoto(False, icon)

        # Variables
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomvaliable = StringVar()
        self.var_meal = StringVar()
        self.var_no_of_days = StringVar()
        self.var__paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

        # Title
        lbl1_title = Label(self.root, text='ROOM BOOKING DETAILS', font=('times new roman', 18, "bold"), bg='black',
                           fg='gold')
        lbl1_title.place(x=0, y=0, width=1295, height=50)

        # Logo
        img2 = Image.open(r"images/grandHotel.jpg")
        img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        # Label Frame
        labelFrameleft = LabelFrame(self.root, bd=2, relief=RIDGE, text='Room Booking Details',
                                    font=('arial', 12, "bold"), padx=2, pady=2)
        labelFrameleft.place(x=5, y=50, width=425, height=490)

        # Labels and Entries
        lbl1_contact = Label(labelFrameleft, text="Customer Contact", font=('arial', 12, "bold"), padx=2, pady=6)
        lbl1_contact.grid(row=0, column=0, sticky=W)
        entry_contact = Entry(labelFrameleft, textvariable=self.var_contact, font=('arial', 13, "bold"), width=20)
        entry_contact.grid(row=0, column=1, sticky=W)
        # -------------fetch Data Button---------------
        btnAdd = Button(labelFrameleft, text="Fetch Data", command=self.fetchbtn, font=("Arial", 8, "bold"), bg='black',
                        fg='gold', width=8, height=1)
        btnAdd.place(x=340, y=4)

        lbl_checkin = Label(labelFrameleft, text="Check-in Date", font=('arial', 12, "bold"), padx=2, pady=6)
        lbl_checkin.grid(row=1, column=0, sticky=W)
        entry_checkin = Entry(labelFrameleft, textvariable=self.var_checkin, font=('arial', 13, "bold"), width=20)
        entry_checkin.grid(row=1, column=1, sticky=W)

        lbl_checkout = Label(labelFrameleft, text="Check-out Date", font=('arial', 12, "bold"), padx=2, pady=6)
        lbl_checkout.grid(row=2, column=0, sticky=W)
        entry_checkout = Entry(labelFrameleft, textvariable=self.var_checkout, font=('arial', 13, "bold"), width=20)
        entry_checkout.grid(row=2, column=1, sticky=W)

        # Room_Type
        roomType = Label(labelFrameleft, text="Room Type", font=('arial', 12, "bold"), padx=2, pady=6)
        roomType.grid(row=3, column=0, sticky=W)
        combo_roomType = ttk.Combobox(labelFrameleft, font=('arial', 13, "bold"), textvariable=self.var_roomtype, state="readonly",
                                      width=18)
        combo_roomType["value"] = ("Single", "Double", "Doublex")
        combo_roomType.current(0)
        combo_roomType.grid(row=3, column=1)

        lbl_roomavailable = Label(labelFrameleft, text="Room Available", font=('arial', 12, "bold"), padx=2, pady=6)
        lbl_roomavailable.grid(row=4, column=0, sticky=W)
        entry_roomavailable = Entry(labelFrameleft, textvariable=self.var_roomvaliable, font=('arial', 13, "bold"),
                                    width=20)
        entry_roomavailable.grid(row=4, column=1, sticky=W)

        lbl_meal = Label(labelFrameleft, text="Meal", font=('arial', 12, "bold"), padx=2, pady=6)
        lbl_meal.grid(row=5, column=0, sticky=W)
        entry_meal = Entry(labelFrameleft, textvariable=self.var_meal, font=('arial', 13, "bold"), width=20)
        entry_meal.grid(row=5, column=1, sticky=W)

        lbl_no_of_days = Label(labelFrameleft, text="No. of Days", font=('arial', 12, "bold"), padx=2, pady=6)
        lbl_no_of_days.grid(row=6, column=0, sticky=W)
        entry_no_of_days = Entry(labelFrameleft, textvariable=self.var_no_of_days, font=('arial', 13, "bold"), width=20)
        entry_no_of_days.grid(row=6, column=1, sticky=W)

        lbl_paidtax = Label(labelFrameleft, text="Paid Tax", font=('arial', 12, "bold"), padx=2, pady=6)
        lbl_paidtax.grid(row=7, column=0, sticky=W)
        entry_paidtax = Entry(labelFrameleft, textvariable=self.var__paidtax, font=('arial', 13, "bold"), width=20)
        entry_paidtax.grid(row=7, column=1, sticky=W)

        lbl_actualtotal = Label(labelFrameleft, text="Sub Total", font=('arial', 12, "bold"), padx=2, pady=6)
        lbl_actualtotal.grid(row=8, column=0, sticky=W)
        entry_actualtotal = Entry(labelFrameleft, textvariable=self.var_actualtotal, font=('arial', 13, "bold"),
                                  width=20)
        entry_actualtotal.grid(row=8, column=1, sticky=W)

        lbl_total = Label(labelFrameleft, text="Total Cost", font=('arial', 12, "bold"), padx=2, pady=6)
        lbl_total.grid(row=9, column=0, sticky=W)
        entry_total = Entry(labelFrameleft, textvariable=self.var_total, font=('arial', 13, "bold"), width=20)
        entry_total.grid(row=9, column=1, sticky=W)

        # Buttons
        btnAdd = Button(labelFrameleft, text="Add", command=self.add_room, font=('arial', 11, 'bold'), bg='black',
                        fg='gold', width=9)
        btnAdd.grid(row=10, column=0, pady=10)

        btnUpdate = Button(labelFrameleft, text="Update", command=self.update_room, font=('arial', 11, 'bold'),
                           bg='black', fg='gold', width=9)
        btnUpdate.grid(row=10, column=1, pady=10)

        btnDelete = Button(labelFrameleft, text="Delete", command=self.delete_room, font=('arial', 11, 'bold'),
                           bg='black', fg='gold', width=9)
        btnDelete.grid(row=11, column=0, pady=10)

        btnBill = Button(labelFrameleft, text="Bill", command=self.calculate_total, font=('arial', 11, 'bold'),
                         bg='black', fg='gold', width=9)
        btnBill.grid(row=11, column=1, pady=10)
        # ---------------right side image---------------

        img3 = Image.open(r"images/room.jpeg ")
        img3 = img3.resize((520, 200), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=760, y=55, width=520, height=200)

        # Table Frame
        tableFrame = Frame(self.root, bd=2, relief=RIDGE)
        # tableFrame.place(x=435, y=50, width=860, height=490)

        tableFrame.place(x=435, y=280, width=860, height=260)

        lblSearchBy = Label(tableFrame, font=("arial", 12, "bold"), text="Search By:", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        self.search_var = ttk.Combobox(tableFrame, textvariable=self.search_var, font=("arial", 12, "bold"), width=24,
                                       state="readonly")
        self.search_var["value"] = ("contact", "roomtype")
        self.search_var.current(0)
        self.search_var.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        self.txtSearch = ttk.Entry(tableFrame, textvariable=self.txt_search, width=24, font=("arial", 13, "bold"))
        self.txtSearch.grid(row=0, column=2, padx=2)
        btnsearch = Button(tableFrame, text="Search",command=self.search_data, font=("arial", 11, "bold"), bg="black", fg="Gold", width=10)
        btnsearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(tableFrame, text="Show All",command=self.show_all_data, font=("arial", 11, "bold"), bg="black", fg="Gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        # -----------data table-------------

        details_table = Frame(tableFrame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)
        scrollx = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scrolly = ttk.Scrollbar(details_table, orient=VERTICAL)
        self.room_table = ttk.Treeview(details_table, columns=(
            "contact", "checkin", "checkout", "roomtype", "roomvaliable", "meal", "no of days")
                                       , xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.config(command=self.room_table.xview)
        scrolly.config(command=self.room_table.yview)
        self.room_table.heading("contact", text="contact")
        self.room_table.heading("checkin", text="checkin")
        self.room_table.heading("checkout", text="checkout")
        self.room_table.heading("roomtype", text="roomtype")
        self.room_table.heading("roomvaliable", text="roomvaliable")
        self.room_table.heading("meal", text="meal")
        self.room_table.heading("no of days", text="no of days")
        self.room_table["show"] = "headings"
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        self.room_table.column("contact", width=100)
        self.room_table.column("checkin", width=100)
        self.room_table.column("checkout", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomvaliable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("no of days", width=100)
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.create_room_table()  # Create the room table when the application starts
        self.fetch_data()

    def create_room_table(self):
        conn = sqlite3.connect("hotel.db")
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS room (
                contact INTEGER PRIMARY KEY,
                checkin TEXT,
                checkout TEXT,
                roomtype TEXT,
                roomavailable TEXT,
                meal TEXT,
                no_of_days INTEGER,
                paidtax REAL,
                actualtotal REAL,
                total REAL
            )
        """)
        conn.commit()
        conn.close()

    def add_room(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = sqlite3.connect("hotel.db")
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO room (contact, checkin, checkout, roomtype, roomavailable, meal, no_of_days, paidtax, actualtotal, total) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (
                        self.var_contact.get(),
                        self.var_checkin.get(),
                        self.var_checkout.get(),
                        self.var_roomtype.get(),
                        self.var_roomvaliable.get(),
                        self.var_meal.get(),
                        self.var_no_of_days.get(),
                        self.var__paidtax.get(),
                        self.var_actualtotal.get(),
                        self.var_total.get()
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room added successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}")
        self.root.focus_force()

    def fetch_data(self):
        conn = sqlite3.connect('hotel.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM room")
        rows = cur.fetchall()
        if len(rows) >= 0:
            self.room_table.delete(*self.room_table.get_children())
            for row in rows:
                self.room_table.insert('', END, values=row)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content['values']
        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomvaliable.set(row[4])
        self.var_meal.set(row[5])
        self.var_no_of_days.set(row[6])
        self.var__paidtax.set(row[7])
        self.var_actualtotal.set(row[8])
        self.var_total.set(row[9])

    def update_room(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please select a room to update")
        else:
            try:
                conn = sqlite3.connect("hotel.db")
                cur = conn.cursor()
                cur.execute(
                    "UPDATE room SET checkin=?, checkout=?, roomtype=?, roomavailable=?, meal=?, no_of_days=?, paidtax=?, actualtotal=?, total=? WHERE contact=?",
                    (
                        self.var_checkin.get(),
                        self.var_checkout.get(),
                        self.var_roomtype.get(),
                        self.var_roomvaliable.get(),
                        self.var_meal.get(),
                        self.var_no_of_days.get(),
                        self.var__paidtax.get(),
                        self.var_actualtotal.get(),
                        self.var_total.get(),
                        self.var_contact.get()
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room updated successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}")
        self.root.focus_force()

    def delete_room(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please select a room to delete")
        else:
            try:
                conn = sqlite3.connect("hotel.db")
                cur = conn.cursor()
                cur.execute("DELETE FROM room WHERE contact=?", (self.var_contact.get(),))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room deleted successfully")
            except sqlite3.Error as e:
                messagebox.showerror("Database Error", f"Error deleting room: {e}")
            except Exception as e:
                messagebox.showerror("Error", f"Unexpected error: {e}")
        self.root.focus_force()

    def calculate_total(self):
        try:
            days = int(self.var_no_of_days.get())
            subtotal = float(self.var_actualtotal.get())
            tax = float(self.var__paidtax.get())
            total = days * (subtotal + tax)
            self.var_total.set(total)
        except Exception as e:
            messagebox.showerror("Error", f"Error in calculating total: {str(e)}")
    def fetchbtn(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter your contact number!", parent=self.root)
        else:
            try:
                conn = sqlite3.connect('hotel.db')
                cur = conn.cursor()
                query = 'SELECT name, gender,email,nationality,address FROM customer WHERE mobile=?'
                value = (self.var_contact.get(),)
                cur.execute(query, value)
                row = cur.fetchone()

                if row is None:
                    messagebox.showerror("Error", "This Number Not Found!", parent=self.root)
                else:
                    showDataFrame = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                    showDataFrame.place(x=455, y=55, width=300, height=180)

                    lblname = Label(showDataFrame, text="Name: ", font=("arial", 12, "bold"))
                    lblname.place(x=0, y=0)
                    lblname_value = Label(showDataFrame, text=row[0], font=("arial", 12, "bold"))
                    lblname_value.place(x=90, y=0)

                    #------------gender-------------------------

                    lbl_gender = Label(showDataFrame, text="Gender: ", font=("arial", 12, "bold"))
                    lbl_gender.place(x=0, y=30)
                    lbl_gender_value = Label(showDataFrame, text=row[1], font=("arial", 12, "bold"))
                    lbl_gender_value.place(x=90, y=30)

                    lbl_gender = Label(showDataFrame, text="Email: ", font=("arial", 12, "bold"))
                    lbl_gender.place(x=0, y=60)
                    lbl_gender_value = Label(showDataFrame, text=row[2], font=("arial", 12, "bold"))
                    lbl_gender_value.place(x=90, y=60)

                    lbl_gender = Label(showDataFrame, text="Nationality: ", font=("arial", 12, "bold"))
                    lbl_gender.place(x=0, y=90)
                    lbl_gender_value = Label(showDataFrame, text=row[3], font=("arial", 12, "bold"))
                    lbl_gender_value.place(x=90, y=90)

                    lbl_gender = Label(showDataFrame, text="Address: ", font=("arial", 12, "bold"))
                    lbl_gender.place(x=0, y=120)
                    lbl_gender_value = Label(showDataFrame, text=row[4], font=("arial", 12, "bold"))
                    lbl_gender_value.place(x=90, y=120)

                conn.close()
            except sqlite3.Error as e:
                messagebox.showerror("Database Error", f"An error occurred: {e}", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"An unexpected error occurred: {e}", parent=self.root)

    def search_data(self):
        conn = sqlite3.connect('hotel.db')
        cur = conn.cursor()

        search_by = self.search_var.get()
        search_text = self.txt_search.get()

        if search_by and search_text:
            query = f"SELECT * FROM room WHERE {search_by} LIKE ?"
            cur.execute(query, ('%' + search_text + '%',))
            rows = cur.fetchall()

            if len(rows) == 0:
                # Clear table and show an error message
                self.room_table.delete(*self.room_table.get_children())
                messagebox.showerror("No Results", f"No records found for {search_by} '{search_text}'.")
            else:
                # Update table with results
                self.room_table.delete(*self.room_table.get_children())
                for row in rows:
                    self.room_table.insert('', END, values=row)
        else:
            messagebox.showwarning("Input Error", "Please enter search criteria.")


        conn.close()

    def show_all_data(self):
        conn = sqlite3.connect('hotel.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM room")
        rows = cur.fetchall()
        if rows:
            self.room_table.delete(*self.room_table.get_children())
            for row in rows:
                self.room_table.insert('', END, values=row)
        conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = RoomBooking(root)
    root.mainloop()
