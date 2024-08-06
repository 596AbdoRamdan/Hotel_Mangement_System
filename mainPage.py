from tkinter import *
from PIL import Image, ImageTk
from RoomBookin import RoomBooking
from RoomDetails import DetailsRoom
from customer import Cust_Win

class HotelMangementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Mangement System")
        self.root.geometry("1550x800+0+0")
        root.resizable(False, False)
        # ---------------1st image------------------
        img1 = Image.open(r"images/reception.jpg")
        img1 = img1.resize((1550,140),Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        #----------------------logo-------------------

        img2 = Image.open(r"images/grandHotel.jpg ")
        img2 = img2.resize((230, 140),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)

        #---------------------title--------------------

        lbl_title= Label(self.root,text="Hotel Management System ", font=("times new roman",40,"bold"),bg="black",fg="Gold",bd=4
                         ,relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        # -----------------main_frame------------------

        main_frame = Frame(self.root,bg="black",bd=4,relief=RIDGE,background="Black")
        main_frame.place(x=0,y=190,width=1550,height=620)


        #----------------------menu--------------------
        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black",
                          fg="Gold", bd=4,padx=40
                          , relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=240)
        # ----------------------btn_frame--------------------
        btn_frame = Label(main_frame,bg="black", bd=4 , relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER", font=("times new roman",14,"bold"),command=self.customer,bg="black",fg="Gold",width=22,cursor="hand2"
                        ,activebackground="black",activeforeground="Gold",relief=RIDGE)
        cust_btn.grid(row=0,column=0,pady=1)

        det_btn = Button(btn_frame,activeforeground="Gold", text="DETAILS", font=("times new roman", 14, "bold"), bg="black", fg="Gold",
                          width=22, cursor="hand2",activebackground="black",command=self.roombooking)
        det_btn.grid(row=1, column=0, pady=1)

        rom_btn = Button(btn_frame, text="ROOMS",activeforeground="Gold", font=("times new roman", 14, "bold"),activebackground="black", bg="black", fg="Gold",
                          width=22, cursor="hand2"
                         ,command=self.roomDetails)
        rom_btn.grid(row=2, column=0, pady=1)

        logout_btn = Button(btn_frame,command=self.logout, text="LOGOUT",activeforeground="Gold",activebackground="black", font=("times new roman", 14, "bold"), bg="black", fg="Gold",
                          width=22, cursor="hand2")
        logout_btn.grid(row=3, column=0, pady=1)
        #---------------------right side image------------------------------------
        img3 = Image.open(r"images/mmm.jpg")
        img3 = img3.resize((1310, 590), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1310, height=590)

        #----------------------down images---------------------------------------------

        img4 = Image.open(r"images/Slide-2.jpg")
        img4 = img4.resize((230, 250), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lblimg2 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=225, width=230, height=250)

        img5 = Image.open(r"images/swimming.jpg")
        img5 = img5.resize((230, 190), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lblimg3 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg3.place(x=0, y=420, width=230, height=190)

    #----------button Functions---------------------
    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = RoomBooking(self.new_window)
    def roomDetails(self):
        self.new_window = Toplevel(self.root)
        self.app2 = DetailsRoom(self.new_window)

    def customer(self):
        self.new_window = Toplevel(self.root)
        self.app3 = Cust_Win(self.new_window)

    def logout(self):
        self.root.destroy()



if __name__ == "__main__":
    root = Tk()
    obj = HotelMangementSystem(root)

    icon = PhotoImage(file=r"images/hotel.png")
    root.iconphoto(True, icon)
    root.mainloop()