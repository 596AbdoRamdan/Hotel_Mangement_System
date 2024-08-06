from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk
import sqlite3
from tkinter import messagebox


class Cust_Win:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")
        icon = PhotoImage(file=r"images/hotel.png")
        root.iconphoto(False, icon)
        root.resizable(False, False)

        # ---------------------title--------------------
        lbl_title = Label(self.root, text="CUSTOMER DETAILS ", font=("times new roman", 18, "bold"), bg="black", fg="Gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ---------------------labelframe--------------
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=("arial", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # --------------------labels and entrys--------

        # custref
        lbl_cust_ref = Label(labelframeleft, text="Customer ref", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)
        self.enty_ref = ttk.Entry(labelframeleft, width=29, font=("arial", 13, "bold"))
        self.enty_ref.grid(row=0, column=1)

        # customer name
        cname = Label(labelframeleft, font=("arial", 12, "bold"), text="Customer Name:", padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)
        self.txtcname = ttk.Entry(labelframeleft, width=29, font=("arial", 13, "bold"))
        self.txtcname.grid(row=1, column=1)

        # gender combobox
        label_gender = Label(labelframeleft, font=("arial", 12, "bold"), text="Gender:", padx=2, pady=6)
        label_gender.grid(row=2, column=0, sticky=W)
        self.combo_gender = ttk.Combobox(labelframeleft, font=("arial", 12, "bold"), width=27, state="readonly")
        self.combo_gender["value"] = ("Male", "Female")
        self.combo_gender.grid(row=2, column=1)

        # post code
        lblPostCode = Label(labelframeleft, font=("arial", 12, "bold"), text="PostCode:", padx=2, pady=6)
        lblPostCode.grid(row=3, column=0, sticky=W)
        self.txtPostCode = ttk.Entry(labelframeleft, width=29, font=("arial", 13, "bold"))
        self.txtPostCode.grid(row=3, column=1)

        # mobile number
        lblMobile = Label(labelframeleft, font=("arial", 12, "bold"), text="Mobile:", padx=2, pady=6)
        lblMobile.grid(row=4, column=0, sticky=W)
        self.txtMobile = ttk.Entry(labelframeleft, width=29, font=("arial", 13, "bold"))
        self.txtMobile.grid(row=4, column=1)

        # email
        lblEmail = Label(labelframeleft, font=("arial", 12, "bold"), text="Email:", padx=2, pady=6)
        lblEmail.grid(row=5, column=0, sticky=W)
        self.txtEmail = ttk.Entry(labelframeleft, width=29, font=("arial", 13, "bold"))
        self.txtEmail.grid(row=5, column=1)

        # nationality
        lblNationality = Label(labelframeleft, font=("arial", 12, "bold"), text="Nationality:", padx=2, pady=6)
        lblNationality.grid(row=6, column=0, sticky=W)
        self.txtNationality = ttk.Combobox(labelframeleft, font=("arial", 12, "bold"), width=27,state="readonly")
        self.txtNationality["value"] = ("Egyptian","American", "British", "Canadian", "Australian", "Indian","other")

        self.txtNationality.grid(row=6, column=1)

        # id number
        lblIdNumber = Label(labelframeleft, font=("arial", 12, "bold"), text="Id Number:", padx=2, pady=6)
        lblIdNumber.grid(row=7, column=0, sticky=W)
        self.txtIdNumber = ttk.Entry(labelframeleft, width=29, font=("arial", 13, "bold"))
        self.txtIdNumber.grid(row=7, column=1)

        # address
        lblAddress = Label(labelframeleft, font=("arial", 12, "bold"), text="Address:", padx=2, pady=6)
        lblAddress.grid(row=8, column=0, sticky=W)
        self.txtAddress = ttk.Entry(labelframeleft, width=29, font=("arial", 13, "bold"))
        self.txtAddress.grid(row=8, column=1)

        # ---------------------buttons-----------------
        btn_frame = Frame(labelframeleft)
        btn_frame.place(x=20, y=400, width=400, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", command=self.update_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.delete_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.reset_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=9)
        btnReset.grid(row=0, column=3, padx=1)

        # -------------------table frame----------------
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", font=("arial", 12, "bold"), padx=2)
        Table_Frame.place(x=435, y=50, width=860, height=490)

        lblSearchBy = Label(Table_Frame, font=("arial", 12, "bold"), text="Search By:", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        self.search_var = ttk.Combobox(Table_Frame,textvariable=self.search_var, font=("arial", 12, "bold"), width=24, state="readonly")
        self.search_var["value"] = ("Mobile", "Ref")
        self.search_var.current(0)
        self.search_var.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        self.txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_search, width=24, font=("arial", 13, "bold"))
        self.txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search", command=self.search_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=9)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Show All", command=self.fetch_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=9)
        btnShowAll.grid(row=0, column=4, padx=1)

        # ----------------------data table----------------------
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table, columns=("ref", "name", "gender", "post", "mobile", "email", "nationality", "idnumber", "address")
                                               , xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref", text="Refer No")
        self.Cust_Details_Table.heading("name", text="Name")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("post", text="PostCode")
        self.Cust_Details_Table.heading("mobile", text="Mobile")
        self.Cust_Details_Table.heading("email", text="Email")
        self.Cust_Details_Table.heading("nationality", text="Nationality")
        self.Cust_Details_Table.heading("idnumber", text="Id Number")
        self.Cust_Details_Table.heading("address", text="Address")

        self.Cust_Details_Table["show"] = "headings"

        self.Cust_Details_Table.column("ref", width=100)
        self.Cust_Details_Table.column("name", width=100)
        self.Cust_Details_Table.column("gender", width=100)
        self.Cust_Details_Table.column("post", width=100)
        self.Cust_Details_Table.column("mobile", width=100)
        self.Cust_Details_Table.column("email", width=150)
        self.Cust_Details_Table.column("nationality", width=100)
        self.Cust_Details_Table.column("idnumber", width=100)
        self.Cust_Details_Table.column("address", width=100)

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

        self.create_table()

    def create_table(self):
        conn = sqlite3.connect('hotel.db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS customer (
                        ref INTEGER ,
                        name TEXT,
                        gender TEXT,
                        post TEXT,
                        mobile TEXT,
                        email TEXT,
                        nationality TEXT,
                        idnumber Integer,
                        address TEXT)''')
        conn.commit()
        conn.close()

    import sqlite3
    from tkinter import messagebox

    def add_data(self):
        if (self.enty_ref.get() == "" or self.txtcname.get() == "" or self.combo_gender.get() == "" or
                self.txtPostCode.get() == "" or self.txtMobile.get() == "" or self.txtEmail.get() == "" or
                self.txtNationality.get() == "" or self.txtIdNumber.get() == "" or self.txtAddress.get() == ""):
            messagebox.showerror("Error", "All fields are required")
        elif not (
                self.enty_ref.get().isdigit() and self.txtIdNumber.get().isdigit()):
            messagebox.showerror("Error", "Reference, Post Code, and ID Number must be integers")
        else:
            try:
                conn = sqlite3.connect('hotel.db')
                cur = conn.cursor()
                cur.execute("INSERT INTO customer VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                    self.enty_ref.get(),
                    self.txtcname.get(),
                    self.combo_gender.get(),
                    self.txtPostCode.get(),
                    self.txtMobile.get(),
                    self.txtEmail.get(),
                    self.txtNationality.get(),
                    self.txtIdNumber.get(),
                    self.txtAddress.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer has been added")
                self.reset_data()

            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Database error: {str(e)}")
        self.root.focus_force()

    def fetch_data(self):
        conn = sqlite3.connect('hotel.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM customer")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for row in rows:
                self.Cust_Details_Table.insert('', END, values=row)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content['values']

        if row:
            self.enty_ref.delete(0, END)
            self.enty_ref.insert(END, row[0])
            self.txtcname.delete(0, END)
            self.txtcname.insert(END, row[1])
            self.combo_gender.set(row[2])
            self.txtPostCode.delete(0, END)
            self.txtPostCode.insert(END, row[3])
            self.txtMobile.delete(0, END)
            self.txtMobile.insert(END, row[4])
            self.txtEmail.delete(0, END)
            self.txtEmail.insert(END, row[5])
            # self.txtNationality.delete(0, END)
            # self.txtNationality.insert(END, row[6])
            self.txtNationality.set(row[6])
            self.txtIdNumber.delete(0, END)
            self.txtIdNumber.insert(END, row[7])
            self.txtAddress.delete(0, END)
            self.txtAddress.insert(END, row[8])

    def update_data(self):
        if self.enty_ref.get() == "":
            messagebox.showerror("Error", "Please select a record to update")
        else:
            conn = sqlite3.connect('hotel.db')
            cur = conn.cursor()
            cur.execute("UPDATE customer SET name=?, gender=?, post=?, mobile=?, email=?, nationality=?, idnumber=?, address=? WHERE ref=?", (
                self.txtcname.get(),
                self.combo_gender.get(),
                self.txtPostCode.get(),
                self.txtMobile.get(),
                self.txtEmail.get(),
                self.txtNationality.get(),
                self.txtIdNumber.get(),
                self.txtAddress.get(),
                self.enty_ref.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Customer has been updated")
            self.reset_data()
        self.root.focus_force()

    def delete_data(self):
        conn = sqlite3.connect('hotel.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM customer WHERE ref=?", (self.enty_ref.get(),))
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Success", "Customer has been deleted")
        self.reset_data()
        self.root.focus_force()


    def reset_data(self):
        self.enty_ref.delete(0, END)
        self.txtcname.delete(0, END)
        self.combo_gender.set("")
        self.txtPostCode.delete(0, END)
        self.txtMobile.delete(0, END)
        self.txtEmail.delete(0, END)
        self.txtNationality.set("")
        self.txtIdNumber.delete(0, END)
        self.txtAddress.delete(0, END)
        self.root.focus_force()



    def search_data(self):
        conn = sqlite3.connect('hotel.db')
        cur = conn.cursor()

        search_by = self.search_var.get()
        search_text = self.txt_search.get()

        if search_by and search_text:
            query = f"SELECT * FROM customer WHERE {search_by} LIKE ?"
            cur.execute(query, ('%' + search_text + '%',))
            rows = cur.fetchall()
            if len(rows) == 0:
                # Clear table and show an error message
                 self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                 messagebox.showerror("No Results", f"No records found for {search_by} '{search_text}'.")
            else:
                # Update table with results
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                for row in rows:
                    self.Cust_Details_Table.insert('', END, values=row)
        else:
                messagebox.showwarning("Input Error", "Please enter search criteria.")

        conn.close()


if __name__ == '__main__':
    root = Tk()
    obj = Cust_Win(root)
    icon = PhotoImage(file=r"images/hotel.png")
    root.iconphoto(False, icon)
    root.mainloop()
