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
        self.root.title("Loding Teacher Profile")
        self.root.geometry("1260x700+0+0")
        self.root.config(bg="black")

    #========Background Colour======== 
     
        self.bg=ImageTk.PhotoImage(file="b5.png")
        right_lbl=Label(self.root,image=self.bg)
        right_lbl.place(x=210,y=70,height=500,width=500)
    #==========Button Continue=================
        btn_cont=Button(self.root,text="Continue > > >",command=self.teacher_window,font=("times new roman",20,"bold"),bg="pink",fg="black",bd=10).place(x=800,y=260,width=220)

#===============Defining teacher window function===================
    def teacher_window(self):
        self.root.destroy()
        import Teac_mng

root=Tk()
obj=poo(root)
root.mainloop()