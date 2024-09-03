#=============Importing Libraries============

#pip install tkinter
from tkinter import*

#import ttk from tkinter
from tkinter import ttk

#pip install pillow
from PIL import Image,ImageTk

#import pymysql
import pymysql

#import messagebox from tkinter
from tkinter import messagebox

#pip install datetime
import datetime

#pip install time
import time

#===========Defining Student Class============
class Student:

    #==========Define default constructor==========
    def __init__(self,root):
        self.root=root
        self.root.title("Student Fees Detail")
        self.root.geometry("1260x600+0+0")
        self.root.config(bg="black")

        
#==========All Variable===================
        self.name_var = StringVar()

        self.course_var = StringVar()

        self.total_fee_var = IntVar()

        self.deposit_fee_var = IntVar()

#================Manage Frame================
                
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#5D8AA8")
        Manage_Frame.place(x=20,y=10,width=450,height=580)

        #==========title label===========
        title=Label(Manage_Frame,text="Student Fees",font=("times new roman",20,"bold"))
        title.pack(side=TOP,fill=X)

        #=========name label=========
        name=Label(Manage_Frame,text="Name",font=("times new roman",18,"bold"),fg="black",bg="#5D8AA8").place(x=30,y=70)
        txt_name=Entry(Manage_Frame,font=("times new roman",15,"bold"),textvariable=self.name_var,bd=3,relief=GROOVE)
        txt_name.place(x=195,y=70,width=220)

        #=============course lable
        course=Label(Manage_Frame,text="Course",font=("times new roman",18,"bold"),fg="black",bg="#5D8AA8").place(x=30,y=130)
        self.cmb_cour=ttk.Combobox(Manage_Frame,font=("times new roman",15),textvariable=self.course_var,state='readonly',justify=CENTER)
        self.cmb_cour['values']=("Select",'BCA','DCA','PGDCA','MSC')
        self.cmb_cour.place(x=195,y=130,width=220)
        self.cmb_cour.current(0)

        #==========total lable=========
        total=Label(Manage_Frame,text="Total Fee",font=("times new roman",18,"bold"),fg="black",bg="#5D8AA8").place(x=30,y=190)
        txt_total=Entry(Manage_Frame,font=("times new roman",15,"bold"),textvariable=self.total_fee_var,bd=3,relief=GROOVE)
        txt_total.place(x=195,y=190,width=220)

        #==========fee deposite label==========
        fee_dep=Label(Manage_Frame,text="Fee Deposited",font=("times new roman",18,"bold"),fg="black",bg="#5D8AA8").place(x=30,y=255)
        txt_depo=Entry(Manage_Frame,font=("times new roman",15,"bold"),textvariable=self.deposit_fee_var,bd=3,relief=GROOVE)
        txt_depo.place(x=195,y=255,width=220)

        # fee_new=Label(Manage_Frame,text="New Deposit",font=("times new roman",18,"bold"),fg="black",bg="#5D8AA8").place(x=30,y=290)
        # txt_new=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=3,relief=GROOVE)
        # txt_new.place(x=195,y=290,width=220)

        # remain=Label(Manage_Frame,text="Fee Remaining",font=("times new roman",18,"bold"),fg="black",bg="#5D8AA8").place(x=30,y=345)
        # txt_rema=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=3,relief=GROOVE)
        # txt_rema.place(x=195,y=345,width=220)

        # #=====Deposit Button=========
        self.btn_img=ImageTk.PhotoImage(file="depobtn1.png")
        btn_register=Button(Manage_Frame,image=self.btn_img,bd=2,cursor="hand2",command=self.add_fees).place(x=125,y=350)

        btn_remain=Button(Manage_Frame,text="Remaining Fee",font=("times new roman",18,"bold"),command=self.remain,bg="#303030",fg="white",bd=5,cursor="hand2").place(x=140,y=450,height=60,width=170)

        #==============Table Frame====================== 
       
        Table_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#5D8AA8")
        Table_Frame.place(x=480,y=10,width=765,height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

        self.Student_table=ttk.Treeview(Table_Frame,columns=("name","course","total_fee","deposit_fee","date_time"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command= self.Student_table.xview)
        scroll_y.config(command= self.Student_table.yview)

        #============Headings for Student Table===========
        self.Student_table.heading("name",text="Name")

        self.Student_table.heading("course",text="Course")

        self.Student_table.heading("total_fee",text="Total_fee")

        self.Student_table.heading("deposit_fee",text="Deposit_fee")

        self.Student_table.heading("date_time",text="Date_time")


        self.Student_table['show']='headings'

        self.Student_table.column("name",width=130)

        self.Student_table.column("course",width=60)

        self.Student_table.column("total_fee",width=50)

        self.Student_table.column("deposit_fee",width=100)

        self.Student_table.column("date_time",width=100)

        self.Student_table.pack(fill=BOTH,expand=1)

        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)

        #=====Call fetch data function========
        self.fetch_data()

#=============Create add_fees function=========

#============Connectivity with Database=========

#====================Validation on Required Fields======================
    def add_fees(self):
        if self.name_var.get()=="":
                messagebox.showerror("Error","All fields are required!!!")

        elif self.course_var.get()=="" :
                messagebox.showerror("Error","All fields are required!!!")

        elif self.total_fee_var.get()=="":
                messagebox.showerror("Error","All fields are required!!!")

        elif  self.deposit_fee_var.get()=="":
                messagebox.showerror("Error","All fields are required")

        else:
                ts = time.time()
                timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                con=pymysql.connect(host="localhost", user="root", password="", database = "stud")    
                cur=con.cursor()
                cur.execute("insert into fees values(%s,%s,%s,%s,%s)",(self.name_var.get(),

                                                                    self.course_var.get(),

                                                                    self.total_fee_var.get(),

                                                                    self.deposit_fee_var.get(),

                                                                    timestamp
                                                                    ))
                con.commit()
                self.fetch_data()
                self.clear()

        con.close()
        messagebox.showinfo("Success","Fee Deposited Successfully")

#=============Create fetch_data function=========

#============Connectivity with Database============
    def fetch_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="stud")    
        cur=con.cursor()
        cur.execute("select * from fees")
        rows=cur.fetchall()

        if len(rows)!=0:
                
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                        self.Student_table.insert('',END,values=row)
                con.commit()
        con.close()

#=============Create get_ cursor=========
    def get_cursor(self,ev):

        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']

        self.name_var.set(row[0])

        self.course_var.set(row[1])

        self.total_fee_var.set(row[2])

        self.deposit_fee_var.set(row[3])
#=============Create clear function=========
    def clear(self):

        self.name_var.set("")

        self.course_var.set("")

        self.total_fee_var.set("")

        self.deposit_fee_var.set("")

    def remain(self):
        con=pymysql.connect(host="localhost", user="root", password="", database = "stud") 
        rema=self.total_fee_var.get()-self.deposit_fee_var.get()
        messagebox.showinfo("REMAINING FEES",rema)
        con.commit()
        con.close()


       
root=Tk()
ob=Student(root)
root.mainloop()