#==========Importing Library===========

#pip install tkinter
from tkinter import*

#pip install pillow
from PIL import Image,ImageTk,ImageDraw 

#import ttk from tkinter
from tkinter import ttk

#=========Defining Class================
class poo:

    #=======Default Constructor========
    def __init__(self,root):
        self.root=root
        self.root.title("Loding Fees Detail")
        self.root.geometry("1260x700+0+0")
        self.root.config(bg="black")

    #========Background Colour======== 
     
        self.bg=ImageTk.PhotoImage(file="payment.jpg")
        right_lbl=Label(self.root,image=self.bg)
        right_lbl.place(x=300,y=50,height=400,width=650)

    #===========Continue Button===================
        btn_cont=Button(self.root,text="Continue > > >",command=self.fee_window,font=("times new roman",20,"bold"),bg="#93C572",fg="black",bd=10).place(x=530,y=510,width=220)

#============Defining Course window function=====================
    def fee_window(self):
        self.root.destroy()
        import fees

root=Tk()
obj=poo(root)
root.mainloop()