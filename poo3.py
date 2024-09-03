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
        self.root.title("Loding Course Detail")
        self.root.geometry("1260x700+0+0")
        self.root.config(bg="black")

    #========Background Colour======== 
     
        self.bg=ImageTk.PhotoImage(file="b2.png")
        right_lbl=Label(self.root,image=self.bg)
        right_lbl.place(x=310,y=70,height=498,width=464)

    #===========Continue Button===================
        btn_cont=Button(self.root,text="Continue > > >",command=self.course_window,font=("times new roman",20,"bold"),bg="light blue",fg="black",bd=10).place(x=860,y=290,width=220)

#============Defining Course window function=====================
    def course_window(self):
        self.root.destroy()
        import Course

root=Tk()
obj=poo(root)
root.mainloop()