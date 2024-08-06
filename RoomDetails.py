import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox


class DetailsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry('1295x550+230+220')
        icon = PhotoImage(file=r"images/hotel.png")
        root.iconphoto(False, icon)
        root.resizable(False, False)

        # Database connection
        self.conn = sqlite3.connect('hotel.db')
        self.cursor = self.conn.cursor()
        self.create_table()

        # Title
        lbl_title = Label(self.root, text="ROOM DETAILS", font=("times new roman", 18, "bold"), fg="yellow", bg="black")
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # Logo
        img2 = Image.open(r"images/grandHotel.jpg")
        img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbling = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lbling.place(x=5, y=2, width=100, height=40)

        # Labelframe
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add", font=("Arial", 18, "bold"),
                                    padx=2, pady=6)
        labelframeleft.place(x=5, y=50, width=540, height=350)

        # Floor
        lbl_floor = Label(labelframeleft, text="Floor", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W, padx=20)

        self.entry_floor = ttk.Combobox(labelframeleft, font=("Arial", 13, "bold"), width=18,state="readonly")
        self.entry_floor["value"] = ("1", "2", "3", "4", "5")
        self.entry_floor.grid(row=0, column=1, sticky=W)

        # Room num
        lbl_RoomNo = Label(labelframeleft, text="Room No", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_RoomNo.grid(row=1, column=0, sticky=W, padx=20)

        self.entry_RoomNo = ttk.Entry(labelframeleft, font=("Arial", 13, "bold"), width=20)
        self.entry_RoomNo.grid(row=1, column=1, sticky=W)

        # Room type
        lbl_Roomtype = Label(labelframeleft, text="Room type", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_Roomtype.grid(row=2, column=0, sticky=W, padx=20)

        self.entry_Roomtype = ttk.Combobox(labelframeleft, font=("Arial", 13, "bold"), width=18, state="readonly")
        self.entry_Roomtype["value"] = ("Single","Double","Doublex")
        self.entry_Roomtype.grid(row=2, column=1, sticky=W)

        # Button frame
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", font=("Arial", 11, "bold"), bg="black", fg="gold", width=10,
                        command=self.add_data)
        btnAdd.grid(row=0, column=0, padx=1)

        btn_update = Button(btn_frame, text="Update", font=("Arial", 11, "bold"), bg="black", fg="gold", width=10,
                            command=self.update_data)
        btn_update.grid(row=0, column=1, padx=1)

        btn_Delete = Button(btn_frame, text="Delete", font=("Arial", 11, "bold"), bg="black", fg="gold", width=10,
                            command=self.delete_data)
        btn_Delete.grid(row=0, column=2, padx=1)

        btn_Reset = Button(btn_frame, text="Reset", font=("Arial", 11, "bold"), bg="black", fg="gold", width=10,
                           command=self.reset_fields)
        btn_Reset.grid(row=0, column=3, padx=1)

        # Table frame
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details", font=("arial", 12, "bold"),
                                 padx=2)
        Table_Frame.place(x=600, y=55, width=600, height=350)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.room_table = ttk.Treeview(Table_Frame, column=("floor", "roomno", "roomtype"), xscrollcommand=scroll_x.set,
                                       yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomno", text="Room No")
        self.room_table.heading("roomtype", text="Room Type")

        self.room_table["show"] = "headings"

        self.room_table.column("floor", width=100)
        self.room_table.column("roomno", width=100)
        self.room_table.column("roomtype", width=100)

        self.room_table.pack(fill=BOTH, expand=1)

        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS room_details (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                floor TEXT NOT NULL,
                roomno TEXT NOT NULL UNIQUE,
                roomtype TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def add_data(self):
        floor = self.entry_floor.get()
        roomno = self.entry_RoomNo.get()
        roomtype = self.entry_Roomtype.get()

        if floor == "" or roomno == "" or roomtype == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                self.cursor.execute("INSERT INTO room_details (floor, roomno, roomtype) VALUES (?, ?, ?)",
                                    (floor, roomno, roomtype))
                self.conn.commit()
                self.fetch_data()
                messagebox.showinfo("Success", "Room added successfully")
                self.reset_fields()
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Room number already exists")
        self.root.focus_force()

    def fetch_data(self):
        self.cursor.execute("SELECT * FROM room_details")
        rows = self.cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for row in rows:
                self.room_table.insert("", END, values=(row[1], row[2], row[3]))
            self.conn.commit()

    def reset_fields(self):
        self.entry_floor.set("")
        self.entry_RoomNo.delete(0, END)
        self.entry_Roomtype.set("")
        self.root.focus_force()

    def get_cursor(self, event):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content['values']
        self.entry_floor.set(row[0])
        self.entry_RoomNo.delete(0, END)
        self.entry_RoomNo.insert(END, row[1])
        self.entry_Roomtype.set(row[2])

    def delete_data(self):
        try:
            selected_item = self.room_table.selection()[0]
            values = self.room_table.item(selected_item, 'values')
            roomno = values[1]

            conn = sqlite3.connect("hotel.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM room_details WHERE roomno = ?", (roomno,))
            conn.commit()
            conn.close()

            # Force UI refresh or repopulate table
            self.room_table.delete(*self.room_table.get_children())
            self.fetch_data()
            self.reset_fields()

            messagebox.showinfo("Success", "Room deleted successfully")
        except IndexError:
            messagebox.showerror("Error", "Please select a room to delete")
        self.root.focus_force()

    def update_data(self):
        floor = self.entry_floor.get()
        roomno = self.entry_RoomNo.get()
        roomtype = self.entry_Roomtype.get()

        if floor == "" or roomno == "" or roomtype == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                selected_item = self.room_table.selection()[0]
                old_values = self.room_table.item(selected_item, 'values')
                old_roomno = old_values[1]

                self.cursor.execute("""
                    UPDATE room_details SET floor = ?, roomno = ?, roomtype = ?
                    WHERE roomno = ?
                """, (floor, roomno, roomtype, old_roomno))
                self.conn.commit()
                self.fetch_data()
                messagebox.showinfo("Success", "Room updated successfully")
                self.reset_fields()
            except IndexError:
                messagebox.showerror("Error", "Please select a room to update")
        self.root.focus_force()


if __name__ == "__main__":
    root = Tk()
    obj = DetailsRoom(root)
    root.mainloop()
