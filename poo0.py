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
        self.root.title("Loding Services")
        self.root.geometry("1260x700+0+0")
        self.root.config(bg="black")

    #========Background Colour======== 
     
        self.bg=ImageTk.PhotoImage(file="a1.jpg")
        right_lbl=Label(self.root,image=self.bg,bg="orange")
        right_lbl.place(x=270,y=10,height=370,width=750)

    #==========Button Continue===================
        btn_cont=Button(self.root,text="Continue > > >",command=self.poo0_window,font=("times new roman",20,"bold"),bg="light blue",fg="black",bd=10).place(x=560,y=430,width=220)

#=============Defining poo0 window function==================
    def poo0_window(self):
        self.root.destroy()
        import win3



root=Tk()
obj=poo(root)
root.mainloop()