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
        self.root.title("Loding Student Profile")
        self.root.geometry("1260x700+0+0")
        self.root.config(bg="black")

    #========Background Colour======== 
     
        self.bg=ImageTk.PhotoImage(file="b3.png")
        right_lbl=Label(self.root,image=self.bg)
        right_lbl.place(x=330,y=0,height=398,width=650)
    
    #==========Button Continue===================
        btn_cont=Button(self.root,text="Continue > > >",command=self.student_window,font=("times new roman",20,"bold"),bg="light blue",fg="black",bd=10).place(x=560,y=430,width=220)

#=============Defining student window function==================
    def student_window(self):
        self.root.destroy()
        import stud_mng



root=Tk()
obj=poo(root)
root.mainloop()