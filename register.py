#=========Importing Library==========

#pip install tkinter
from tkinter import*

from tkinter import ttk

#pip install pillow
from PIL import Image,ImageTk

from tkinter import messagebox

#pip install pymysql
import pymysql

#=========Defining Class==========
class Register:

    #=========Default Constructor==========
    def __init__(self,root):
        self.root=root
        self.root.title("Registeration Window")
        self.root.geometry("1260x700+0+0")
        self.root.config(bg="black")

        #=======BG Image=======
        self.bg=ImageTk.PhotoImage(file="clg3.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,width=2560,height=1440)

        #=======LEFT Image=======
        self.left=ImageTk.PhotoImage(file="img2.jpg")
        left=Label(self.root,image=self.left).place(x=80,y=110,width=398,height=429)

        #=======Register Frame=======
        frame1=Frame(self.root,bg="black")
        frame1.place(x=473,y=50,width=700,height=540)
        
        #=======Title Label==========
        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="orange",fg="black").place(x=50,y=30)
        
        #======================Row1

        #============fname Label=========
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="black",fg="gray").place(x=50,y=100)
        
        #===========fname Entry Field=========
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)

        #============lname Label=========

        #===========lname Entry Field=========
        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="black",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)

        #======================Row2

        #============Contact no. label=========
        contact_no=Label(frame1,text="Contact",font=("times new roman",15,"bold"),bg="black",fg="gray").place(x=50,y=170)
        
        #============Contact no. entry field=========
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)

        #============email Label=========
        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="black",fg="gray").place(x=370,y=170)
       
        #============Email Entry Field=========
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)
        
        #======================Row3

        #============Question Label=========
        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="black",fg="gray").place(x=50,y=240)
        
        #=======Combobox for question field============
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)

         #============Answer Label=========
        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="black",fg="gray").place(x=370,y=240)
        
        #============Answer Entry Field=========
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)

        #======================Row4

        #============Password Label=========
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="black",fg="gray").place(x=50,y=310)
        
        #============Password Entry Field=========
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=50,y=340,width=250)

        #============Confirm Password Label=========
        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="black",fg="gray").place(x=370,y=310)
       
        #============ Confirm Password Entry Field=========
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_cpassword.place(x=370,y=340,width=250)
        
        #======Register Button =======
        self.btn_img=ImageTk.PhotoImage(file="btn3.png")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)
        
        #==========Sign in Buttton====
        btn_login=Button(self.root,text="Sign In",command=self.login_window,font=("times new roman",20,"bold"),bd=4,bg="orange",cursor="hand2").place(x=100,y=420)
    
    #=========Defining Function login_window==========
    def login_window(self):
        self.root.destroy()
        import login
    
    #=========Defining Function clear=========
    def clear(self):
        self.txt_fname.delete(0,END)

        self.txt_lname.delete(0,END)

        self.txt_email.delete(0,END)

        self.txt_contact.delete(0,END)

        self.txt_password.delete(0,END)

        self.txt_cpassword.delete(0,END)

        self.cmb_quest.current(0)

        self.txt_answer.delete(0,END)

    #=========Defining Function register_data==========

    #=======Connectivity with database=========

    #==============Validation with Required Fields============
    def register_data(self):
        if self.txt_fname.get()=="" :
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)

        elif self.txt_email.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)

        elif self.cmb_quest.get()=="Select":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)

        elif self.txt_answer.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)

        elif self.txt_password.get()=="" :
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        
        elif self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)

        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password & Confirm Password should be same",parent=self.root)

        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="stud")
                cur=con.cursor()
                cur.execute("select * from emp where email=%s",self.txt_email.get())
                row=cur.fetchone() 

                if row!=None:  
                    messagebox.showerror("Error","User Already Exist,Please try with another email",parent=self.root)  
                
                else:
                    cur.execute("insert into emp(f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",  
                           (self.txt_fname.get(),

                            self.txt_lname.get(),

                            self.txt_contact.get(), 

                            self.txt_email.get(),

                            self.cmb_quest.get(),

                            self.txt_answer.get(),

                            self.txt_password.get()
                           ))
                    con.commit()
                    self.clear()
                con.close()
                messagebox.showinfo("Success","Successfully Registered",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

root=Tk()
ob=Register(root)
root.mainloop()
