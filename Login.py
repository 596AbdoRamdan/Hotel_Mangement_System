from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#----------pip install pillow----------
import PIL
from PIL import Image, ImageTk

class Login_Window:
    def __init__(self,root):
        # Screen Create with name and resolution
        self.root = root
        self.root.title('Login')
        self.root.geometry('1550x800+0+0')


        #----------Background Image Upload----------
        # self.bg = ImageTk.PhotoImage(file="")
        # lbl_bg = Label(self.root,image=self.bg)
        # lbl.bg.place(x=0, y=0, relwidth=1, relheight=1)


        #----------Background Color Upload----------
        bg = Label(self.root,bg='light blue',width=1550,height=800)
        bg.place(x=0, y=0)



        #----------Window of Login create----------
        frame = Frame(self.root, bg='grey')
        frame.place(x=610, y=170, width=340, height=450)


        #----------Icon of The Middle of the Frame Upload----------
        img1 = Image.open(r"D:\My_Pics\Picsart_23-03-07_19-46-32-490.jpg")
        img1 = img1.resize((100,100),PIL.Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1,bg='black',borderwidth=0)
        lblimg1.place(x=730, y=175,width=100, height=100)

        #----------Label of The Icon Creation----------
        get_str = Label(frame,text='Get Started',font=("times new roman",20,'bold'),bg='grey',fg='white')
        get_str.place(x=95, y=100)

        #----------Username Label & Entry Creation----------
        username = lbl = Label(frame,text="Username",font=("times new roman",20,'bold'),bg='grey',fg='white')
        username.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame,font=("times new roman",20,'bold'))
        self.txtuser.place(x=40, y=200,width=270)



        #----------Password Label & Entry Creation----------
        password = lbl = Label(frame, text="Password", font=("times new roman", 20, 'bold'), bg='grey', fg='white')
        password.place(x=70, y=240)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 20, 'bold'))
        self.txtpass.place(x=40, y=280, width=270)


        #----------Icon Images----------
        # img2 = Image.open(r"D:\My_Pics\Picsart_23-03-07_19-46-32-490.jpg")
        # img2 = img2.resize((25, 25), PIL.Image.Resampling.LANCZOS)
        # self.photoimage2 = ImageTk.PhotoImage(img2)
        # lblimg1 = Label(image=self.photoimage2, bg='black', borderwidth=0)
        # lblimg1.place(x=610, y=323, width=25, height=25)



if __name__ == '__main__':
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
