#==========Importing Library===========

#pip install tkinter
from tkinter import*

#pip install pillow
from PIL import Image,ImageTk,ImageDraw 

#import datetime
from datetime import*

#import time
import time

#pip install math
from math import*

#pip install pymysql
import pymysql

#import messagebox from tkinter
from tkinter import messagebox

#import ttk from tkinter
from tkinter import ttk

#=========Defining Class================
class Clock:

    #=======Default Constructor========
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1260x700+0+0")
        self.root.config(bg="#021e2f")

    #========Background Colour======== 
        left_lbl=Label(self.root,bg="black",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=200)

        self.bg=ImageTk.PhotoImage(file="clg3.jpg")
        right_lbl=Label(self.root,image=self.bg)
        right_lbl.place(x=200,y=0,relheight=1,relwidth=1)

    #======== Login Frames=============
        login_frame=Frame(self.root,bg="black")
        login_frame.place(x=250,y=85,width=800,height=500)
        
        #===========Title Label==========
        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",25,"bold"),bg="orange",fg="black").place(x=230,y=40)

        #===========Email Label==========
        email=Label(login_frame,text="EMAIL ADDRESS :",font=("times new roman",20,"bold"),fg="gray",bg="black").place(x=230,y=100)
        self.txt_email=Entry(login_frame,font=("times new roman",15,"bold"),bg="white",fg="black",bd=4)
        self.txt_email.place(x=230,y=140,height=40,width=350)

        #===========Password Label==========
        password=Label(login_frame,text="PASSWORD :",font=("times new roman",20,"bold"),fg="gray",bg="black").place(x=230,y=200)
        self.txt_password=Entry(login_frame,font=("times new roman",15,"bold"),bg="white",fg="black",bd=4)
        self.txt_password.place(x=230,y=250,height=40,width=350)

        #==============Button Register new account==========
        btn_reg=Button(login_frame,text="Register New  Account?",command=self.register_window,font=("times new roman",14),fg="green",bg="black",bd=0).place(x=230,y=300)
        
        #==============Button Forget Password==========
        btn_forget=Button(login_frame,text="Forget Password?",command=self.forget_password_window,font=("times new roman",14),bg="black",fg="dark red",bd=0).place(x=450,y=300)
        
        #==============Button Login==========
        btn_login=Button(login_frame,text="LogIn",command=self.login,font=("times new roman",20,"bold"),bg="orange",fg="black",bd=5).place(x=340,y=350,width=150)
    
    #========Clock Label===========    
        self.lbl=Label(self.root,bg="#0047AB",text="\nClock",font=("times new roman",25,"bold"),bd=0,fg="black",compound=BOTTOM)
        self.lbl.place(x=90,y=110,height=450,width=350)
        self.working()

    #==============Defining reset Function==============
    def reset(self):
        self.cmb_quest.current(0)
        
        self.txt_new_pass.delete(0,END)

        self.txt_answer.delete(0,END)

        self.txt_password.delete(0,END)

        self.txt_email.delete(0,END)

    #========Defining forget_password function==============

    #==========Validation on required fields========
    def forget_password(self):
        if self.cmb_quest.get()=="" :
            messagebox.showerror("Error","All Fields Are Required",parent=self.root2)

        elif self.txt_answer.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root2)

        elif self.txt_new_pass.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root2)

        else:

            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="stud")
                cur=con.cursor()
                cur.execute("select * from emp where email=%s and question=%s and answer=%s",(self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row=cur.fetchone()

                if row==None:  
                    messagebox.showerror("Error","Please select correct security question/Enter answer",parent=self.root2)
                
                else:
                    cur=con.cursor()
                    cur.execute("update emp set password=%s where email=%s ",(self.txt_new_pass.get(),self.txt_email.get()))
                    row2=cur.fetchone()
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Password Reset Successfully",parent=self.root2)
                    self.reset()                  
                    self.root2.destroy()

            except Exception as es:
                messagebox.showerror("Error",f"Error due to : {str(es)}",parent=self.root2)

    #==========Defining Function forget_password_window=============
    
    #==========Validation on required fields========
    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter the email for reset your Password",parent=self.root)   

        else:

            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="stud")
                cur=con.cursor()
                cur.execute("select * from emp where email=%s",self.txt_email.get())
                row=cur.fetchone()

                if row==None:  
                    messagebox.showerror("Error","Enter valid email address",parent=self.root) 

                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("400x400+450+150")
                    self.root2.config(bg="black")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    t=Label(self.root2,text="Forget Password",font=("times new roman",15,"bold"),fg="black",bg="orange").place(x=0,y=10,relwidth=1)
                   
                    #==========Forget Password=========
                   
                    #==========label question========
                    question=Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),bg="black",fg="gray").place(x=40,y=60)
            
                    self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman",13),state='readonly',justify=CENTER)
                    self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
                    self.cmb_quest.place(x=40,y=100,width=200)
                    self.cmb_quest.current(0)

                    #==========label answer========
                    answer=Label(self.root2,text="Answer",font=("times new roman",15,"bold"),bg="black",fg="gray").place(x=40,y=140)
                
                    self.txt_answer=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.txt_answer.place(x=40,y=180,width=250)

                    #==========label new password========
                    new_pass=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="black",fg="gray").place(x=40,y=230)
                
                    self.txt_new_pass=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.txt_new_pass.place(x=40,y=270,width=250)
                   
                    #===========Reset Button========
                    btn_reset=Button(self.root2,text="Reset password",command=self.forget_password,font=("times new roman",20,"bold"),fg="black",bg="orange",bd=5).place(x=40,y=310,width=200,height=45)
                    
            except Exception as es:
                messagebox.showerror("Error",f"Error due to : {str(es)}",parent=self.root)

    #=========Defining Function register_window==========
    def register_window(self):
        self.root.destroy()
        import register

    #=========Defining Function login==========
    #=======Connectivity with database=========
    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":   
            messagebox.showerror("Error","All fields are Required",parent=self.root)

        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="stud")
                cur=con.cursor()
                cur.execute("select * from emp where email=%s and password=%s",(self.txt_email.get(),self.txt_password.get()))
                row=cur.fetchone()

                if row==None:  
                    messagebox.showerror("Error"," Invalid Username & Password",parent=self.root) 

                else:
                    messagebox.showinfo("Welcome",parent=self.root)
                    self.root.destroy()
                    import poo0
                con.close()

            except Exception as es:
                messagebox.showerror("Error",f"Error due to : {str(es)}",parent=self.root)

    #=========Defining Function clock_image==========            
    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(100,180,100))
        draw=ImageDraw.Draw(clock)

        #========For Clock Image=========
        bg=Image.open("c4.jpg")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))

        # Formula to rotate the Anticlock

        #angle_in_radians = angle_in_degrees * math.pi / 180

        #line_length = 100

        #center_x = 250

        #center_y = 250

        #end_x = center_x + line_length * math.cos(angle_in_radians)

        #end_y = center_y - line_length * math.sin(angle_in_radians)

        #========Hour Line Image=========
        # x1,y1,x2,y2
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="white",width=4)

        #=========Min Line Image==========
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="white",width=3)

        #==========Sec Line Image=========
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="red",width=2)
        draw.ellipse((195,195,208,208),fill="gray")
        clock.save("clock_new.jpg")

    #=========Defining Function working==========
    def working(self):
        h=datetime.now().time().hour

        m=datetime.now().time().minute

        s=datetime.now().time().second

        hr=(h/12)*360

        min_=(m/60)*360

        sec_=(s/60)*360

        # print(h,m,s)
        # print(hr,min_,sec_)

        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(Image.open("clock_new.jpg"))
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)
 
root=Tk()
obj=Clock(root)
root.mainloop()