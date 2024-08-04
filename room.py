from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class RoomBooking():
    def __init__(self, root):
        self.root = root
        self.root.geometry('1295x550+230+220')
        self.root.title('Room Booking')

        #------------variables-------
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomvaliable=StringVar()
        self.var_meal=StringVar()
        self.var_no_of_days=StringVar()
        self.var__paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()



        #------------title--------------------

        lbl1_title = Label(self.root, text='ROOMBOOKING DETAILS', font=('times new roman', 18,"bold"), bg='black', fg='gold')
        lbl1_title.place(x=0, y=0,width=1295, height=50)

        #--------------logo-------------------

        img2 = Image.open(r"images/grandHotel.jpg ")
        img2= img2.resize((100, 40), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        #---------------label frame--------------

        labelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='roombooking Details',
                                  font=('arial', 12,"bold")
                                  ,padx=2,pady=2)
        labelFrameleft.place(x=5, y=50,width=425, height=490)
       #------------labels and entries----------
       #customer contact
        lbl1_contact = Label(labelFrameleft,text="Customer Contact",font=('arial', 12,"bold"),padx=2,pady=6)
        lbl1_contact.grid(row=0,column=0,sticky=W)
        entry_contact=ttk.Entry(labelFrameleft,font=('arial', 13,"bold"),textvariable=self.var_contact,width=20)
        entry_contact.grid(row=0,column=1,sticky=W)
        #-------------fetch Data Button---------------
        btnAdd=Button(labelFrameleft,text="Fetch Data",command=self.fetchbtn,font=("Arial",8,"bold"),bg='black',fg='gold',width=8,height=1)
        btnAdd.place(x=340,y=4)

        #check_in_Date
        check_in_date = Label(labelFrameleft, text="Check_in Date", font=('arial', 12, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)
        check_in_date = ttk.Entry(labelFrameleft, font=('arial', 13, "bold"),textvariable=self.var_checkin, width=29)
        check_in_date.grid(row=1, column=1)

        #check_out_Date
        check_out_date = Label(labelFrameleft, text="Check_out Date", font=('arial', 12, "bold"), padx=2, pady=6)
        check_out_date.grid(row=2, column=0, sticky=W)
        check_out_date = ttk.Entry(labelFrameleft, font=('arial', 13, "bold"),textvariable=self.var_checkin, width=29)
        check_out_date.grid(row=2, column=1)

        #Room_Type
        roomType = Label(labelFrameleft, text="Room Type", font=('arial', 12, "bold"), padx=2, pady=6)
        roomType.grid(row=3, column=0, sticky=W)
        combo_roomType = ttk.Combobox(labelFrameleft, font=('arial', 13, "bold"),textvariable=self.var_roomtype, width=27)
        combo_roomType["value"]=("Single","Double","Laxary")
        combo_roomType.grid(row=3, column=1)

        #Available_Room
        Available_Room = Label(labelFrameleft, text="Available_Room", font=('arial', 12, "bold"), padx=2, pady=6)
        Available_Room.grid(row=4, column=0, sticky=W)
        Available_Room = ttk.Entry(labelFrameleft, font=('arial', 13, "bold"),textvariable=self.var_roomvaliable, width=29)
        Available_Room.grid(row=4, column=1)

        #Meal
        Meal = Label(labelFrameleft, text="meal", font=('arial', 12, "bold"), padx=2, pady=6)
        Meal.grid(row=5, column=0, sticky=W)
        Meal = ttk.Entry(labelFrameleft, font=('arial', 13, "bold"),textvariable=self.var_meal, width=29)
        Meal.grid(row=5, column=1)

        #No of Days
        Days = Label(labelFrameleft, text="No Of Days", font=('arial', 12, "bold"), padx=2, pady=6)
        Days.grid(row=6, column=0, sticky=W)
        Days = ttk.Entry(labelFrameleft, font=('arial', 13, "bold"), width=29,textvariable=self.var_no_of_days)
        Days.grid(row=6, column=1)

        #Paid_Tax
        Paid_Tax = Label(labelFrameleft, text="Paid Tax", font=('arial', 12, "bold"), padx=2, pady=6)
        Paid_Tax.grid(row=7, column=0, sticky=W)
        Paid_Tax = ttk.Entry(labelFrameleft, font=('arial', 13, "bold"),textvariable=self.var__paidtax, width=29)
        Paid_Tax.grid(row=7, column=1)

        #sub_total
        sub_total = Label(labelFrameleft, text="Sub Total", font=('arial', 12, "bold"), padx=2, pady=6)
        sub_total.grid(row=8, column=0, sticky=W)
        sub_total = ttk.Entry(labelFrameleft, font=('arial', 13, "bold"),textvariable=self.var_actualtotal, width=29)
        sub_total.grid(row=8, column=1)

        #Total_Cost
        Total_Cost = Label(labelFrameleft, text="Total Cost", font=('arial', 12, "bold"), padx=2, pady=6)
        Total_Cost.grid(row=9, column=0, sticky=W)
        Total_Cost = ttk.Entry(labelFrameleft, font=('arial', 13, "bold"),textvariable=self.var_total, width=29)
        Total_Cost.grid(row=9, column=1)

        #-----------------Bill Button------------------
        bill_btn = Button(labelFrameleft, text="Bill", font=("Arial", 11, "bold"), bg='black', fg='gold', width=10)
        bill_btn.grid(row=10, column=0, padx=1,sticky=W)

        #------------------btns--------------
        btn_frame=Frame(labelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btn_Add = Button(btn_frame, text="Add", font=("Arial", 11, "bold"), bg='black', fg='gold', width=10)
        btn_Add.grid(row=0, column=0, padx=1)

        btn_delete = Button(btn_frame,text="Delete",font=("Arial", 11, "bold"),bg='black',fg='gold',width= 10 )
        btn_delete.grid(row=0, column=1,padx=1)

        btn_update = Button(btn_frame, text="Update", font=("Arial", 11, "bold"), bg='black', fg='gold', width=10)
        btn_update.grid(row=0, column=2, padx=1)

        btn_reset = Button(btn_frame, text="Reset", font=("Arial", 11, "bold"), bg='black', fg='gold', width=10)
        btn_reset.grid(row=0, column=3, padx=1)

        #---------------right side image---------------

        img3 = Image.open(r"images/room.jpeg ")
        img3 = img3.resize((520, 200), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=760, y=55, width=520, height=200)

        #-----------tabel frame search system----------------
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System"
                               ,font=('arial', 12, "bold"))
        Table_frame.place(x=435, y=280, width=860, height=260)
        lbl_search=Label(Table_frame,font=("arial", 12, "bold"),text="Search By: ",bg="red",fg="white")
        lbl_search.grid(row=0, column=0, padx=2,sticky=W)
        self.serch_var=StringVar()
        combo_serach=ttk.Combobox(Table_frame,textvariable=self.serch_var,font=("arial", 12, "bold")
                                  ,state="readonly",width=24)
        combo_serach["value"]=("contact","Room")
        combo_serach.current(0)
        combo_serach.grid(row=0, column=1, padx=2)
        self.txt_search=StringVar()
        txtSerch=Entry(Table_frame,textvariable=self.txt_search,font=("arial", 13, "bold"),width=24)
        txtSerch.grid(row=0, column=2, padx=2)

        btnsearch=Button(Table_frame,text="Search",font=("arial",11,"bold"),bg="black",fg="Gold",width=10)
        btnsearch.grid(row=0, column=3, padx=1)

        btnShowAll=Button(Table_frame,text="Show All",font=("arial",11,"bold"),bg="black",fg="Gold",width=10)
        btnShowAll.grid(row=0, column=4, padx=1)
        #--------------------show Data Table-------------------------------
        details_table=Frame(Table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)

        scrollx=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(details_table,orient=VERTICAL)
        self.room_table=ttk.Treeview(details_table,columns=("contact","checkin","checkout","roomtype","roomvaliable","meal","no of days")
                                     ,xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.config(command=self.room_table.xview)
        scrolly.config(command=self.room_table.yview)
        self.room_table.heading("contact",text="contact")
        self.room_table.heading("checkin",text="checkin")
        self.room_table.heading("checkout",text="checkout")
        self.room_table.heading("roomtype",text="roomtype")
        self.room_table.heading("roomvaliable",text="roomvaliable")
        self.room_table.heading("meal",text="meal")
        self.room_table.heading("no of days",text="no of days")
        self.room_table["show"]="headings"
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomvaliable", width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("no of days",width=100)
        self.room_table.pack(fill=BOTH, expand=1)

    def fetchbtn(self):
        if self.var_contact.get() =="":
            messagebox.showerror("Error","Please enter your contact details",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",passwd="test@123",database="management")
            mycursor=conn.cursor()
            query=("")

if __name__ == '__main__':
    root = Tk()
    obj = RoomBooking(root)
    root.mainloop()