from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox

class details_room:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Mangement System")
        self.root.geometry('1295x550+230+220')

    #------------------title---------------
        lbl_title=Label(self.root,text="RoomBooking Details",font=("times new roman",18,"bold"),fg="yellow",bg="black")
        lbl_title.place(x=0,y=0,width=1295,height=50)

    #------------------logo-----------------
        img2=Image.open(r"images/grandHotel.jpg")
        img2=img2.resize((100,40),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling =Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbling.place(x=5,y=2,width=100,height=40)

    #------------------labelframe-----------
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("Arial",18,"bold"),padx=2,pady=6)
        labelframeleft.place(x=5,y=50,width=540,height=350)
    #Floor
        lbl_floor=Label(labelframeleft,text="Floor",font=("Arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W,padx=20)

        entry_floor=ttk.Entry(labelframeleft,font=("Arial",13,"bold"),width=20)
        entry_floor.grid(row=0,column=1,sticky=W)
    #Room num
        lbl_RoomNo = Label(labelframeleft, text="Room No", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_RoomNo.grid(row=1, column=0, sticky=W, padx=20)

        entry_RoomNo = ttk.Entry(labelframeleft, font=("Arial", 13, "bold"), width=20)
        entry_RoomNo.grid(row=1, column=1, sticky=W)
    # Room type
        lbl_Roomtype = Label(labelframeleft, text="Room type", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_Roomtype.grid(row=2, column=0, sticky=W, padx=20)

        entry_Roomtype = ttk.Entry(labelframeleft, font=("Arial", 13, "bold"), width=20)
        entry_Roomtype.grid(row=2, column=1, sticky=W)
    #buttom

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btnAdd=Button(btn_frame, text="Add",font=("Arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btn_update = Button(btn_frame, text="Update", font=("Arial", 11, "bold"), bg="black", fg="gold", width=10)
        btn_update.grid(row=0, column=1, padx=1)

        btn_Delete = Button(btn_frame, text="Delete", font=("Arial", 11, "bold"), bg="black", fg="gold", width=10)
        btn_Delete.grid(row=0, column=2, padx=1)

        btn_Reset = Button(btn_frame, text="Reset", font=("Arial", 11, "bold"), bg="black", fg="gold", width=10)
        btn_Reset.grid(row=0, column=3, padx=1)
    #------------------table frame-----------------
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="show Room Details",font=("arial",12,"bold"),padx=2)
        Table_Frame.place(x=600,y=55,width=600,height=350)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.room_table=ttk.Treeview(Table_Frame,column=("floor","roomno","roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomno", text="Room No")
        self.room_table.heading("roomtype", text="Room Type")

        self.room_table["show"]="headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomtype",width=100)

        self.room_table.pack(fill=BOTH,expand=1)


if __name__=="__main__":
    root=Tk()
    obj=details_room(root)
    root.mainloop()