#=========Importing Libraries============

#pip install tkinter
from tkinter import*

#pip install pillow
from PIL import Image,ImageTk,ImageDraw

#===========Defining Class
class Window3:

    #==========Defining Default Constructor============
    def __init__(self,root):    
        self.root=root
        self.root.title("Continue with one of these")
        self.root.geometry("1260x700+0+0")
        self.root.config(bg="black")
    
    #=========Right Label Image===========
        self.bg=ImageTk.PhotoImage(file="college.jpg")
        right_lbl=Label(self.root,image=self.bg)
        right_lbl.place(x=0,y=170,height=388,width=640)

    #============Title Label=================
        title=Label(self.root,text="College Management System",bd=10,relief=GROOVE,font=("times new roman",25,"bold"),fg="black",bg="green")
        title.pack(side=TOP,fill=X)

    #========================================================LABLE======================================

        #==========Label 1
        Label_1 = Label(self.root, text = 'STUDENT PROFILE', font = ('arial',25,'bold'), bg = 'orange')
        Label_1.place(x=740,y=200,height=40,width=340)

        #==========Label 2
        Label_2 = Label(self.root, text = 'TEACHER PROFILE', font = ('arial',25,'bold'), bg = 'orange')
        Label_2.place(x=740,y=290,height=40,width=340)

        #==========Label 3
        Label_3 = Label(self.root, text = 'Course', font = ('arial',25,'bold'), bg = 'orange')
        Label_3.place(x=740,y=380,height=40,width=340)

        #==========Label 4
        Label_4 = Label(self.root, text = 'Fee Detail', font = ('arial',25,'bold'), bg = 'orange')
        Label_4.place(x=740,y=470,height=40,width=340)

    #========================================================BUTTONS===================================================================
        
        #=========Button 1=========
        Button_1 = Button(self.root, text = 'VIEW',font = ('arial',16,'bold'),bd=5,bg="light blue",command=self.std_win)
        Button_1.place(x=1100,y=200,height=40,width=70)
       
        #=========Button 2=========
        Button_2 = Button(self.root, text = 'VIEW', font = ('arial',16,'bold'),bd=5,bg="light blue",command=self.tea_win)        
        Button_2.place(x=1100,y=290,height=40,width=70)

        #=========Button 3=========
        Button_3 = Button(self.root, text = 'VIEW', font = ('arial',16,'bold'),bd=5,bg="light blue",command=self.cour_win)
        Button_3.place(x=1100,y=380,height=40,width=70)

        #=========Button 4=========
        Button_4 = Button(self.root, text = 'VIEW', font = ('arial',16,'bold'),bd=5,bg="light blue",command=self.fees_win)
        Button_4.place(x=1100,y=470,height=40,width=70)

#==============Defining Function std_win===========
    def std_win(self):
        self.root.destroy()
        import poo1

#==============Defining Function tea_win===========
    def tea_win(self):
        self.root.destroy()
        import poo2

#==============Defining Function cour_win===========
    def cour_win(self):
        self.root.destroy()
        import poo3

#==============Defining Function fee_win===========
    def fees_win(self):
       self,root.destroy()
       import poo4

 
root=Tk()
ob=Window3(root)
root.mainloop()